---
title: Network Architecture
parent: Introduction
nav_order: 4
layout: page-with-toc
---

# Network Architecture（网络架构）

## 设计范式

到目前为止，我们一直从自底向上的视角观察 Internet：从最基础的构件开始，逐步构建整体图景。在这一节中，我们会改用自顶向下的视角观察 Internet，并分析其设计中更高层的架构选择。

这些 Internet 设计范式影响了 Internet 为什么会以今天这种方式运行，也影响了我们在 Internet 之上构建的 application。这些范式与历史上构建系统的方式相比，是一次非常激进的转变。

这些设计只是许多可能设计中的一种。很多 design choice 是多年前做出的，当时 Internet 还没有成长到今天这样的规模。其他设计当然也存在，而且关于「什么设计最好」的争论至今仍然存在。

例如，Internet 被设计成联邦式系统，也就是独立运营者之间彼此合作。但近些年，software-defined networking（SDN，软件定义网络）作为一种更中心化的网络管理方式出现了。

在最初的 Internet 中，switch 被有意设计得很「笨」：它只负责转发数据，而不解析数据。然而，在现代 Internet 中，攻击者可能会用大量无用数据淹没 switch，switch 可能需要某种方式检测这种情况。早期提出简单基础设施范式的 Internet 设计者，并没有考虑到这种安全影响。

## 窄腰

在某一层可以有多个 protocol。例如，在 Layer 7，我们可以使用 HTTP 提供网站服务，也可以使用 NTP 同步系统时钟，它们都构建在同一个 Internet 基础设施之上。又例如，在 Layer 2，我们可以对有线网络使用 Ethernet，也可以对无线网络使用 Wi-Fi。

注意，虽然某一层可以有多个 protocol，但你的 application 可以选择固定使用一组特定的 protocol stack（协议栈）。例如，你可以选择 HTTP over TCP over IP，而不需要使用其他 Layer 7 或 Layer 4 protocol。这样，所有使用你这个 application 的人都会使用同一套 stack。

<img width="900px" src="/assets/intro/1-31-multi-protocols.png">

观察这张图，你会注意到 Layer 3 只有一个 protocol。这就是让 Internet connectivity 成为可能的 **narrow waist（窄腰）**。归根到底，Internet 上的所有人都必须同意使用 IP，packet 才能在整个 Internet 中传输。

## Demultiplexing（解复用）

TODO：补充 demultiplexing（解复用）内容。

<img width="900px" src="/assets/intro/1-32-demultiplex.png">

<img width="500px" src="/assets/intro/1-33-layer3-demultiplex.png">

<img width="700px" src="/assets/intro/1-34-layer4-demultiplex.png">

<img width="700px" src="/assets/intro/1-35-demultiplex-headers.png">

<img width="900px" src="/assets/intro/1-36-ports.png">

注意命名。在 networking 中，port（端口）这个词会指两种不同的东西。Physical port（物理端口）是你把 link 插进 switch 的实际物理位置。Logical port（逻辑端口）则是 Layer 4 header 中的一个数字，用于区分一个 packet 属于哪个 application。

<img width="700px" src="/assets/intro/1-37-logical-physical-port.png">

注意：**socket** 指的是 OS（操作系统）中用于把 application 连接到 OS networking stack 的机制。当 application 打开一个 socket 时，这个 socket 会关联到一个 logical port number（逻辑端口号）。当 OS 收到 packet 时，它会使用 port number 将 packet 交给对应的 socket。

<img width="900px" src="/assets/intro/1-38-layers-in-os1.png">

<img width="900px" src="/assets/intro/1-39-layers-in-os2.png">

<img width="900px" src="/assets/intro/1-40-layers-in-os3.png">

## End-to-End Principle（端到端原则）

为什么我们要把 Internet 设计成这样的分层结构？为什么只有 host 理解 Layer 4 和 Layer 7，而 router 不需要理解这些层？

**end-to-end principle（端到端原则）** 为 Internet 设计提供了重要的智慧和指导。MIT 科学家、Internet Architecture Board 成员 David D. Clark 是这一原则的重要贡献者。他的两篇论文「End-to-End Arguments in System Design」（1981）和「The Design Philosophy of the DARPA Internet Protocols」（1988）对 Internet 设计哲学产生了巨大影响。

End-to-end principle 指导我们讨论 network 应该实现哪些功能、不应该实现哪些功能。这个原则非常宽泛，应用范围很广；但在这里，我们聚焦一个问题：reliability（可靠性，Layer 4）应该由 network 实现，还是只由 end host 实现？

现在，我们先考虑一个简单的 reliability protocol。Host A 想向 Host B 发送 10 个 packet，于是它把编号为 1 到 10 的 packet 通过 network 发送出去。目标是让 B 要么收到所有 packet，要么意识到有些 packet 丢失并报错（这里我们先忽略如何从错误中恢复）。

如果我们在 network 中实现 reliability，Internet 会是什么样子？不同于前面看到的图，现在每个 router 除了理解 Layer 1、2、3，还必须理解 Layer 4。

在这个新图景中，中间 router 必须可靠地把 packet 发送到 next hop。它必须保证 next hop 收到了所有 packet；如果没有，router 必须重新发送丢失的 packet。Host 不检查所有 packet 是否都已收到，而是依赖 network 来确保所有 packet 都被收到。

<img width="900px" src="/assets/intro/1-41-reliability-in-network.png">

在这种方法中，host 必须信任 network。如果某个 router 有 bug 并丢弃了 packet，host 实际上没有什么办法处理。

<img width="900px" src="/assets/intro/1-42-buggy-reliability-in-network.png">

另一种方法是 end-to-end approach（端到端方法）：我们不在 network 中实现 reliability，而是强制两个 end host 来保证 reliability。Router 可以丢弃 packet，是否所有 packet 都已收到则由 end host 自己验证。

<img width="900px" src="/assets/intro/1-43-reliability-in-endhost.png">

在 end-to-end approach 中，reliability 由 end host 实现，因此控制权在 host 手中。Host 仍然可能有 bug 并丢弃 packet，但这一次，host 有能力自己修复 bug。更一般地说，如果你在写代码，最好由你自己控制某个 feature 是否正确，而不是依赖其他可能出错的人，而且你还无法修复他们的错误。

带着这个比较来看，如果我们采用第一种方法，也就是依赖 network 保证正确性，那么当 network 有 bug 时，我们实际上无法保证完美 reliability。End host 很可能最终仍然会像第二种方案那样进行 end-to-end check（端到端检查）。

在旧 Internet 中，每条 link 确实实现了 reliability。然而，如我们所见，现代 Internet 在 network 中只实现 best-effort，并强制 end host 实现 reliability，这与 end-to-end principle 一致。

总结：某些应用需求必须 end-to-end 地实现，才能保证正确性。同时，end-to-end 实现本身已经足够，不需要 network 提供额外支持。因为单独的 end-to-end 实现已经足够，向 network 添加功能只会引入不必要的额外复杂度和成本，却不能真正帮助我们达成需求。

注意，end-to-end principle 并不是一个永远成立的证明或定理。它是一条指导原则和哲学论证，不同设计者可能会提出支持或反对这一原则的不同论点。

下面是一个例子，说明 end-to-end principle 并不是严格规则。虽然 end-to-end principle 说 reliability 应该只在 end host 中实现，但我们仍然可以在 network 中额外增加一些 reliability，作为 end-to-end check 的补充。如果 link 非常不可靠，这可能会很有用。假设 A 和 B 之间有 10 条 link，每条 link 有 10% 的概率失败。那么每次发送 packet 时，它有 65% 的概率会被丢弃。然而，如果每个 router 为了 reliability 都发送两份 packet，那么每条 link 的失败概率只有 0.1%，packet 被丢弃的概率也只有 1%。Wireless link 有时会实现 reliability，以降低错误率并提升 end host 的性能。

End-to-end principle 也扩展到了其他领域。例如，在 security（安全）中，end-to-end principle 可能会说，两个 end host 通信时应该在 end host 上加密消息，而不是在 network 的中间节点加密。

用 Clark 的原话来说，end-to-end argument 是：「The function in question can completely and correctly be implemented only with the knowledge and help of the application at the end points. Therefore, providing that function as a feature of the communication system itself is not possible. Sometimes an incomplete version of the function provided by the communication system may be useful as a performance enhancement.」
