---
title: Core-Based Trees
parent: Beyond Client-Server
nav_order: 4
layout: page-with-toc
---

# Core-Based Trees (CBT)

## CBT 定义

Multicast routing 的目标仍然相同：我们有一个 destination 是 group 的 packet，router 需要协同工作，把这个 packet forward 给 group 的所有 member。

不过，现在我们会尝试一种不同方法，它与 DVMRP 完全不同。

<img width="900px" src="/assets/beyond-client-server/7-032-cbt-taxonomy.png">

在 **Core-Based Tree（CBT）** 方法中，每个 destination group 都有自己的 tree。某个 destination group 的 CBT 就是一棵触达该 group 每个 member 的 tree。

<img width="600px" src="/assets/beyond-client-server/7-033-cbt-end-goal.png">

同时思考 CBT tree 和 DVMRP tree 可能会让人困惑。现在，你可以把它们看成完全不同、彼此没有共同点的 tree。

## 构建 CBT

为了构建 core-based tree，这棵 tree 需要一个 root，我们称之为 core。Core 是 network 中某个提前选定的任意 router。

现在，我们会以 core 为 root，构建一棵触达每个 group member 的 tree。

如果某个 member 想加入 group，这个 member 会向 core unicast 一条 join message。这个 packet 会穿过若干 router 到达 core。所有这些 router 也会加入 tree，因此 tree 现在有了一条从 core 到新 member 的 path。

<img width="800px" src="/assets/beyond-client-server/7-034-cbt-join-1.png">

<img width="600px" src="/assets/beyond-client-server/7-035-cbt-join-2.png">

更正式地说，如果你是一个 router，并且收到某个特定 group 的 join message，你就知道自己现在是这个 group 的 tree 的一部分。Join message 的 incoming link 是你的 child（指向远离 root 的 link）。Join message 的 outgoing link（到 root 的 next-hop）是你的 parent（指向 root 的 link）。你可以记下 parent 和 child，从而记住自己在 tree 中的位置。没有一个全局 mastermind 记住整棵 tree；tree 上的每个 router 都负责记住自己的 parent 和 child。

<img width="900px" src="/assets/beyond-client-server/7-036-cbt-join-recap.png">

如果某个 member 想离开 group，它可以向 tree 上自己的直接 parent unicast 一条 quit message。如果你在 tree 上的所有 child 都发送了 quit message，这意味着你也可以离开 tree，所以你可以向自己的直接 parent 发送 quit message。Quit message 会发送给直接 parent，不会再继续 forward。

<img width="700px" src="/assets/beyond-client-server/7-037-cbt-leave-1.png">

<img width="600px" src="/assets/beyond-client-server/7-038-cbt-leave-2.png">

<img width="900px" src="/assets/beyond-client-server/7-039-cbt-quit-recap.png">

记住，我们为每个 group 构建一棵 tree。这意味着 router 必须为自己所属的每棵 tree 记住 parent 和 child。另外，join 和 leave message 必须关联到特定 group，例如“我想加入 group G2”。

<img width="600px" src="/assets/beyond-client-server/7-040-multiple-1.png">

<img width="600px" src="/assets/beyond-client-server/7-041-multiple-2.png">

下面是关于 core 的一些细节，不过它们不是这个 protocol 背后的主要直觉。
- 由于 core 是一个 router，它有 unicast IP address，所有人都可以向 core 发送 unicast packet。
- 我们为每个 group 构建一棵 tree。不同 group 可以使用不同 core。
- 我们会假设每个人都知道 group 到 core 的 mapping，例如“Group G1 使用 R2 作为 core”。这个 mapping 可以用类似 DNS 的方式发布（回忆一下：DNS 适合分发 key-value pair）。
- Core 不是 group member。在我们的模型中，我们假设 host 可以加入或离开 group，而不是 router。Core 是 router，因此它不会加入 multicast group。

下面是关于 join 和 quit message 的一些细节，不过它们不是这个 protocol 背后的主要直觉。
- Join 和 quit message 在技术上由 first-hop router 发送。Router 使用 IGMP 检测自己的某个 directly-connected host 加入或离开了 group，然后 first-hop router 发送 join 或 quit message。
- 现实中，join message 会收到 JOIN-ACK 作为响应，router 会在 JOIN-ACK 发送时记录自己的 parent 和 child。类似地，quit message 会收到 QUIT-ACK 作为响应。在这门课中，我们会忽略这个 feature。

## 使用 CBT

现在我们已经为一个 group 构建了 CBT，该如何使用它向这个 group 发送 message？

情况 1：如果你是 group member，意味着你已经接触到这棵 tree。因此，你只需要把 message broadcast 给 tree 上的每个人。

更具体地说，你首先把 packet forward 给 tree 上的 parent。然后，tree 上的每个 router 收到 packet，并把 packet flood 到自己的所有 tree link（包括 parent link 和 child link）。

<img width="700px" src="/assets/beyond-client-server/7-042-cbt-forwarding-1.png">

情况 2：如果你不是 group member，你没有接触到这棵 tree，因此情况 1 的策略不可行。相反，你可以把 packet unicast 给 core。然后，core 可以把 message broadcast 给 tree 上的每个人。

更具体地说，当你把 packet unicast 给 core 时，需要 encapsulate 这个 packet。Outer header 包含到达 core 的 unicast information。Inner header 包含 multicast information。

当 core 收到 packet 时，它解开 outer header，并看到内部的 multicast packet。然后，core 就可以沿 tree broadcast 这个 packet。和情况 1 一样，tree 上的每个 router 收到 packet，并把 packet flood 到自己的所有 tree link（parent 和 child link）。

<img width="900px" src="/assets/beyond-client-server/7-043-cbt-forwarding-2.png">

## 好处：更好的扩展性

回忆一下，DVMRP 扩展性差，因为 router 必须跟踪每个 source、每个 destination group 的一棵 tree。每棵 tree 展示从一个 source 到一个 destination group 中所有 member 的 shortest path。

在 CBT 方法中，某个 destination group 的 CBT 只是一棵触达该 group 每个 member 的 tree。

注意，CBT 对所有 source 都相同。不同于 DVMRP（每个 source、每个 destination group 一棵 tree），现在我们只有每个 destination group 一棵 tree。

<img width="900px" src="/assets/beyond-client-server/7-044-dvmrp-cbt-scaling.png">

比较 DVMRP tree 和 CBT tree 有助于理解 protocol 如何扩展，但除此之外，每个 protocol 中构建的 tree 语义完全不同。如果你感到困惑，可能更容易把这些 tree 看成完全分开的概念主题。

回忆一下，DVMRP 的另一个扩展性问题是 pruning state 会被周期性清除；当这种情况发生时，packet 会被 broadcast 给 network 上的所有人（包括非 group member）。CBT 也解决了这个问题，因为 CBT operation 中没有任何时候需要把 packet broadcast 给所有人。Tree 本身告诉我们 group member 在哪里，因此确保非 group member 永远不会收到 packet。

## 效率分析

回忆一下，DVMRP 从 sender 到所有 group member 构建 least-cost tree。通过沿这些 tree forward packet，我们确保 packet 会沿 least-cost path forward 到所有 group member。

相比之下，CBT tree 完全不涉及 sender，因此不再保证 optimality。从 sender 到所有 group member 的 path 不一定是 least-cost path。

CBT 用效率换取扩展性。CBT 更可扩展，因为需要构建的 tree 更少（也就是 router 存储更少 state）；但作为交换，packet 可能沿 suboptimal path forward。

CBT 的效率高度依赖于选择哪个 router 作为 core。例如，考虑下面这个 topology 以及若干 core 选择。

<img width="700px" src="/assets/beyond-client-server/7-045-core-choice-1.png">

<img width="700px" src="/assets/beyond-client-server/7-046-core-choice-2.png">

<img width="700px" src="/assets/beyond-client-server/7-047-core-choice-3.png">

在每一种 core 选择中，至少有一对 router 由 suboptimal path 连接。我们不再有一棵从某个 source 到所有 group member 的 guaranteed shortest paths tree。

例如，如果 A 计划向 group 发送大量 packet，R2 可能是不错的 core 选择，因为它刚好沿 shortest path 连接 A 到 B 和 C。不过，如果 B 想向 group 发送 packet，这些 packet 到 C 时会走 suboptimal path。

寻找最优 core 是不可行的，尤其是 member 可以随时加入和离开 group。在实践中，operator 通常手动选择 core。

## CBT 的其他优点和缺点

CBT 在 root 处产生单点故障。为了引入 fault-tolerance，我们需要让 tree 有多个 core。这可以做到，但会引入更多 complexity。我们不会进一步讨论 multi-core tree，不过如果你好奇，可以看下面链接的 paper。

回忆一下，DVMRP 是作为 distance-vector 的扩展构建的，这导致 multicast protocol（DVMRP）和 unicast protocol（distance-vector）紧密耦合。改变一个 protocol 也要求更新另一个 protocol。相比之下，CBT 与 unicast routing protocol 解耦。CBT 确实会使用 unicast forwarding table（例如把 join message forward 到 root），但这些 forwarding table 如何生成并不重要（distance-vector、link-state、hard-coded 等都可以）。因此，CBT 不依赖任何特定 unicast protocol，并且可以和任何 unicast protocol 一起工作。

CBT 延伸阅读：[https://people.eecs.berkeley.edu/~sylvia/cs268-2019/papers/cbt.pdf](https://people.eecs.berkeley.edu/~sylvia/cs268-2019/papers/cbt.pdf)

DVMRP 和 CBT 哪个更好？正如我们看到的，这两个 protocol 之间存在 trade-off。

如果你有一个 source 向一个大型 group 发送数据，那么 DVMRP 可能是更好的解决方案，因为它会确保所有数据沿 network 中的 optimal path 传输。大量数据正在被发送（给许多 group member），因此使用 optimal path 会显著节省 bandwidth。另外，如果 group 很大（例如包含 network 中几乎所有人），那么 DVMRP 偶尔发生 flooding 可能不是大问题。

相比之下，如果你有一个小 group，其 member 分散在一个大型 network 中，那么 CBT 可能是更好的解决方案。CBT 会避免把 packet flood 给非 member，否则会浪费大量 bandwidth（因为大多数 host 不在 group 中）。

在实践中，DVMRP 和 CBT 今天都仍被使用。DVMRP 有时称为 PIM-DM（Protocol Independent Multicast - Dense Mode），这反映出 DVMRP 适合大型 group。CBT 有时称为 PIM-SM（Protocol Independent Multicast - Sparse Mode），这反映出 CBT 适合较小 group。
