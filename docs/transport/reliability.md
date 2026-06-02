---
title: Transport Layer Principles
parent: Transport
nav_order: 1
layout: page-with-toc
---

# Transport Layer 原理

## 可靠性抽象和目标

很多应用需要可靠性。例如，在 Internet 上发送文件时，我们希望 recipient 收到的字节和 sender 发出的字节完全相同，并且顺序也完全相同。

然而，Layer 3 只提供不可靠的 best-effort packet 递送。packet 可能丢失（被丢弃）、损坏，也可能乱序（发送 packet 的顺序和接收 packet 的顺序不一致）。packet 还可能被延迟，例如某个 packet 可能卡在队列里，等待通过一条 link。

在少数情况下，packet 甚至可能被复制：sender 只发送了一个 packet，但 recipient 收到了这个 packet 的多个副本。这通常发生在路径上的某个 router 遇到某类错误时。在实践中，这种错误非常少见。

有趣的是，UC Berkeley 的 Vern Paxson 是最早发现并报告 link layer 中 packet 重复现象的人之一。

我们会使用 Layer 4（传输层）来弥合这个差距：开发一些 protocol，它们依赖网络支持的 best-effort packet 抽象，同时为应用开发者提供可用的可靠抽象。

出于实践上的原因（其他地方会讨论），可靠性在 end host 上实现，而不是在中间 router 上实现。另外，为了方便，可靠性通常实现在操作系统中，这样应用就不需要各自重新实现一套可靠性机制。

<img width="900px" src="/assets/transport/3-007-reliability-at-end-hosts.png">

我们先用 **at-least-once delivery**（至少一次递送）来形式化可靠性。在这个模型中，目的地必须至少一次收到每个 packet，并且 packet 不能损坏；但目的地可能收到同一个 packet 的多个重复副本。传输层会利用 best-effort delivery 来提供 at-least-once delivery。然后，我们的 protocol 可以在 at-least-once delivery 的基础上删除重复副本，为应用提供 exactly-once delivery。

注意，可靠递送并不保证 packet 一定会被发送出去。一台没有连接到网络的计算机，无论使用什么可靠性 protocol，都无法把数据发送到目的地。可靠性 protocol 可以放弃并发送失败，但必须把失败报告给应用。protocol 不能虚假地声称某个 packet 已经成功递送。

我们的 protocol 也应该高效。更具体地说，它应该尽可能快地递送数据，并且尽量减少带宽使用，避免发送不必要的 packet。例如，我们可以通过把每个 packet 重发数百次来保证 packet 到达，但这会违反高效使用带宽的要求。

## 传输层目标

在传输层，我们的目标是给应用提供方便的抽象，让开发者的工作更简单。传输层允许应用开发者从连接的角度思考，而不是从网络中单个 packet 的发送角度思考。理想情况下，开发者不需要考虑底层网络细节，例如把长数据拆成 packet、重发丢失的 packet、超时等。

可靠性只是我们可能希望在传输层实现的几个目标之一。

传输层通过引入 port number，在 end host 上不同进程之间实现 **demultiplexing**。port number 可以用来把每个 flow（connection）关联到 end host 上的不同进程。

传输层还实现 flow control 和 congestion control，它们分别帮助限制 packet 的发送速率，避免让接收方和网络过载。

## 使用 Port 做 Demultiplexing

假设我的个人计算机上有两个应用，它们都在和同一个 server 通信。当 packet 到达我的个人计算机时，它们有相同的 source IP address（server）和相同的 destination IP address（我的计算机）。我怎么判断哪些 packet 属于哪个应用？

<img width="900px" src="/assets/transport/3-001-demultiplex.png">

为了区分，也就是 **demultiplex**，哪些 packet 属于哪个应用，transport layer header 中包含一个额外的 **port number**，可以用来识别 end host 上的某个具体应用。

<img width="900px" src="/assets/transport/3-002-ports.png">

当传输层收到一个 packet 时，它可以使用 port number 决定 payload 应该交给哪个更高层的应用。因为传输层实现在操作系统中，这些 port（有时称为 **logical port**）就是应用连接到操作系统网络栈的位置。应用知道自己的 port number，操作系统知道所有应用的 port number，匹配的编号让数据可以在应用和操作系统之间明确传递，而不会和其他应用的数据混在一起。

<img width="800px" src="/assets/transport/3-003-port-attachment.png">

port number 长度为 16 bit。现代 Internet 通常使用 client-server 设计：client 访问服务，server 提供服务。server 通常在 well-known port（端口号 0-1023）上监听请求。client 知道这些 port，并且可以访问它们来请求服务。例如，带有 well-known port number 的应用层 protocol 包括 HTTP（port 80）和 SSH（port 22）。

相比之下，client 可以选择自己的随机 port number（通常是端口号 1024-65535）。这些 port number 可以随机选择，因为 client 是发起连接的一方，而且没有人依赖 client 拥有固定的 port number（client 不提供服务）。client 的 port number 是 **ephemeral**（临时的），因为连接结束后这个 port number 可以被丢弃，不需要永久保留。

## Bytestream 抽象

在传输层实现可靠性意味着，应用开发者不再需要从一个个大小受限、在网络中发送的 packet 角度思考。相反，开发者可以从 **可靠、有序的 bytestream** 角度思考。sender 有一条没有长度限制的字节流，并把这条流交给传输层。然后，recipient 会以相同顺序收到完全相同的字节流，并且没有字节丢失。你可以把 bytestream 想象成一根管道：sender 把字节一个接一个放进管道，同样的字节会一个接一个从 recipient 这一端出现。sender 和 recipient 不需要考虑重发丢失的 packet，也不需要考虑 packet 乱序到达，因为传输层 protocol 会替开发者实现这些事情。

<img width="900px" src="/assets/transport/3-004-bytestream.png">

## UDP 和 Datagram

有时，应用并不需要可靠性。例如，考虑一个读取你家水压的传感器。这个传感器每分钟向公用事业公司发送一次读数（包含时间和水压的小型固定大小消息）。这个系统可能不需要 packet 按顺序到达，例如读数本身已经包含时间戳；也可能不需要把长消息拆成 packet 的能力，因为每条读数都很小。只要大多数读数能到达公用事业公司，这个系统甚至可能不需要可靠性。

不需要可靠性的应用可以在传输层使用 **UDP**（User Datagram Protocol），而不是 TCP。UDP 不提供可靠性保证。如果应用需要某个 packet 到达，应用必须自己处理 packet 重发（传输层不会重发 packet）。UDP 中的消息限制为单个 packet。如果应用想发送更大的消息，应用需要负责拆分并重新组装这些消息。不过要注意，UDP 仍然实现了用于 demultiplexing 的 port 概念。

<img width="900px" src="/assets/transport/3-005-datagram.png">

在传输层，你可以根据需求选择使用 UDP 或 TCP，但不能同时选择二者。UDP 和 TCP 是现代 Internet 中标准的传输层 protocol。

<img width="300px" src="/assets/transport/3-006-tcp-features.png">

## 其他可靠性设计

TCP 最初由 Vint Cerf 和 Bob Kahn 实现，当时他们还是 UCLA 的学生。此后，他们因为这项工作获得了 Turing Award、Presidential Medal of Freedom 等荣誉。很了不起的是，最初的 TCP 设计和今天实践中使用的设计非常相似，并经受住了时间考验。TCP 的核心思想相当简单，设计也很优雅（虽然并不完美）。不过，实现要做对可能很棘手，而且风险很高，因为几乎整个现代 Internet 都运行在 TCP 之上。

自 TCP 最初创建以来，TCP 的许多具体部分已经演化，例如更好的 timer 估计算法、更聪明的 acknowledgement、更聪明的 ISN 选择、congestion control 等，但核心架构决策和抽象（connection-oriented bytestream、window）保持不变。

TCP 是 Internet 上标准的可靠性 protocol，但也存在其他根本不同的方法。

例如，sender 可以利用冗余的思想（类似 error-correcting code 或 RAID 中看到的做法）来更可靠地发送数据。sender 不是原样发送用户数据，而是把数据编码成更多 packet，并在每个 packet 中有意加入冗余。例如，用户可能有 10 个 packet，某个算法可能把这些数据编码成 20 个 packet。这个算法可能保证，只要 20 个 packet 中任意 15 个被收到，就能重建原始的 10 个数据 packet。

更形式化地说，一个编码算法可能接收 k 个 packet，把它们编码成 n 个 packet（其中 n 大于 k），使得只要收到任意 k' 个 packet（其中 k' 大于 k 但小于 n），就能恢复原始的 k 个 packet。

Coding scheme 是一个很深的主题，包含很多算法，例如 fountain code、raptor code，不过我们不会进一步讨论它们。它们可以在视频流平台等实践系统中看到。
