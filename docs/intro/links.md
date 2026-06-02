---
title: Links
parent: Introduction
nav_order: 6
layout: page-with-toc
---

# Links（链路）

## Link 的属性

现在我们已经了解 Internet 的各个 layer 是如何构建起来的，接下来关注一个 packet 如何跨越一条 link（链路）发送。

我们可以用三个属性来衡量一条 link 的性能。

Link 的 **bandwidth（带宽）** 表示单位时间内我们能在这条 link 上发送多少 bit。直观地说，这就是 link 的速度。如果把 link 想象成一根输水管，bandwidth 就是管子的宽度。更宽的管子允许我们每秒把更多水送入管中。我们通常用 bits per second（每秒 bit 数）衡量 bandwidth，例如 5 Gbps = 每秒 50 亿 bit。

Link 的 **propagation delay（传播延迟）** 表示一个 bit 沿着 link 传播需要多长时间。在水管类比中，这对应 link 的长度。更短的管子意味着水在到达另一端之前停留在管中的时间更短。Propagation delay 用时间衡量，例如 nanosecond（纳秒）、millisecond（毫秒）。

如果把 bandwidth 和 propagation delay 相乘，就得到 **bandwidth-delay product（BDP，带宽时延积）**。直观地说，这是 link 的 capacity（容量），也就是任意时刻存在于 link 上的 bit 数量。在水管类比中，如果我们把管子装满并冻结时间，管子的 capacity 就是这一瞬间管子里有多少水。

<img width="600px" src="/assets/intro/1-57-link-properties.png">

注意：你有时会看到 **latency（时延）** 这个词。在 link 的语境中，latency 就是它的 propagation delay；不过这个词也可以用于其他语境，例如从一个 end host 到另一个 end host、跨越多条 link 的 latency。Latency 本身并没有一个脱离语境的严格定义。

## Timing Diagram（时序图）

假设我们有一条 link，它的 bandwidth 是 1 Mbps = 每秒 100 万 bit，propagation delay 是 1 ms = 0.001 秒。

我们想沿这条 link 发送一个 100 byte = 800 bit 的 packet。从第一个 bit 被发送开始，到最后一个 bit 被接收为止，需要多长时间？

为了回答这个问题，我们可以画一个 timing diagram（时序图）。左侧竖条是 sender，右侧竖条是 recipient。时间从 0 开始，并随着我们沿图向下移动而增加。

<img width="300px" src="/assets/intro/1-58-timing1.png">

先关注第一个 bit。我们每秒可以把 1,000,000 个 bit 放到 link 上（bandwidth），所以把单个 bit 放到 link 上需要 1/1,000,000 = 0.000001 秒。在时间 0.000001 秒时，link 上已经有一个 bit，位于 sender 一端。

然后，这个 bit 需要 0.001 秒穿越 link（propagation delay），所以在时间 0.000001 + 0.001 秒时，最早的第一个 bit 到达 recipient。

<img width="900px" src="/assets/intro/1-59-timing2.png">

现在考虑最后一个 bit。和前面一样，把一个 bit 放到 link 上需要 0.000001 秒。我们有 800 个 bit 要发送，所以最后一个 bit 在时间 800 x 0.000001 = 0.0008 秒时被放到 link 上。

然后，最后一个 bit 需要 0.001 秒穿越 link，所以在时间 0.0008 + 0.001 秒时，最后一个 bit 到达 recipient。这就是我们可以说整个 packet 已经到达 recipient 的时刻。

<img width="900px" src="/assets/intro/1-60-timing3.png">

## Packet Delay（packet 延迟）

更一般地说，**packet delay（分组延迟）** 是发送整个 packet 所需的时间，从第一个 bit 被放到线上开始，到最后一个 bit 在另一端被接收为止。这个 delay 是 transmission delay（传输延迟）和 propagation delay（传播延迟）之和。

Transmission delay 表示把 bit 放到线上需要多长时间。在上面的例子中，它是 800 x (1 / 1,000,000)。一般来说，它等于 packet size（分组大小）除以 link bandwidth（链路带宽）。

由于 transmission delay 是 bandwidth 的函数，我们可以用 bandwidth 和 propagation delay 这两个 link property 来计算 packet delay。

## Bandwidth 和 Propagation Delay 的 Trade-off

考虑两条 link：

Link 1 的 bandwidth 是 10 Mbps，propagation delay 是 10 ms。

Link 2 的 bandwidth 是 1 Mbps，propagation delay 是 1 ms。

哪条 link 更好？这取决于你要发送的 packet。

假设我们想发送一个 10 byte 的 packet。对于两条 link，把一个 packet 放到线上所需的时间都可以忽略不计，此时 propagation delay 是 delay 的主要来源。Link 2 的 propagation delay 更短，所以它是更好的选择。

假设我们改为发送一个 10,000 byte 的 packet。现在，transmission delay 是 delay 的主要来源，因此我们更喜欢 Link 1，因为它能更快地把 byte 放到线上（更高 bandwidth）。你可以用正式的 packet delay 计算验证这个直觉：Link 1 发送这个 packet 大约需要 18 ms，而 Link 2 大约需要 81 ms。

作为现实例子，考虑一次 video call（视频通话）。如果视频质量很差，你很可能 bandwidth 不足（缩短 propagation delay 并不会有帮助）。相比之下，如果你说话和对方回答之间有明显延迟，问题很可能是 propagation delay 太长（增加 bandwidth 也不会有帮助）。

## Pipe Diagram（管道图）

到目前为止，我们一直使用 timing diagram 来表示 network event 发生的时间，例如 recipient 什么时候收到 packet。

观察 packet 在 network 中传输的另一种方式是：在某个冻结的时间点，画出 link 上的 bit。两种视角传达的是同一类信息，但在不同语境下，其中一种可能更有用。

为了画出 link，我们可以把 link 想象成一根管子（类似前面的水管类比），并把管子画成一个矩形：宽度是 propagation delay，高度是 bandwidth。管子的面积就是 link 的 capacity。

<img width="600px" src="/assets/intro/1-61-pipe1.png">

假设我们想跨越这条 link 发送一个 50 byte 的 packet。在 pipe view（管道视角）中，我们可以展示某个冻结时刻：packet 正在沿 link 传输。

Packet 被画成一个矩形，矩形的高度表示在单个 time step（时间步）中有多少 byte 被放到线上。在每个 time step，packet 会在管子中向右滑动。最终，packet 开始离开管子；每个 time step，矩形的一列会离开管子。

<img width="900px" src="/assets/intro/1-62-pipe2.png">

<img width="900px" src="/assets/intro/1-63-pipe3.png">

<img width="900px" src="/assets/intro/1-64-pipe4.png">

一个不那么直观的事实：timing diagram 中的 packet transmission delay 对应的是矩形的宽度。

为了理解原因，假设有一条 link 每秒能发送 5 bit，而我们有一个 20 bit 的 packet。在 timing diagram 中，从第一个 bit 被发送到最后一个 bit 被发送之间相隔 4 秒。

<img width="900px" src="/assets/intro/1-65-packet-delay-1.png">

在 pipe diagram 中，每秒会有一列 5 bit 进入管子。我们需要 4 列进入管子，这需要 4 秒。这意味着管子中 packet 的宽度是 4 列，也就是 4 秒。

<img width="900px" src="/assets/intro/1-66-packet-delay-2.png">

Pipe diagram 让我们能在同一条轴上观察 packet transmission time 和 propagation delay，并比较这两项。

Pipe diagram 可以用于比较不同 link。我们来看完全相同的 packet 穿过三条不同 link 的情况。

<img width="700px" src="/assets/intro/1-67-different-pipes.png">

如果缩短 propagation delay，管子的宽度会变短。管子的高度保持不变，每个矩形 packet 的形状也保持不变。（记住，你可以把 packet 的高度理解为每个 time step 进入管子的 bit 数，把 packet 的宽度理解为把所有 bit 送入管子所需的时间。）

这里还有其他观察：packet 宽度保持不变，说明 transmission delay 没有变化。此外，link 的面积变小了，这告诉我们 link 的 capacity 更低。

当我们增加 bandwidth 时，管子的高度会变高，表示单位时间内可以把更多 bit 送进管子。

注意，packet 的形状也改变了。Packet 现在更高，因为单位时间内可以把更多 bit 送进管子。结果是，我们能更快完成把 packet 送入管子的过程，因此 packet 的宽度（transmission delay）会减小。

## 过载的 Link

<img width="700px" src="/assets/intro/1-68-link1.png">

考虑这张图：packet 正在到达一个 switch。Switch 需要把所有 packet 沿 outgoing link（出方向链路）转发出去。在这个例子中没有问题，因为 switch 有足够 capacity，可以在每个 packet 到达时处理它。

<img width="700px" src="/assets/intro/1-69-link2.png">

那么这张图呢？

<img width="700px" src="/assets/intro/1-70-transient1.png">

从长期来看，我们有足够 capacity 发送所有 outgoing packet；但在这个具体瞬间，有两个 packet 同时到达，而我们只能发送一个。这称为 **transient overload（瞬时过载）**，在 Internet 的 switch 中极其常见。

为了应对 transient overload，switch 会维护一个 packet queue（分组队列）。如果两个 packet 同时到达，switch 会把其中一个放入 queue，并发送另一个。

<img width="700px" src="/assets/intro/1-71-transient2.png">

在任意时刻，switch 可以选择发送来自某条 incoming link（入方向链路）的 packet，也可以选择发送 queue 中的 packet。这个选择由 **packet scheduling（分组调度）** algorithm 决定，我们之后会看到许多不同设计。

<img width="900px" src="/assets/intro/1-72-transient3.png">

当没有 incoming packet 时，switch 可以 drain（清空）queue，并发送任何排队中的 packet。

<img width="900px" src="/assets/intro/1-73-transient4.png">

这使得 queue 能帮助我们吸收 transient burst（瞬时突发）。

<img width="700px" src="/assets/intro/1-74-transient5.png">

如果 incoming link 看起来像这样呢？

<img width="700px" src="/assets/intro/1-75-persistent.png">

现在我们遇到了 **persistent overload（持续过载）**。Outgoing link 根本没有足够 capacity 支持当前 incoming traffic（入方向流量）的水平。

我们可以把 queue 填满，但这仍然不足以支撑 incoming load。无论如何，switch 最终都会丢弃 packet。

如何处理 persistent overload？运营者需要正确规划自己的 link 和 switch。如果他们发现某个 switch 经常过载，可能会决定升级 link，而这可能需要人工操作。

过载的一种可能解决方案是让 router 告诉 sender 放慢速度。（之后学习 congestion control 时我们会研究这个问题。）不过归根到底，我们能做的并不多，这也是 Internet 被设计为只提供 best-effort service 的原因。

现在我们已经有了 queue 的概念，需要回头更新 packet delay 的公式。现在，packet delay 是 transmission delay、propagation delay 和 queuing delay（排队延迟）之和。
