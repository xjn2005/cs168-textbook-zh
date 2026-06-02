---
title: IP Multicast
parent: Beyond Client-Server
nav_order: 2
layout: page-with-toc
---

# IP Multicast

## IP Multicast 简史

IP multicast 在 1990 年代和 2000 年代被积极研究和开发。推动这项发展的预期是：Internet 的 killer application 会是直播电视或广播。（趣闻：最早的直播音乐会之一是 1994 年的 Rolling Stones。）

回头看，1990 年代和 2000 年代开发的 IP multicast protocol 在采用情况上成败参半。现代 router 确实支持我们将要看到的 IP multicast protocol，但 network operator 并不总是在 router 上启用这些 protocol。（在 router 上禁用 protocol，本质上意味着 router 不理解或不支持该 protocol。）

IP multicast protocol 有时会在单个 domain 内使用（例如 datacenter network 内部）。不过，IP multicast protocol 很少或几乎从不跨不同 domain 部署。这意味着 user 不能期待在 global Internet 层面使用 IP multicast。例如，如果世界各地的一组 user 加入一个 multicast group，现代 Internet 不会自动支持向这个 group multicast packet。

虽然这些 protocol 没有被全球部署，但这些 protocol 中使用的技术可以应用到其他网络问题上。特别是，这些技术在解决与 AI training 相关的问题时重新变得重要（我们讨论 collective 时会学习）。

## IP Multicast Service Model

我们如何定义一个 group？每个 multicast group 由一个 IP address 定义。从 224.0.0.0 到 239.255.255.255 的地址是 multicast address，所有人都知道这个 hard-coded range 中的地址是 multicast address。

<img width="500px" src="/assets/beyond-client-server/7-005-multicast-addresses.png">

要加入一个 group，你会 announce 你想加入的 group 的 multicast address。至少一个 router 应该听到你的 message（例如你的 home router），然后 router 会彼此协调传播这条信息（例如使用 routing protocol）。最终，所有 router 都会知道你是这个 group 的一部分。

<img width="900px" src="/assets/beyond-client-server/7-006-join-message.png">

类似地，你可以 announce 自己正在离开一个 group，并且同样使用 multicast address 标识你所指的是哪个 group。

<img width="900px" src="/assets/beyond-client-server/7-007-leave-message.png">

要向一个 group 发送 packet，你只需要把 multicast group address 填入 IP destination field。然后，router 会使用这个 group address，把 packet forward 给所有 group member。注意，作为 sender，你不需要关心谁属于这个 group，因为 router 会替你弄清楚。

<img width="900px" src="/assets/beyond-client-server/7-008-multicast-forwarding.png">

总结一下，IP multicast service model 为 end host 定义了三个 operation：你可以向一个 group 发送 packet（即使你自己不是这个 group 的一部分）。你可以 announce 自己正在加入一个 group。你可以 announce 自己正在离开一个 group。在这三个 operation 中，你的工作都只是发送 packet。Router 会处理这些 packet，彼此协调（例如运行 routing protocol），并相应地决定如何 route multicast packet。

现在我们知道 host 如何与 IP multicasting 交互（发送、加入、离开），就可以思考 router 如何传递 multicast packet。

在 unicast model 中，router 收到一个 packet，并沿单个 next-hop forward 这个 packet。现在，在 IP multicast model 中，当 router 收到一个 multicast packet（也就是 destination 是 multicast group address）时，router 会沿零条、一条或多条 outgoing link forward 这个 packet，使 packet 到达所有 group member。

为了实现 multicast，router 需要一些额外 state 来跟踪 group membership，这样 router 才能只把 packet forward 给通向 group member 的 next-hop。如果某个 next-hop 不通向任何 group member，就没有必要沿这个 next-hop 发送 packet。随着 user 加入和离开 group，router 针对这个 group 的 next-hop 也可能变化。

## 实现 Multicast

定义好 service model 后，我们现在可以在 router 中实现 IP multicasting。记住这里的最终目标：user 通过发送 packet、announce join 和 announce leave 与 network 交互。Router 必须获取这些信息，并用它正确地把 multicast packet forward 给该 group（由 multicast address 定义）的所有 member。

我们可以把这个问题分成两部分：

1. Router 如何知道它直接连接的 host 属于哪些 group？我们会使用一个叫 IGMP 的 protocol 来解决这个问题。

    <img width="900px" src="/assets/beyond-client-server/7-009-igmp-taxonomy.png">

2. Router 如何通过 network forward packet，使其到达 destination group member？我们会看两个解决这个问题的 protocol：DVMRP 和 CBT。两个 protocol 实现相同目标，因此你可以在实现中任选一个（就像你可以选择 distance-vector 或 link-state，但不会两个都用）。

    <img width="900px" src="/assets/beyond-client-server/7-010-dvmrp-cbt-taxonomy.png">

## IGMP：Directly-Connected Host

在解决更大的 multicast routing 问题之前，我们先从一个较小的问题开始。假设一个 router 直接连接到许多 host。Router 需要某种方式知道每个 host 属于哪些 group。我们会使用一个叫 IGMP（Internet Group Management Protocol）的 protocol 来实现这一点。

从高层看，router 和 host 会交换 message，使 router 得知每个人的 group membership。可以交换的 message 类型包括：

**Queries：** Router 周期性地向 host 发送 Query。这些 message 会问：你属于哪些 group？

**Reports：** 作为响应，host 会把 Report 发回 router。Report 回答这个问题：这些是我所属的 group。Host 也可以发送 unsolicited Report（也就是不等待 Query）。

<img width="900px" src="/assets/beyond-client-server/7-011-igmp-queries-reports.png">

通过周期性交换 Query 和 Report，router 可以掌握最新的 group membership。如果 router 很久没有收到某个 membership 的 Report，router 会假设这个 membership 已经过期并将其 invalidated。

IGMP 帮助 router 了解 directly-connected host。不过，router 仍然不知道 network 其他地方的其他 host，因此我们还需要 routing algorithm 来处理那些 host。

为了和 distance-vector routing 做比较，你可以把 IGMP 看成 multicast 版本的 static routing：router 了解自己 directly-connected host（但不了解 network 其他地方的其他 host）。
