---
title: Introduction to Routing
parent: Routing
nav_order: 1
layout: page-with-toc
---

# Routing 简介

## 什么是 Routing？

假设机器 A 和机器 B 都连接到了 Internet。机器 A 想向机器 B 发送一条消息，但这两台机器并没有直接相连。机器 A 怎么知道应该把消息发到哪里，才能让消息最终到达机器 B？这条消息会沿着网络中的哪条路径到达目的地机器 B？在本单元中，我们会学习 **routing（路由）** 来回答这些问题。

<img width="600px" src="/assets/routing/2-001-intro-pic.png">

首先，我们会建立一个 Internet 模型，让 routing 可以被表述为一个定义清楚的问题。我们还会看到 routing 问题的答案长什么样，以及什么样的答案是有效且较好的。

接着，我们会考察几类不同的 routing protocol（路由协议），它们可以用来帮助生成 routing 问题的答案。我们还会看到 addressing protocol（寻址协议）如何让 routing protocol 扩展到整个 Internet。

最后，我们会简要了解现实中用来实现这些 routing protocol 的硬件。

## Inter-Domain Routing 和 Intra-Domain Routing

一种可能的 routing 策略，是建立一个包含全世界每一台机器的 Internet 模型，然后设计一个单一而庞大的 routing protocol，让我们可以把 packet 发送到世界上任何地方。然而，由于 Internet 的规模，这在实践中并不可行。

相反，我们会利用这样一个事实：Internet 是网络的网络。换句话说，Internet 由许多 local network（局部网络）组成。每个 local network 实现自己的 routing protocol，规定如何只在这个 local network 内部发送 packet。然后，我们可以把所有这些 local network 连接起来，并在所有 local network 之间实现一个 routing protocol，规定如何在不同 local network 之间发送 packet。

<img width="900px" src="/assets/routing/2-002-network-of-networks.png">

Local network 并不完全相同。例如，它们的规模可能不同：有些 network 可能包含更多机器。机器也可能分布在更大的物理范围内（例如整个 UC Berkeley 校园），或较小的范围内（例如你的家）。Network 还可能在需要支持的 bandwidth（带宽）、允许的故障率、可用支持人员数量、基础设施年龄、建设和维护所需资金等方面不同。

由于每个 network 都有自己的结构和需求，不同的 local network 可能会选择使用不同的 routing protocol。某种 packet routing 策略可能在一个 network 上有效，但在另一个 network 上并不适用。

在网络的网络模型下，我们可以让每个 local network 自行选择其内部 packet 的 routing 策略。每个运营者都可以选择最适合自己的 protocol。用于在 local network 内部 routing packet 的 protocol 称为 **intra-domain（域内）** routing protocol，或 **interior gateway protocol（IGP，内部网关协议）**。现实中的例子包括 OSPF（Open Shortest Path First）和 IS-IS（Intermediate System to Intermediate System）。

<img width="900px" src="/assets/routing/2-003-intradomain.png">

相比之下，用于在不同 network 之间 routing packet 的 protocol 称为 **inter-domain（域间）** routing protocol，或 **exterior gateway protocol（EGP，外部网关协议）**。为了支持 packet 跨越不同 local network 发送，每个 network 都需要同意使用同一种 protocol 来在彼此之间 routing packet。如果不同 network 使用不同的 inter-domain protocol，就无法保证整个 Internet 能以一致的方式连接起来。假如某个运营者只实现了 Protocol X，而另一个运营者只实现了 Protocol Y，会怎样？这两个 local network 如何交换消息并不清楚。

由于每个 network 都必须同意使用同一种 inter-domain protocol，因此在 Internet 上大规模部署的这类 protocol 只有一种，也就是 BGP（Border Gateway Protocol）。

<img width="900px" src="/assets/routing/2-004-interdomain.png">

Interior gateway protocol 和 exterior gateway protocol 这个模型有助于建立直觉，但在实践中，两者之间并不总是有清晰界限。例如，除了用于不同 network 之间，BGP 有时也会在 local network 内部使用。

无论一个 protocol 是部署在 network 内部，还是部署在所有 network 之间，我们还可以根据底层 algorithm（算法）的工作方式来对 routing protocol 分类。具体来说，我们会学习 distance-vector protocol（距离向量协议）、link-state protocol（链路状态协议）和 path-vector protocol（路径向量协议，稍后会更详细介绍每一类）。
