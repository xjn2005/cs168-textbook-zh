from __future__ import annotations

import argparse
import http.server
import os
import subprocess
import sys
import threading
import time
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = ROOT / "site"
POLL_SECONDS = 0.8
DEBOUNCE_SECONDS = 0.4
RELOAD_SNIPPET = """
<script>
(() => {
  const events = new EventSource("/__reload");
  events.onmessage = () => window.location.reload();
})();
</script>
""".strip()
WATCH_PATHS = [
    ROOT / "mkdocs.yml",
    DOCS,
]


def iter_watched_files() -> list[Path]:
    files: list[Path] = []
    for path in WATCH_PATHS:
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(item for item in path.rglob("*") if item.is_file())
    return files


def snapshot() -> dict[Path, tuple[int, int]]:
    state: dict[Path, tuple[int, int]] = {}
    for path in iter_watched_files():
        try:
            stat = path.stat()
        except OSError:
            continue
        state[path] = (stat.st_mtime_ns, stat.st_size)
    return state


def inject_reload_script() -> None:
    if not SITE.exists():
        return

    for path in SITE.rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        if "/__reload" in text:
            continue
        if "</body>" in text:
            text = text.replace("</body>", f"{RELOAD_SNIPPET}\n</body>", 1)
        else:
            text = f"{text}\n{RELOAD_SNIPPET}\n"
        path.write_text(text, encoding="utf-8", newline="\n")


def build() -> bool:
    env = os.environ.copy()
    env.setdefault("NO_MKDOCS_2_WARNING", "true")
    env.setdefault("PYTHONWARNINGS", "ignore::DeprecationWarning")

    try:
        subprocess.run(["mkdocs", "build"], cwd=ROOT, check=True, env=env)
        inject_reload_script()
        return True
    except Exception as exc:  # noqa: BLE001 - keep preview alive after bad edits.
        print(f"Build failed: {exc}", file=sys.stderr)
        return False


class PreviewServer(http.server.ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, server_address: tuple[str, int], handler: type[http.server.BaseHTTPRequestHandler]):
        super().__init__(server_address, handler)
        self.reload_version = 0
        self.reload_condition = threading.Condition()

    def notify_reload(self) -> None:
        with self.reload_condition:
            self.reload_version += 1
            self.reload_condition.notify_all()


class PreviewHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802 - stdlib handler API.
        if self.path == "/__reload":
            try:
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream")
                self.send_header("Cache-Control", "no-cache")
                self.send_header("Connection", "keep-alive")
                self.end_headers()
            except OSError:
                return

            server = self.server
            assert isinstance(server, PreviewServer)
            last_seen = server.reload_version
            while True:
                with server.reload_condition:
                    server.reload_condition.wait_for(
                        lambda: server.reload_version != last_seen,
                        timeout=30,
                    )
                    if server.reload_version == last_seen:
                        payload = ": keep-alive\n\n"
                    else:
                        last_seen = server.reload_version
                        payload = f"data: {last_seen}\n\n"
                try:
                    self.wfile.write(payload.encode("utf-8"))
                    self.wfile.flush()
                except (BrokenPipeError, ConnectionAbortedError, ConnectionResetError, OSError):
                    return
            return

        super().do_GET()

    def log_message(self, format: str, *args: object) -> None:
        if self.path == "/__reload":
            return
        if len(args) >= 2 and str(args[1]) in {"200", "304"}:
            return
        print(format % args)


class SitePreviewHandler(PreviewHandler):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, directory=SITE, **kwargs)


def watch_and_rebuild(server: PreviewServer) -> None:
    current = snapshot()
    while True:
        time.sleep(POLL_SECONDS)
        updated = snapshot()
        if updated == current:
            continue

        time.sleep(DEBOUNCE_SECONDS)
        updated = snapshot()
        if updated != current and build():
            current = updated
            server.notify_reload()
            print("Rebuilt preview.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=4173, type=int)
    parser.add_argument("--build-only", action="store_true")
    args = parser.parse_args()

    if not build():
        return 1
    if args.build_only:
        return 0

    server = PreviewServer((args.host, args.port), SitePreviewHandler)
    watcher = threading.Thread(target=watch_and_rebuild, args=(server,), daemon=True)
    watcher.start()

    print(f"Serving at http://{args.host}:{args.port}/")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Stopping preview.")
    finally:
        server.server_close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
