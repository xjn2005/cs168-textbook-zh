---
title: Multicast
parent: Beyond Client-Server
nav_order: 1
layout: page-with-toc
---

# Multicast

## 动机：Multicast

在到目前为止见过的每个主题中，我们都说 Internet 的目标是在 host 之间传递数据。特别是，我们一直假设的是 unicast delivery，也就是有一个单一 source，把数据发送到一个单一 destination。

我们见过的许多 protocol（例如 HTTP、DNS、TCP、TLS）都依赖 client-server model，而这个模型又依赖 unicast delivery model。在 client-server model 中，一个 client 和一个 server 交换数据，这意味着它们在彼此之间发送 unicast data。

Internet 上的大多数 traffic 确实是 unicast，但也有一些例外。特别是，有些 application 涉及一组 host 之间的通信。例如，考虑多人游戏、实时内容分发 app（例如 Zoom 会议、体育比赛直播），或协作文档（例如 Google Docs）。Group communication 也有一些更特殊的用途，例如 discovery（例如向所有 Apple 设备发送消息，以便找到最近的 speaker），或 AI training（我们稍后会在这些 notes 中学习）。

Client-server 范式并不是思考这些场景的最自然方式。在多人游戏或视频会议 app 中，并不存在单一 client 或单一 server。Network 应该如何支持这些 application，让 developer 更容易编写这类 application？

这个问题的一种可能答案是：network 完全不提供支持。Group communication 可以用 unicast 实现。例如，当你更新协作文档时，可以向 group 中的每个其他人分别发送一个 unicast packet，让他们都知道你的更新。

<img width="500px" src="/assets/beyond-client-server/7-001-unicast-model.png">

不过，这种只使用 unicast 的方法可能很低效。考虑这个 network topology：你在 USA，而所有其他 group member 都在 Europe。如果你向每个 group member 分别发送 unicast packet，就会通过昂贵的海底光缆发送多份重复数据。另外，这也迫使 sender 发送许多重复的 unicast packet，扩展性很差（例如想象一台 server 向数百万用户直播体育比赛）。

直观上，更自然的方法是只通过海底光缆发送一个 packet，然后让 Europe 的某个实体（例如 router 或 host）把 packet 的副本分发给 group member。理想情况下，我们希望避免沿同一条 link 发送同一个 packet 的重复副本。换句话说，每条 link 应该只承载这个 packet 一次（如果这条 link 后面没有 group member，也可能是零次）。

<img width="500px" src="/assets/beyond-client-server/7-002-multicast-model.png">

这种方法需要 network 提供额外支持，也需要开发一些新 protocol。

## Multicast 定义

回忆一下，到目前为止我们已经见过四种 packet delivery model：

Unicast：把一个 packet 发送到恰好一个 destination。

Anycast：把一个 packet 发送到一组可能 destination 中的任意一个。集合中只需要一个成员收到 packet。

Broadcast：把一个 packet 发送到所有 destination。“所有”的定义取决于问题语境，但你可以把它理解为某个 local network 中的所有 host。

Multicast：把一个 packet 发送到某个 group 中的所有 member。Host 可以随时选择加入或离开 group。注意，即使你自己不是该 group 的 member，也可以向这个 group 发送 packet。

<img width="900px" src="/assets/beyond-client-server/7-003-uni-any-multi-broadcast.png">

Multicast 范式可以用来思考前面的 group communication 问题。例如，所有想接收体育比赛直播的 host 都可以加入一个 multicast group。然后，streaming service 可以向整个 group multicast packet。

再举一个例子，如果我们想用 multicast 做 discovery，可以让建筑中的所有 printer 加入一个 multicast group。然后，user 可以向整个 group multicast packet，找到自己可以使用的 printer。

## IP Multicast vs. Overlay Multicast

Multicast 历史中一个长期争论，是一个 architecture 问题：我们应该在哪一层实现 multicast？

一种选择是在 Layer 3 实现 multicast，有时称为 **IP multicast**。在这种方法中，我们给 router 添加专门支持，让它们理解如何 multicast packet。这个选项性能更好，但实现更难。

另一种选择是在 Layer 7 实现 multicast，有时称为 **overlay multicast**。在这种方法中，application 处理所有 multicast 功能。这种方法不改变 Layer 3，因此 router 只需要理解 unicast。这个选项性能较差，但实现更简单。

两种选项都不是绝对更好。我们会研究两种选项，并分析它们之间的 trade-off。

<img width="500px" src="/assets/beyond-client-server/7-004-multicast-taxonomy.png">
