---
title: IP Multicast Challenges
parent: Beyond Client-Server
nav_order: 5
layout: page-with-toc
---

# IP Multicast Challenges

## Inter-Domain Routing

到目前为止描述的 protocol（IGMP、DVMRP、CBT）可以用于 intra-domain multicast routing。不过，它们不容易扩展到 inter-domain multicast routing。

这里的一个主要问题是 scalability。例如，如果在全球规模使用 DVMRP，那么每当 pruning state 被周期性删除时，packet 都会被 flood 到整个 Internet，这并不现实。

另外，回忆一下，inter-domain routing 会引入 AS autonomy 和 privacy 这两个额外 challenge。例如，如果在全球规模使用 CBT，那么 core router 可能位于另一个 network 中，这要求你信任别人来控制 core router。

Inter-domain multicast routing 是一个困难问题，已经有许多工作尝试开发解决方案。例如，CBT core selection 问题可以通过让多个 core（每个 network 一个）相互通信来解决。不过，在实践中，inter-domain multicast routing 的采用非常少。

## Charging

IP multicast service model 从根本上与现代 ISP 使用的商业模式相冲突。例如，考虑这个 AS graph，其中 AS A 和 AS B 是 peer：

<img width="400px" src="../assets/beyond-client-server/7-048-multicast-charging-1.png">

作为 peer，AS A 和 AS B 应该能交换等量 traffic，但 multicast 让“等量 traffic”很难定义。举例来说，假设 AS A 向 AS B 发送一个 multicast packet。AS B 可能有许多 child 是这个 group 的一部分。这意味着 AS B 收到一个 packet，却必须发送出许多 packet。这里 AS B 使用的 bandwidth 比 AS A 多得多。AS A 是否需要因此额外付钱给 AS B？（这是一个 open question，没有明确答案。）

再举一个例子，考虑这个 AS graph，其中 AS A 是 provider，AS B 是 customer：

<img width="200px" src="../assets/beyond-client-server/7-049-multicast-charging-2.png">

AS B 正在向 AS A 付费购买 service。如果 AS B 发送一个 multicast packet，而 AS A 必须把这个 packet 的副本 forward 到许多其他 destination，会怎么样？相比 unicast packet，AS A 是否应该对这个 packet 收取更高费用？如果应该，又应该多收多少？（这是一个 open question，没有明确答案。）

设计商业模式更加困难，因为 IP multicast model 并不会显式跟踪 group size。如果你想根据 destination group 的大小向 user 收费，没有清晰方式确定任意给定 destination group 的大小。你的 forwarding table 会告诉你不同 delivery tree 上的 parent 和 child，但这些 table 不会告诉你总共有多少 end host 会收到这个 packet。

## Congestion Control

考虑一个 source 沿 delivery tree 向许多 recipient 发送 multicast packet。Source 需要选择一个合适的 sending rate，以避免让 network 过载。Source 应该选择什么 rate？

<img width="800px" src="../assets/beyond-client-server/7-050-multicast-congestion.png">

Traffic 会沿许多不同 path 传输，而每条 path 可能有不同 capacity。Source 可以以 1 Mbps 发送，以避免让任何 link 过载，但这会让其他 path 上的 capacity 闲置。另一方面，source 可以以 100 Mbps 发送来最大化性能，但这会让一些 link 过载。Source 应该选择什么 rate，并没有明确答案。

在实践中，一种可能方案是根据性能定义不同 group。例如，我们可以定义 4 个不同 multicast group，每个 group 接收相同的视频流，但视频质量不同。然后，任何感兴趣的 recipient 都可以尝试加入不同 group，看看哪个 group 给自己的性能最好。

## Reliability

就像 IP unicast 一样，IP multicast 是 best-effort，这会引入一些额外 complexity。例如，你可能发送一个 packet，它可能到达一些 group member，但没有到达所有 group member。

我们可以尝试添加 ack 来解决这个问题，但这也可能有问题。如果 group 有数百万个 member，单个 sender 无法为每个 packet 处理数百万个 ack。

另一种可能方法是使用 negative acknowledgement（nack）。如果 group member 收到 packet，就什么也不发送；如果没有收到 packet（例如 timer 过期），就发送 nack。同样，如果 group 有数百万个 member，单个 sender 可能会被压垮。

在 nack 方法中，如何从 failure 中恢复也不清楚。如果有人没有收到 packet，我们是否要把 packet 再次 multicast 给整个 group？这会浪费 bandwidth，因为一些 group member 已经收到 packet，并且会收到重复副本。

另一种方法是只把 packet unicast 给发送 nack 的 group member。如果许多 group member 没有收到 packet，这可能会很浪费，因为我们必须 unicast 许多份相同 packet。例如，考虑最开始的第一条 link 丢弃 packet 的情况，这意味着没有任何 group member 收到 packet。

哪种 retransmission 方法更好？这并不立即清楚，并且可能取决于有多少 group member 收到了 packet。

在实践中，一些现代 IP multicast application 根本不实现 reliability。或者，它们通过把一些 redundancy 编码进 data stream 来实现 reliability（想象 error-correcting code），使 loss 和 corruption 可以从数据本身纠正，而不需要 network 帮助。

编码 redundancy 确实意味着你需要更多 bit 来编码相同数据。例如，如果你想发送 5 个 packet 的数据，可能会发送 10 个 packet，并以某种方式编码 bit，使得任意 5 个 packet 都能用于重构原始数据。

## Security

IP multicast 的另一个限制是缺少 access control。任何人都可以加入 group，任何人也都可以向任何 group 发送 message。如果你想强制 access control（例如只有付费 user 才能观看体育比赛），就必须单独构建这个功能。

缺少 access control 会导致 security vulnerability。恶意 sender 可以向某个特定 multicast group flood packet，导致该 group 的所有 member 都被压垮。注意，这比 unicast 替代方案更有效；在 unicast 中，恶意 sender 必须分别向每个 member flood packet。

加密这类额外 security measure 也很难实现。假设你通过给每个 group member 一个 shared secret key 来加密 multicast message。如果有人离开 group，会怎样？如果继续使用同一个 key，这个 user 仍然知道 secret key，并且可以读取你的 message。一种方法是切换到新 key，但现在你需要一种方式，把这个新 key 安全地分发给剩余 group member。

## 实践中的 IP Multicast

由于所有这些 challenge，今天 IP multicast 大多只在单个 domain 内使用，而不是跨不同 domain 使用。

有些 application 可能仍然希望跨多个 network 进行 group communication（例如多人游戏、视频会议）。许多 application 没有依赖不支持 inter-network communication 的 IP multicasting，而是实现了自己的 custom solution 来支持 group communication。

例如，如果 group 足够小，application 可以实现一个 central relay server。Group communication 会 unicast 到 central relay server，然后 relay server 再把 message unicast 给其他 group member。

或者，如果 group 足够小，朴素的基于 unicast 的方案（向每个 group member 分别发送 unicast packet）可能也完全可行。

如果 IP multicasting 不能跨 domain 工作，而 custom solution 又需要额外工作来实现和扩展，现代 application 如何处理 group communication？一种解决方案是使用 overlay multicast，它是 IP multicast 的替代方案，在 Layer 7 而不是 Layer 3 实现 network functionality。接下来我们会看 overlay multicast。
