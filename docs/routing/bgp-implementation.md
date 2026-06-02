---
title: BGP Implementation and Issues
parent: Routing
nav_order: 10
layout: page-with-toc
---

# BGP Implementation and Issues

## Border Router 和 Interior Router

到目前为止，我们已经对 BGP 如何在 AS 之间工作有了直观图景。本节会展示 BGP 在 router 层面实际如何实现。这样做时，我们也会看到 BGP 如何与前面讲过的 intra-domain routing protocol 交互。

到目前为止，我们的 inter-domain routing 模型把整个 AS 当成一个单独实体，用它来 import 和 export path。

<img width="900px" src="/assets/routing/2-165-combining1.png">

然而，现实中 AS 内部包含许多由 link 连接的 router（和 host）。

<img width="900px" src="/assets/routing/2-166-combining2.png">

为了真正实现 BGP，我们需要 AS 内部的所有 router 协同工作，让整个 AS 表现得像一个节点。

在一个 AS 内部，我们会把 router 分成两类。**border router** 至少有一条 link 连接到不同 AS 中的 router。**interior router** 只连接到同一个 AS 内部的其他 router。

<img width="900px" src="/assets/routing/2-167-borders.png">

只有 border router 需要向其他 AS advertise route。有时，我们把 advertise BGP route 的 router 称为 **BGP speaker**。BGP speaker 需要理解 BGP protocol 的语义和语法（怎样读取和创建 BGP announcement，收到 announcement 后该做什么，等等）。


## External BGP 和 Internal BGP Session

**BGP session** 由两个 router 彼此交换信息组成。

<img width="900px" src="/assets/routing/2-168-bgp1.png">

**external BGP (eBGP) session** 发生在来自不同 AS 的两个 router 之间。eBGP session 可以用来在不同 AS 之间交换 announcement，并学习通往其他 AS 的 route。只有 border router 会参与 eBGP session（因为 eBGP 需要和另一个 AS 通信）。

<img width="900px" src="/assets/routing/2-169-bgp2.png">

相比之下，**internal BGP (iBGP) session** 发生在同一个 AS 内的两个 router 之间（它们不一定由一条 link 直接连接）。更具体地说，如果某个 border router 学到一条新 route，它可以用 iBGP 把这条新 route 分发给 AS 内的其他 router。这让 AS 内所有 router 能协调起来，作为一个实体一起行动。border router 和 internal router 都会参与 iBGP session。

<img width="900px" src="/assets/routing/2-170-bgp3.png">

eBGP 和 iBGP session 不同于 **interior gateway protocols (IGP)**。IGP 是部署在 AS 内部、用于在 AS 内 routing packet 的 intra-domain routing protocol（例如 distance-vector、link-state）。

<img width="900px" src="/assets/routing/2-171-bgp4.png">

iBGP 和 IGP 很容易混淆。两者都在同一个 AS 内交换消息。不过，iBGP 是 inter-domain protocol 的一部分，帮助 router 学习通往其他 AS 的 path。IGP 是 intra-domain protocol，帮助 router 学习通往同一 AS 内 destination 的 path。

<img width="900px" src="/assets/routing/2-172-bgp5.png">

eBGP、iBGP 和 IGP 共同工作，建立从 Internet 中任意一个 router 到任意另一个 router 的 route（即使这些 router 属于不同 AS）。

首先，每个 AS 运行 IGP，以学习同一个 AS 内任意两个 router 之间的 least-cost path。

<img width="900px" src="/assets/routing/2-173-bgp6.png">

接着，AS 运行 eBGP，彼此 advertise route，以学习通往其他 AS 的 route。

<img width="900px" src="/assets/routing/2-174-bgp7.png">

最后，AS 运行 iBGP，使得已经学到外部 route 的 router 可以把这条 route 分发给同一个 AS 内的所有其他 router。

<img width="900px" src="/assets/routing/2-175-bgp8.png">

从 eBGP、iBGP 和 IGP 学到的 route 可以用来把 packet 发送到 Internet 中任何地方。如果 destination 位于同一个 AS 中（相同 IP prefix），我们可以使用 IGP 学到的 route 来转发 packet。如果 destination 位于不同 AS 中（不同 IP prefix），我们可以回想 iBGP，它告诉我们本 AS 中任何 router 发现的外部 route。使用 iBGP 结果，我们可以找出哪一个 border router 位于那条外部 route 上。然后，我们可以使用 IGP 把 packet 转发到正确的 border router（它随后会把 packet 转发到下一个 AS）。

<img width="900px" src="/assets/routing/2-176-bgp9.png">

举个具体例子，假设 E 想向 Z 发送 packet。首先，E 所在 AS 中每个 router 运行 IGP，学习所有内部 route。接下来，AS#5 中某个 router 使用 eBGP advertise 一条通往 Z 的 route。此时，只有 G 知道自己可以到达 Z。最后，G 使用 iBGP 告诉自己 AS 中的所有 router：它可以到达 Z。

E 通过 iBGP 听说，同一个 AS 中的 G 可以到达 Z。使用 IGP route，E 可以把 packet 发给 G（先转发给 F）。然后，G 可以使用从 eBGP 学到的 route，把 packet 发往 Z。

advertise 通往外部 destination 的 route 的 border router，有时称为该 destination 的 **egress router**。这个 router 可以帮助你的 packet 离开本地网络，移动到更接近 destination 的其他网络。在上面的例子中，G 就是 destination Z 的 egress router。

这些 protocol 的一个结果是，每个 router 都有两张 forwarding table。一张表把所有内部 destination（同一个 AS）映射到 next hop，由 IGP 信息填充。另一张表把所有外部 destination 映射到 egress router（它知道通往外部 destination 的 route），由 eBGP 信息填充。

<img width="900px" src="/assets/routing/2-177-bgp10.png">

注意，在 eBGP table 中，egress router 不一定是 next hop。egress router 可能离本地有好几个 hop，但我们会使用 IGP 到达这个 egress router。

<img width="900px" src="/assets/routing/2-178-bgp11.png">

我们已经见过 eBGP（path-vector，advertising route）和 IGP（distance-vector 或 link-state）如何作为 algorithm 实现。iBGP 又是怎样实现的？当一个 border router 安装通往某个 destination 的新 route 时，它必须通知 AS 中其他 router。一个简单方案是让 border router 直接告诉 AS 中每个其他 router。

<img width="900px" src="/assets/routing/2-179-bgp12.png">

这个方案相对简单，不过它要求每个 border router 都与每个其他 router 建立 iBGP session。在一个有 B 个 border router、总共 N 个 router 的网络中，这个 protocol 需要 BN 个 iBGP connection，并且可能随着本地网络变大而难以扩展。

注意：现实中，还有其他方法可以结合 inter-domain 和 intra-domain router。如果你感兴趣，可以查一下 “route reflectors”，不过这门课不会覆盖它们。


## AS 之间的多条 Link：Hot Potato Routing

到目前为止，在 AS graph 中，如果两个 AS 连接，我们只画一条 link（edge）。实践中，由于 AS 实际上由许多 router 组成，两个 AS 之间可能由多条 link 连接。

实践中，大型 AS 之间拥有多条 link 可能很有用。例如，Verizon 和 AT&T 都是非常大的 AS，在整个美国都有基础设施。假设这两个 AS 之间只有一条位于西海岸的 link。如果东海岸的 Verizon router 想和东海岸的 AT&T router 通信，packet 就必须先在 Verizon 网络中横跨整个国家，穿过 link 进入 AT&T 网络，然后再横跨整个国家回到 destination。

<img width="800px" src="/assets/routing/2-180-multilink1.png">

两个 AS 之间有多条 link，也意味着两个 router 之间可能存在多条经过相同 AS 的 path。在 AS 层面，这些 path 都经过同样的 AS，而我们之前的模型没有区分它们。不过，在更细的模型中，两条 path 都需要被 export，并且必须 import 一条偏好的 route。

<img width="800px" src="/assets/routing/2-181-multilink2.png">

如果有两条 route，importing AS 偏好哪一条？

<img width="800px" src="/assets/routing/2-182-multilink3.png">

带宽要花钱，所以我希望这段 traffic 尽可能多地走别人拥有并付费维护的基础设施，尽可能少地走我自己的基础设施。因此，橙色 path 更受偏好。

更正式地说，importing AS 会收到两个 announcement：一个来自西边 router，一个来自东边 router。

<img width="800px" src="/assets/routing/2-183-multilink4.png">

通过 iBGP，AS 内部每个 router 都能看到两个 announcement。一个说 egress router 是西边 router，另一个说 egress router 是东边 router。每个 router 都必须决定 import 哪一个 announcement。

<img width="800px" src="/assets/routing/2-184-multilink5.png">

我们聚焦 router E。使用 IGP，这个 router 可以算出到西边 egress router（F）的距离，以及到东边 egress router（I）的距离。由于西边 egress router（F）更近，经由西边 egress router（F）routing packet 会消耗本 AS 更少的带宽。因此，这个 router 会 import 经过西边 egress router（F）的 path。另一个 router，比如更靠近东边 egress router（I）的 router，可能会决定 import 另一条 path。

<img width="800px" src="/assets/routing/2-185-multilink6.png">

这种选择最近 egress router 的策略有时称为 **hot potato routing**。我们希望 packet 尽快离开自己的 AS，并尽快开始在别人的 link 上传输。


## Router 之间的多条 Link：MED

如果一个 router 距离两个可能的 egress router 一样近，会怎样？

<img width="800px" src="/assets/routing/2-186-med1.png">

为了打破平局，exporting AS 可以宣布它对某条 route 的偏好。

exporting AS 偏好哪条 route？同样，因为带宽要花钱，exporting AS 偏好粉色 path，因为它使用的本 AS 带宽更少。在粉色 path 的 announcement 中，exporting AS 可以额外说「我希望你使用这条 path」；在橙色 path 的 announcement 中，exporting AS 可以额外说「我希望你避免这条 path」。

<img width="900px" src="/assets/routing/2-187-med2.png">

现在，距离两个 egress router 一样近的 router 可以在 iBGP announcement 中看到这些额外信息。

<img width="900px" src="/assets/routing/2-188-med3.png">

使用这些额外信息，router 可以选择粉色 path 上的 egress router，因为 exporting AS 偏好这条 path。

<img width="800px" src="/assets/routing/2-189-med4.png">

exporting announcement 中的这项额外信息称为 **Multi-Exit Discriminator (MED)**。从 exporter 角度看，它表示我希望别人从哪个 router 进入我的网络。从 importer 角度看，它表示另一个 AS 希望你从哪个 router 离开自己的网络并进入对方网络。

另一种解释 MED 的方式是：经由这个 router 到 destination 的距离。exporter 可以说，「西海岸 router 距离 destination 有 3 个 hop」，以及「东海岸 router 距离 destination 有 12 个 hop」。较低的 MED 数值更受偏好，因为 exporter 希望尽可能少使用自己的带宽。exporter 宁愿使用自己的 3 条 link，而不是 12 条 link。


## Import Policy 的优先级

更细的模型允许两个 AS 之间由多条 link 连接，这意味着除了 Gao-Rexford rules 之外，现在还会有额外的 import policy rule。当你收到多个针对同一 destination 的 announcement 时，按下面顺序使用这些 tiebreaking rule 来选择 path：

1. 使用 **Gao-Rexford rules**。优先选择由 customer advertise 的 path，其次是 peer，再其次是 provider。
2. 如果多条 path 有相同的 Gao-Rexford priority（例如两条 path 都来自 customer），选择**更短的 path**（经过更少 AS 的 path）。
3. 如果多条 path 长度相同，选择有**更近 egress router** 的 path（使用 IGP 找出到每个 egress router 的距离）。
4. 如果多条 path 到 egress router 的距离相同，选择 **MED 更低**的 path（MED 包含在 advertisement 中）。
5. 如果多条 path 的 MED 相同，**任意打破平局**（例如选择 IP 地址更低的 router）。

<img width="900px" src="/assets/routing/2-190-med5.png">

注意，closest egress router（hot potato routing）和 MED 经常互相矛盾。每个 AS 都偏好最小化自己的带宽使用，并希望 packet 使用其他 AS 的带宽来承载。

作为 exporting AS，我希望 packet 尽可能靠近 destination 时才进入我的 AS。这意味着我希望 importing AS 把 packet 承载很远（到 egress 的路径很长）。

<img width="900px" src="/assets/routing/2-191-med6.png">

相比之下，作为 importing AS，我希望尽可能少承载 packet（到 egress 的路径很短）。这意味着我希望 packet 在离 destination 尽可能远的位置进入另一个 AS（迫使另一个 AS 做所有工作）。

<img width="900px" src="/assets/routing/2-192-med7.png">

这种矛盾的一个结果是，Internet 中的 path 经常是非对称的。如果两个 host 来回发送 packet，一个方向的 path 可能不同于另一个方向的 path。

<img width="800px" src="/assets/routing/2-193-med8.png">

在这个例子中，对于向东发送的 packet，A 选择西边 egress router，并迫使 B 承载大部分 traffic。在另一个方向（向西）上，B 选择东边 egress router，并迫使 A 承载大部分 traffic。

从根本上说，BGP 允许这种行为，因为每个 AS 都拥有设置自己 policy 的 autonomy（这里的 policy 就是 hot potato routing）。

实践中，有些 AS 会尝试实现更聪明的策略，诱使其他 AS 把 packet 承载得更远。或者，如果你支付额外费用，带宽更充足的 AS 也可能同意为你把 traffic 承载得更远。


## BGP Message 类型和 Route Attribute

回忆一下，一个 protocol 必须指定 syntax 和 semantics。具体来说，BGP 必须指定发送和接收的 message 结构。BGP 也必须指定 router 收到 message 后应该做什么。

BGP 有四种不同的 message type。Open message 可以用来在两个 router 之间启动 session，使它们互相通信。KeepAlive message 可以用来确认 session 仍然打开，即使最近没有发送 message。Notification message 可以用来处理错误。我们不会进一步描述前三种 message type。

我们会关注第四种，也是最有意思的 message type：Update。这些 message 用来 announce 新 route、修改现有 route，或者删除不再 active 的 route。

Update message 包含一个 destination，用 IP prefix 表示。message 还包含 **route attribute**，可用于编码与这个 IP prefix 对应的任何有用信息。route attribute 是一组 name-value pair，其中 name 表示 attribute 类型，value 表示这个 attribute 的值。一个非网络例子是：color=red、shape=triangle。attribute name 是 color 和 shape，它们分别对应 red 和 triangle 这些 value。

有些 attribute 是 AS 本地的，只在 iBGP message 中交换。其他 attribute 是全局的，可以在 eBGP advertisement 中发送。

BGP attribute 有很多，但我们会关注三个重要 attribute，它们用来编码 importing path 时的不同 tiebreaker。

**LOCAL PREFERENCE** attribute 在某个具体 AS 内编码 Gao-Rexford import rule（最高优先级 tiebreaker）。AS 可以给更偏好的 route（例如来自 customer 的 route）分配更高的值，给不太偏好的 route（例如来自 provider 的 route）分配更低的值。这个 attribute 是本地的，只会携带在 iBGP message 中。它不会在 eBGP announcement 中发送给其他 AS，因为其他 AS 不需要知道这个 AS 的偏好。

<img width="900px" src="/assets/routing/2-194-attribute1.png">

举个例子，假设 router E 从 AS#7 收到一个 eBGP announcement，而 router A 知道 AS#7 是 customer。那么，在 iBGP message 中，router E 可以设置 local preference value 为 3000（较高数字）。现在，同一个 AS 中的其他所有 router 都知道：router E 可以通过 `ASPATH` attribute 中的 path 到达它正在 announce 的 destination，并且 local preference 是 3000。

相比之下，如果 router D 从 AS#79 收到一个 eBGP announcement，而这个 AS 是 peer，那么在 iBGP message 中，router D 可以设置较低的 local preference value 1000，然后把这条 path（带有较低 local preference）分发给 AS 中的其他 router。

local preference 数值是任意的，只有相对排序重要。在上面的例子中，数字也可以是 300 和 100，而不是 3000 和 1000，行为仍然相同。local preference 数字通常由运营者手动设置。

**ASPATH** attribute 包含被 advertise 的 route 沿途经过的 AS 列表（反向顺序）。这个 attribute 是全局的，可以在 eBGP announcement 中发送。

<img width="800px" src="/assets/routing/2-195-attribute2.png">

例如，一个 announcement 会包含 destination 的 IP prefix（128.112.0.0/16），以及 ASPATH attribute [3, 72, 25]。

`ASPATH` 是 importing path 时第二优先级的 tiebreaker。如果两个 announcement 有相同 local preference（例如都来自 customer），我们会选择更短的 path。`ASPATH` 告诉我们每条 path 的长度，长度由 path 经过的 AS 数量衡量。

如果 local preference 和 path length 都打平，第三优先级 tiebreaker 是到 egress router 的 IGP cost。这个 cost 存储在 router 的本地 forwarding table 中（例如，本地 distance-vector protocol 会存储到同一个 AS 中每个其他 router 的 cost）。

**MED** attribute 编码 exporting AS 的偏好。等价地说，这个 attribute 表示从 exporting router 到 destination 的距离（较低数字更受偏好）。

<img width="900px" src="/assets/routing/2-196-attribute3.png">

例如，如果这两个 AS 之间有两条 link，exporting AS 的两个 border router 都会 announce 一条 path。两种情况下 `ASPATH` 和 destination 相同，因为到 destination 的 AS path 是相同的。不过，西边 router 会包含一个比东边 router 更低的 `MED` attribute number。这表示：如果可能，请把发往该 destination 的 packet 通过我的西边 router routing（较低数字），因为这个 router 更接近 destination。

如果 local preference、path length 和到 egress router 的距离都打平，第四优先级 tiebreaker 是每个 announcement 中的 MED 数值。


## BGP 的问题

BGP 没有内建的安全保证。恶意 AS 可以撒谎，advertise 一条通往某个 destination 的 route，即使它实际上无法到达这个 destination。恶意 AS 也可以 advertise 一条通往 destination 的非常便宜的 route，即使这条便宜 route 并不存在。这可能诱导其他 AS 把 packet 通过恶意 AS routing，而攻击者就能删除或修改经过恶意 AS 的 packet。这些攻击称为 **prefix hijacking**。关于使用密码学来保护 BGP 的研究很活跃，不过这些 protocol 还没有被广泛部署。

BGP 在选择 path 时优先考虑 policy，而不是 least cost。此外，因为 BGP 用 AS 数量来衡量 path length，path length 可能会误导我们（例如，被 advertise 的 path 中，一个 AS 内可能包含 2 个 router，也可能包含 200 个 router）。这可能导致 packet 并不总是走 least-cost path，也让 Internet 性能难以推理。有些人可能把这些归类为问题，不过它们也可能更像是一种有意的设计 trade-off。BGP 的设计者做了一个明确选择：优先考虑 policy，并隐藏 AS 的内部拓扑，代价是牺牲一些性能。

BGP 实现起来很复杂。这里有许多我们没有覆盖的微妙实现细节。即使在我们覆盖的主题中，local preference 或 MED number 等配置也必须由运营者手动设置，而错误配置可能导致错误 path 在网络中传播。BGP misconfiguration 经常导致 Internet outage，也有很多研究在开发工具来验证 BGP 是否正确配置。

BGP 需要一些假设（所有人都遵循 Gao-Rexford rules，AS graph 形成层级结构，没有 provider-customer cycle）才能保证 reachability 和 convergence。如果这些假设不成立（例如某个 AS 选择了违反 Gao-Rexford 的自定义 policy），BGP 可能产生不稳定行为：route 永不收敛，或者出现 cycle 和 dead-end。
