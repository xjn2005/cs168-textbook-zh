---
title: Overlay Multicast
parent: Beyond Client-Server
nav_order: 6
layout: page-with-toc
---

# Overlay Multicast

## Overlay Multicast 简史

回忆一下，IP multicast 是在 1990 年代和 2000 年代开发的。在 2000 年代早期，IP multicast 部署进展缓慢，部分原因是我们前面讨论过的问题。因此，许多 startup 出现了，包括 FastForward Networks（Berkeley）、ProxyNet（Berkeley）、Sightpath（MIT）和 Akamai（MIT）。它们的工作大多彼此独立，但解决方案都使用了同一个基本思想：基于 overlay 的 multicast。

## Overlay Multicast：定义

回忆一下 IP multicast 的一个主要问题：跨不同 network 实现 multicast 很困难。在这张图中，如果所有 host 都是同一个 group 的 member，那么跨不同 network 的 router 很难协调，并把 packet 发送给整个 group。

<img width="900px" src="/assets/beyond-client-server/7-051-overlay-before.png">

这里的解决方案是构建一个直接把 host 彼此连接起来的 *virtual network topology*：

<img width="900px" src="/assets/beyond-client-server/7-052-overlay-after.png">

这里画出的 virtual link 是一种虚构，它们并不真正对应现实生活中的 physical link。例如，如果 A 想沿这条 virtual link 向 D 发送 packet，这个 packet 仍然必须穿过若干真实 router 和 link。

不过，通过画出这些 virtual link，我们现在可以假装所有 host 都在一个小型 local network 中彼此连接。这些 host 随后可以运行 multicast routing algorithm，在彼此之间 forward packet。

<img width="900px" src="/assets/beyond-client-server/7-053-overlay-tables-1.png">

例如，我们可以使用 virtual link 构建一棵以 D 为 root 的 core-based tree。然后，每个人都可以通过沿 tree 的 virtual link broadcast packet 来 multicast packet。

记住，当 packet 沿 virtual link 发送时，它仍然必须穿过若干真实 router 和 link。例如，如果 A 想把一个 packet forward 给 D 和 B，它必须发送两个 unicast packet：“From A, To D” 和 “From A, To B”。这两个 unicast packet 都会沿若干真实 router 和 link 传输，直到到达 destination。

在下面的例子中，A 正在向 G 发送一个 unicast packet。这个 packet 沿若干真实 router 和 link 传输到 G。途中，中间 host C 和 D 会接收并 forward 这个 packet。

<img width="900px" src="/assets/beyond-client-server/7-055-overlay-forward-1.png">

直观上，virtual network 给我们一种错觉：所有 host 都连接在一个小型 local network 中，尽管它们在现实中分散在世界各地。

从 network architecture 的角度看，end host（位于 Layer 7）现在负责运行 multicast protocol。End host 现在扮演 **virtual router** 的角色。这意味着 end host 必须构建 multicast forwarding table，知道自己的 outgoing virtual link（例如在 static table entry 中），并沿 virtual link forward packet。Router 完全不需要思考 multicasting（它们只需要运行标准 unicast protocol）。

这不同于 IP multicasting。在 IP multicasting 中，router 负责运行 multicast protocol，而 end host 不需要思考这些 protocol（它们只需要向 group address 发送 packet）。

我们画出的 virtual link 形成 **overlay network**。Overlay network 中的 end host（virtual router）彼此交谈，以运行 multicast routing algorithm。Overlay routing table 基于 virtual link（例如 B 的 table 可能会说，如果我从 A 收到 packet，就 forward 给 C 和 D）。

负责沿 virtual link 发送 packet 的真实 link 和 router 形成 **underlay network**。Underlay network router 彼此交谈，以运行标准 unicast routing algorithm（例如 distance-vector、BGP）。Underlay routing table 基于 physical link（例如 R1 的 table 可能会说，到 G 的 next-hop 是 R2）。

<img width="900px" src="/assets/beyond-client-server/7-054-overlay-tables-2.png">

为了实现 overlay 和 underlay network，我们会使用 encapsulation。假设我们想向 group address multicast 一个 packet。那么 inner header（overlay）会说 “From A, To G1”，host 会读取这个 overlay packet 来决定如何 forward packet。

假设 Host A 决定这个 packet 需要沿 virtual link C forward。那么 Host A 会用 outer header “From A, To C” encapsulate 这个 packet，并把这个 packet unicast 给 C。Underlay 只使用 outer header，负责把 unicast packet 从 A forward 到 C。

<img width="900px" src="/assets/beyond-client-server/7-056-overlay-forward-2.png">

<img width="900px" src="/assets/beyond-client-server/7-057-overlay-forward-3.png">

<img width="900px" src="/assets/beyond-client-server/7-058-overlay-forward-4.png">

## 实现 Overlay Network

在最基本的模型中，overlay network 中的 node 是 end host（例如你的个人 laptop）。这意味着 end host 需要理解 multicast routing protocol，构建自己的 forwarding table，并 forward packet。

End host 也可以是某家公司安装的 proxy server（类似 CDN server）。这些机器仍然是运行 multicast routing protocol 的 end host，但它们不是实际 user machine（例如你的个人 laptop），而是专门部署来帮助支持 multicast routing。注意，这些 proxy server 仍然是在 overlay 中运行 multicast routing 的 end host。它们仍然需要 encapsulate packet，并通过 underlay network unicast 这些 packet，因此这些 server 不是 Layer 3 router。

Overlay network 的一般思想也可以用于 multicast 之外的其他目的。例如，packet 也可以跨 overlay network unicast。你可以使用 overlay topology 构建 peer-to-peer file sharing service。（Peer-to-peer service 指的是 group 中任意 user 都可以和任意其他 user 共享 file，而不依赖存储所有 file 的 central server。）

许多 overlay network 可以同时共存在同一个 underlay network 之上。从 end host 的角度看，end host 会运行两个不同 application。每个 application 都有自己单独的 forwarding table、neighboring link list 等。每个 application 可以提供不同 service。

## Overlay Multicast 的好处

Overlay multicast 方法有什么好处？

最大好处是部署容易。从 underlay router 的视角看，overlay network 只是另一个发送和接收 unicast packet 的 application。Underlay router 和 protocol 不需要任何修改。

IP multicast 要求大多数或所有 router 理解 multicast protocol。相比之下，在 overlay multicast 中，只有某些参与 node（例如 group 中的 user）需要理解 protocol。所有其他 end host 都不需要任何修改。

每个 overlay multicast application 可以使用自己的 implementation 或 protocol，因此不同 application（例如不同 group）之间不需要标准化。对比 IP multicast：所有 router 都需要说同一种 protocol，才能彼此协调。

因为每个 overlay multicast application 可以做出自己的 implementation decision，这种方法也给 application 自由，让它们定义自己的目标。

每个 application 可以决定如何绘制 virtual topology，如何设置 link cost，以及如何计算穿过 network 的 path。有些 group 可能更关心 latency，而其他 group 可能更关心 throughput。

Overlay multicast 中的 access control 也更容易（相比 IP multicast）。Routing protocol implementation 可以被定制为只允许 authorized user 参与 protocol。每个 application 都可以自行决定什么算是 authorize 一个 user。

每个 application 也可以决定自己的商业模式。Routing protocol implementation 可以被定制为跟踪 usage 并相应向 user 收费，每个 application 都可以自行决定什么算是 track usage。例如，一个由 CDN server 组成的 overlay network 可能用于向数百万 user 直播体育比赛。Application 本身可以跟踪哪些 user 正在观看体育比赛，并相应收费。

也存在更不寻常的商业模式。例如，peer-to-peer file sharing system 可能被用来非法流式传输受版权保护的材料。这个 system 可能希望避免跟踪 user，以免给 user 惹麻烦。

## Overlay Multicast 性能

Overlay network 的性能高度依赖于你在 end host 之间画出的 virtual topology。特别是，virtual topology 中的 link 和 cost 应该准确反映对应的 underlay topology。

例如，这个 overlay network topology 与对应的 underlay topology 非常接近。

<img width="900px" src="/assets/beyond-client-server/7-059-underlay-1.png">

从 A 到 C 的 virtual link 可以分配较低 cost，因为现实中 A 和 C 距离较近（underlay path 穿过 3 个 router）。从 D 到 G 的 virtual link 可以分配较高 cost，因为现实中 D 和 G 距离更远（underlay path 穿过 5 个 router）。如果我们在 overlay topology 中计算 shortest path，得到的 path 应该和 underlay topology 中的 shortest path 很相似。让 packet 在 underlay 中走短 path 是理想的，因为 packet 最终仍然要通过 underlay network forward。

在这个特定 overlay topology 中，从 A 到 G 的 packet 最终会沿一条非常接近 shortest path 的路径 forward。

下面是一个 overlay network 糟糕建模对应 underlay topology 的例子。

<img width="900px" src="/assets/beyond-client-server/7-060-underlay-2.png">

注意，我们没有改变 underlay topology 的任何东西。我们只改变了 virtual link 的放置方式。

在这个特定 overlay topology 中，如果尝试计算从 A 到 G 的 shortest path，会得到 A 到 C 到 B 到 E 到 F 到 G 这条 path。如果随后沿这条 path 发送 packet，从 A 到 G 的 packet 最终会在 underlay network 中沿一条糟糕得多的 path forward。

为了衡量 overlay network 的性能，我们可以定义 **stretch factor**。它是 underlay path cost 与 overlay path cost 的比值。

<img width="700px" src="/assets/beyond-client-server/7-061-stretch.png">

在上面的例子中，underlay cost 是 4，overlay cost 是 1，因此 stretch factor 是 4。为了更好地建模 underlay network，把这条 virtual link 的 cost 设为 4 可能更合理。

高 stretch value 是不好的，因为它意味着 underlay path 比对应 overlay path 长很多倍。理想情况下，我们希望 stretch value 更低（更接近 1），这意味着 underlay path cost 大致等于 overlay path cost。

我们如何构建 low-stretch overlay topology？有时，operator 会手动设计 topology。

也存在 self-organizing protocol，用于自动发现好的 overlay topology。从高层看，一个 self-organizing protocol 可能这样工作：一开始，随机选择你的 neighbor（也就是从你到随机 neighbor 画 virtual link）。周期性地，你搜索新的 candidate neighbor，并测量你到这些新 candidate neighbor 的距离（例如发送 packet 并测量 round-trip time）。如果最佳 candidate neighbor 优于当前最差 neighbor，就放弃当前最差 neighbor（删除 virtual link），并添加最佳 candidate neighbor（添加新的 virtual link）。

## Overlay Multicast 的缺点

Overlay multicast 会引入额外 overhead，从而影响性能。例如，encapsulate 和 decapsulate packet 需要额外时间和处理能力。

Overlay multicast 并没有内建进 Internet，这意味着 application developer 必须自己实现 overlay multicast。对比 IP multicast，application developer 只需要向 group address 发送 packet，而不必构建自己的 forwarding table 等。

尽管有这些缺点，overlay multicast 的性能已经足够好，因此今天在 Internet 中被广泛部署。
