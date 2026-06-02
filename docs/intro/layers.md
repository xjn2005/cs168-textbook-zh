---
title: Layers of the Internet
parent: Introduction
nav_order: 2
layout: page-with-toc
---

# Internet 的分层

## Layer 1：物理层

在这一部分中，我们将自底向上地构建 Internet，从最基础的构件开始，并逐步组合形成整个 Internet 基础设施。我们会持续使用邮政系统作为类比，因为它与 Internet 在设计上有许多相似之处。

首先，我们需要一种能够跨越空间传递信号的方法。在邮政系统中，这可能是邮递员、Pony Express、卡车、信鸽等。

而在 Internet 中，我们需要的是一种能够跨空间传输 bit（0 和 1）的方法。其实现技术可能包括：电线上的电压变化、无线电波、光纤中的光脉冲等等。整个电子工程领域中有大量研究都围绕「如何跨空间传输信号」展开，不过本课程不会深入讨论这些细节。

## Layer 2：链路层

在类比中，现在我们已经拥有了一种跨空间发送数据的方法，因此可以利用这个基础构件连接两户人家。甚至还可以尝试连接整个城镇中的所有家庭。

在 Internet 中，**link（链路）** 用于连接两台机器。链路可以采用任意技术实现，例如有线、无线、光纤等。若使用链路将一批彼此相近的计算机连接起来（例如 UC Berkeley 校园中的所有计算机），便形成了一个 **local area network（LAN，局域网）**。

<img width="175px" src="/assets/intro/1-01-lan.png">

在 Layer 2 中，我们还可以将 bit 组织成数据单元，称为 **packet（数据包）**（在这一层有时也称为 frame）。同时，我们需要定义 packet 在物理信号中的起始与结束位置。此外，还要解决诸如「多人同时共享同一根线发送数据」之类的问题。

## Layer 3：网络层

现在，我们已经能够在局部区域内连接所有人，但如果不同区域中的两个人想要通信，又该怎么办？一种可能的方法是在不同 local network 之间增加大量链路，但这显然效率不高。（如果两个 local network 分别位于不同大陆呢？）

<img width="400px" src="/assets/intro/1-02-mesh.png">

更聪明的方法是：在每个 network 中引入一个「邮局」，然后只需要将两个邮局连接起来即可。这样，当 network A 中的人想与 network B 中的人通信时，他只需将邮件发送到 A 中的邮局。该邮局会把邮件转发到 B 中的邮局，再由后者投递到最终目的地。

<img width="400px" src="/assets/intro/1-03-router.png">

在 Internet 中，这种负责接收并转发邮件的「邮局」被称为 **switch（交换机）** 或 **router（路由器）**。

如果我们在不同 switch 之间继续建立链路，就可以把 local network 连接起来。当 local network 和链路足够多时，就能把全世界连接起来，从而形成 Internet。

<img width="700px" src="/assets/intro/1-04-network-of-networks.png">

其中一个关键问题是：如何在 network 中寻找路径？当一个 switch 收到 packet 时，它如何知道应当把 packet 转发到哪里，才能让 packet 更接近最终目的地？这将成为 routing（路由）部分的核心问题。

我们还必须确保链路具有足够容量（capacity）来承载数据。这将成为 congestion control（拥塞控制）部分的核心问题。

目前这张图展示的是 Internet 的基础设施，但在本课程中，我们还会研究负责管理这些基础设施的运营者。在类比中，他们相当于建设和运营邮局的人。在 Internet 中，这些运营者是 ISP，例如 AT&T、Amazon Web Services，甚至 UC Berkeley 本身，它们负责拥有并运营 Internet 基础设施。除了硬件与软件基础设施之外，我们还需要将这些实体视作现实中的企业与组织，并考虑它们的经济与政治激励。例如，如果 AT&T 建设了一条海底光缆，它可能会向其他 ISP 收取数据传输费用。

## 网络的网络

Internet 常被描述为一个**网络的网络**。世界上存在大量小型 local network，而 local network 内部的事务可以由本地独立管理（例如由 UC Berkeley 自行管理）。随后，所有 local network 彼此连接，最终形成 Internet。

在 Internet 中，不同链路可能采用不同的 Layer 2 技术。有些链路可能使用有线 Ethernet（以太网），而另一些链路可能采用光纤或蜂窝无线技术。在 Layer 2 中，我们关注的是：如何利用该 network 内部所采用的具体技术，在 local network 中跨链路发送 packet。而在 Layer 3 中，我们则将「沿链路发送 packet」的能力作为基础构件，实现 packet 在整个 Internet 中的任意传输。当 packet 跨越不同 network 时，它可能会经过多种不同类型的链路。

<img width="700px" src="/assets/intro/1-05-different-links.png">

在邮政系统类比中，我们可以区分「家庭」与「邮局」。家庭负责彼此收发信件，而邮局本身并不收发自己的邮件，它们存在的意义是帮助其他家庭完成通信。

在 Internet 中，**end host（端系统）** 指的是通过 Internet 通信的机器，例如 server、laptop、phone 等。与之相对，**switch/router** 本身并不发送或接收自己的数据，它存在的目的仅仅是帮助 end host 彼此通信。例如你家中的 router，或者 ISP 部署的大型 router。

在这些讲义中，我们通常会将 end host 画成圆形，将 router 画成方形。

## 抽象层

在逐步构建 Internet 的过程中，你可能已经注意到：我们正在不断把问题拆解为更小的任务与抽象。

Barbara Liskov 在 Turing lecture 中曾说：

> “Modularity based on abstraction is the way things are done.”

也就是说，「基于抽象的模块化是构建大型系统的基本方式。」

这正是我们构建和维护大型计算机系统的方法。对于 Internet 而言，modularity 尤其重要，因为 Internet 涉及大量设备（host、router）以及现实中的大量实体（用户、科技公司、ISP）。只有所有人都对任务分层达成一致，Internet 才能以如此大规模正常运作。

这种 layered、network-of-networks 的方法有一个重要优点：每个 network 都可以自主决定如何移动数据。例如，你的 packet 在 Internet 中跳转（hop）时，某些链路可能采用 wireless 技术，而另一些链路采用 wired 技术。不同 hop 的 lower-layer protocol 可以完全不同，而 Layer 3 protocol 依然能够正常工作。

Layering 还允许不同领域并行创新。例如，硬件芯片设计者与软件开发者可以分别在不同 layer 上推进创新。

## Layer 3：Best-Effort 服务模型

看起来我们已经构建出了一个能够向全世界发送数据的系统，那么为什么不止步于此呢？因为 Layer 3 仍然存在两个问题需要解决。

第一个问题是 Layer 3 的服务模型。如果你使用 Layer 3 基础设施在 Internet 上传输消息，那么 network 会向用户提供怎样的服务？你可以把服务模型理解为 network 与用户之间的一份「契约」，它规定了 network 支持什么、不支持什么。

一些可能的 service model 包括：

- network 保证数据一定送达；
- network 保证数据在某个时间限制内送达；
- network 不保证送达，但会在失败时报告错误。

然而，Internet 的设计者并没有采用这些模型。相反，Internet 只提供 **best effort（尽力而为）** 的数据传输。也就是说，如果你通过 Layer 3 发送数据，Internet 会「尽力」传输它，但并不保证数据一定送达，也不会告诉你传输是否成功。

为什么设计者选择了如此「弱」的 service model？其中一个重要原因是：满足这种弱要求的 network 更容易构建。

## Layer 3：Packet 抽象

到目前为止，在 Layer 3 中，我们一直将每条消息视作独立发送的对象。更正式地说，Layer 3 中最基本的数据传输单位是 **packet**：它是一个较小的数据块，在 Internet 中作为单一单位，在 router 之间不断跳转。

Layer 3 的第二个问题在于：packet 的大小是有限的。如果 application 想要发送大量数据（例如视频），就必须把这些数据拆分成多个 packet，并让每个 packet 独立穿越 network。

有了 packet 抽象之后，我们便可以观察 packet 在 network 中的完整生命周期：

发送方首先将数据拆分为 packet；

packet 沿链路传输并到达 switch；

switch 会把 packet 转发给目标主机，或者转发给一个更接近目标的 switch；

packet 会在一个或多个 switch 之间不断 hop，每一次 hop 都更接近最终目的地，直到最终抵达 destination。

需要注意的是，由于采用 best-effort model，任意一个 switch 都可能丢弃 packet，因此 packet 并不一定能够真正抵达 destination。

<img width="700px" src="/assets/intro/1-06-path-through-network.png">

## Layer 4：传输层

目前为止，我们已经发现 Layer 3 存在两个问题：

1. 大数据必须拆分成多个 packet；
2. IP 仅提供 best-effort 服务。

为了解决这两个问题，我们引入新的 layer：**transport layer（传输层）**。这一层以 Layer 3 为基础构件，并实现额外 protocol，用于：

- 重传丢失 packet；
- 将数据拆分成 packet；
- 对乱序到达（out-of-order）的 packet 重新排序；
- 以及其他功能。

Transport layer protocol 让我们不再需要从「packet」的角度思考问题，而可以转而从 **flow（数据流）** 的角度理解通信：即两个 endpoint 之间交换的一系列 packet 流。

## Layer 7：应用层

建立在 Internet 之上的 application layer 是一个极其强大的设计选择。假如在 lower layer 中，我们专门构建了一个「用于视频传输」的基础设施，那么 email client 就不得不再单独建设一套用于邮件传输的基础设施。Internet 的设计使它能够成为一个通用通信网络，从而支持任意类型的 application data。

在本课程中，我们会更多关注支撑 application layer 的基础设施（例如邮递员、邮局），而不是 application 本身（例如信件内容）。不过在课程后半部分，我们也会接触一些常见的 application protocol。

现在，当我们回顾所有 layer 时，会发现：

- 每一层都依赖于其下层提供的服务；
- 同时又向其上层提供服务。

例如，编写 Layer 7（application）protocol 的人，可以默认 Layer 4 已经提供 reliable data delivery（可靠数据传输）。他们不需要再考虑 packet 丢失问题，因为这些已经由 Layer 4 解决。

<img width="700px" src="/assets/intro/1-07-layers.png">

两个 layer 之间只能通过接口直接交互。实际上不存在「跳过中间层、直接让 Layer 7 建立在 Layer 3 之上」这种做法。

最后，你可能注意到我们跳过了 Layer 5 与 Layer 6。这是因为在 1970 年代层次结构首次标准化时，设计者认为这些 layer 是必要的，但它们在现代 Internet 中已经基本过时。

其中：

- Session Layer（第 5 层）原本用于将不同 flow 组合成 session（例如把网页中的图片与广告组合成一个完整网页）；
- Presentation Layer（第 6 层）原本用于帮助用户可视化数据。

而今天，这些功能大多已经由 Layer 7 实现。
