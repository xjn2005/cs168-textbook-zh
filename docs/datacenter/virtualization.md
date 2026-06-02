---
title: Virtualization
parent: Datacenters
nav_order: 5
layout: page-with-toc
---

# Virtualization and Encapsulation

## 物理 Datacenter 的限制

Datacenter 以固定且结构化的方式组织。相同的 server 被组织进 rack，而 rack 又按照某种固定 topology 排列。这种方法有一些好处。例如，它给了我们一种自然方式来分配 hierarchical address。

不过，当我们考虑 application 如何托管在 datacenter 中时，datacenter 的固定组织也有一些缺点。假设 Google 推出一个新 service，并希望把它托管在现有 datacenter 中。如果我们把这个 application 直接放在一台 physical server 上，就必须有人为这个 application 物理安装一台新 server，并为它分配自己的 IP address。如果 service 扩张，可能还需要安装更多 server。如果 server 宕机，我们就必须等待有人修复它。这里的核心问题是：改变物理基础设施很难，但我们经常希望快速且频繁地添加新 host、扩展现有 host，并移动 host。

把 application 放在 physical server 上还会带来扩展问题。假设 Google 的新 service 非常轻量，但需要一台 dedicated server（例如出于安全原因）。我们必须把整台 physical server 分配给这个轻量 service，而这台 server 的大部分计算能力都会闲置。

这种方法也有 routing 问题。假设我们想把这个 service 移到 datacenter 建筑中的另一个区域（例如因为建筑的一部分正在维护）。首先，必须有人在建筑中物理移动 server。另外，在我们的 hierarchical address 模型中，我们需要给这个 service 分配一个新的 IP address，对应它新的物理位置。理想情况下，application 更希望保持同一个地址，而不管它位于 datacenter 的哪个位置。

<img width="900px" src="/assets/datacenter/6-043-dc-address-scaling.png">

## Virtualization

我们可以用 virtualization 来解决这些问题，在维持 datacenter 刚性物理结构的同时，让 application 更灵活。**Virtualization（虚拟化）** 允许我们在一台 physical server 内运行一个或多个 virtual server。

Virtual server 给 application 一种错觉：它们正运行在一台 dedicated physical machine 上。不过，在现实中，多台 virtual server 可能运行在同一台 machine 上。当 application 试图与硬件交互（例如 disk、network card）时，它实际上是在与软件中的 **hypervisor** 交互。Hypervisor 向每个 virtual application 呈现真实硬件会提供的相同 interface。Hypervisor 自身运行在真实 physical hardware 上，并且可以把 application request（例如 disk write、network packet send）转发到硬件层。

有了 virtualization，如果我们有一个新 application，就可以请求 hypervisor 为这个 application 启动一个新的 virtual machine。Hypervisor 运行在软件中，因此不需要在 physical datacenter 中安装任何新 server。类似地，我们也可以完全通过软件把 host 移动到另一台 physical machine 上。

<img width="900px" src="/assets/datacenter/6-044-vm.png">

Virtualization 允许多个 application 共享一台 physical server。这些 application 可以彼此隔离，并由不同的人管理。这让我们能更高效地使用 datacenter 中的 compute resource。它也允许 datacenter 中拥有更多 host。例如，一个包含 40 台 server 的 rack 可以拥有超过 40 个 end host。

## Virtual Switch

Physical server 有一张 network card 和一个 IP address，但我们需要给每台 virtual machine 一种错觉：它有自己的 dedicated network card 和 address。另外，switch 现在可能有多台 virtual machine 连接到同一个 physical port。

为了管理同一台 physical machine 上的多个 network connection，server 需要一个 **virtual switch**。这个 virtual switch 在 server 上以软件形式运行（它不是 physical router），并执行真实 switch 会执行的相同操作（例如 forwarding packet）。每台 virtual machine 都连接到 virtual switch，而 virtual switch 连接到网络的其余部分。

<img width="500px" src="/assets/datacenter/6-045-virtual-switch.png">

注意：Switch 通常运行在专用硬件上，以最大化效率。Virtual switch 可以在通用 CPU 上用软件运行，因为它只需要支持少量 virtual machine（容量低于 switch 通常需要处理的规模）。

## Underlay 和 Overlay Network

有了 virtualization，现在我们有了运行在 physical server 之上的 virtual host。不同于 physical server，virtual host 可以被快速创建、关闭和修改。

Virtual machine 不一定使用和 physical server 相同的 addressing scheme。Physical server IP address 由 physical datacenter topology 定义（例如 pod、rack）。相比之下，virtual machine IP address 通常由某种现实世界的 hierarchy 定义（例如国家、组织）。特别是，同一台 physical server 上的 virtual host 不一定都有相同 IP prefix，因此我们不能使用相同的 aggregation 技巧来扩展。

如果我们天真地扩展 routing scheme 来支持 virtual machine，forwarding table 会很快变得非常大。之前，我们可以通过这种方式 aggregate： “blue pod 中的所有 server 都有相同 IP prefix，并且它们都有 R2 作为 next hop。” 现在，blue pod 中的 server 可能包含数百个 virtual host，它们都有不同 IP address（没有 common prefix）。我们将需要为每个 virtual host 准备一个单独的 forwarding entry。另外，如果一个 virtual host 移动到另一台 physical machine（保持相同 IP address），routing protocol 就必须重新发现到这个 virtual host 的 path。我们能不能避免为了支持每个 VM address 而扩展整个 datacenter？

这里的核心问题是：现在我们有两个不同的 addressing system，一个用于 virtual host，另一个用于 physical host。两套 addressing scheme 都工作在 IP layer，但在 IP layer 内部，现在有两个抽象 sub-layer 需要思考。

**Underlay network（底层网络）** 处理 physical machine 之间的 routing。Underlay network 包含 top-of-rack switch 和 spine switch 这样的 datacenter 基础设施。Underlay network 具有良好扩展性，因为我们使用 physical datacenter topology 定义 hierarchical address。

**Overlay network（覆盖网络）** 位于 physical topology（underlay）之上，只思考 virtual machine 之间的 routing。在实践中，每台 virtual machine 通常只需要与网络中的少量其他 virtual machine 通信。因此，overlay network 具有良好扩展性，因为一台 virtual machine 不需要知道其他每一台 virtual machine。

<img width="900px" src="/assets/datacenter/6-046-virtual1.png">

理想情况下，我们希望这两层分别思考 addressing。Underlay network 不应该需要知道 virtual host address（否则扩展性会很差）。类似地，overlay network 不应该需要知道 datacenter 中每台 physical server（每台 VM 只需要知道少量其他 VM）。

如果我们不告诉 underlay network 关于 virtual host address 的信息，那么当 datacenter switch 收到一个以 virtual IP 为 destination 的 packet 时，它会查找自己的 forwarding table，找不到任何 virtual IP，然后丢弃这个 packet。我们需要某种方法，在 overlay（以虚拟方式思考）和 underlay（以物理方式思考）之间架桥。

## Encapsulation

为了统一 overlay 和 underlay layer，我们可以使用设计 Internet 时用过的 layering 和 header 策略！

到目前为止，我们把 IP 当作单一 layer，每个 packet 有一个 IP header，它理解 IP addressing system。

现在我们有两个 IP sub-layer，且它们有两个不同的 IP addressing system，因此可以向 packet 中引入一个额外 header。例如，我们可以有两个 IP header，其中一个 header 理解 overlay network，另一个 header 理解 underlay network。或者，我们可以把原始 IP header 用于 underlay network，并为 overlay network 引入一种新的 header 类型（不同于 IP）。

<img width="700px" src="/assets/datacenter/6-047-virtual2.png">

现在，我们的 packet routing 策略可以把 overlay 和 underlay network 结合起来。假设 VM A 想向 VM B 发送一个 packet。

<img width="900px" src="/assets/datacenter/6-048-virtual3.png">

1. VM A 创建一个只有单个 IP header 的 packet，其中包含 B 的 virtual IP address。（记住，A 是从 overlay 的角度思考，并不知道 underlay physical IP address。）VM A 把这个 packet 转发给 virtual switch（位于 A 所在的 physical server 上）。

    <img width="900px" src="/assets/datacenter/6-049-virtual4.png">

2. Virtual switch 读取 header，得知 B 的 virtual IP address。然后，virtual switch 查找与 B 的 virtual IP address 对应的 physical server address。（我们还没有描述如何做到这一点。）

    Virtual switch 添加一个额外的 outer header，其中包含 B 的 physical server address。添加 header 有时称为 **encapsulation（封装）**。

    此时，packet 有两个 header。Inner header（更高层、overlay、由 VM A 添加）包含 B 的 virtual IP address，outer header（更低层、underlay、由 virtual switch 添加）包含 B 的 physical server address。

    Virtual switch 根据 physical server address，把这个 packet 转发给 next hop switch。

    <img width="900px" src="/assets/datacenter/6-050-virtual5.png">

3. Packet 会穿过 underlay network 发送。Datacenter 中的每个 switch 只查看 outer header（underlay、physical server address）来决定如何转发 packet。（记住，datacenter switch 以 underlay 的方式思考，并不知道 overlay virtual IP address。）

    <img width="900px" src="/assets/datacenter/6-051-virtual6.png">

    <img width="900px" src="/assets/datacenter/6-052-virtual7.png">

4. 最终，packet 到达 destination physical server 的 virtual switch。Virtual switch 查看 outer header（underlay），并注意到 destination physical server address 就是自己。

    Virtual switch 移除 outer header，露出内部的 inner header。移除 outer header 有时称为 **decapsulation（解封装）**。

    <img width="900px" src="/assets/datacenter/6-053-virtual8.png">

最后，virtual switch 读取 inner header（overlay）。这会告诉 virtual switch，packet 应该被转发给 physical server 上的哪台 VM。

<img width="900px" src="/assets/datacenter/6-054-virtual9.png">

在这个过程中，**encapsulation** 允许我们在两个不同 layer 上思考 routing。Underlay 可以使用 physical server address route packet，而不必思考 overlay。类似地，overlay 中的 VM 可以发送和接收 packet，而不必思考如何在 underlay 中转发 packet。Virtual switch 通过把 virtual machine address 翻译成 physical server address，并添加和移除额外 underlay header，把两层连接起来。

<img width="900px" src="/assets/datacenter/6-055-virtual10.png">

<img width="800px" src="/assets/datacenter/6-056-virtual11.png">

<img width="900px" src="/assets/datacenter/6-057-virtual12.png">

## 支持 Encapsulation 的 Forwarding Table

为了支持使用 encapsulation 的 routing，我们应该在 forwarding table 中安装哪些 entry？

Virtual machine 应该安装一条 default route，把每个 packet 都转发给 physical machine 上的 virtual switch。

Virtual switch 需要实现一些额外功能，把这两层连接起来。特别是，当你看到一个 virtual address 时，应该用对应的 physical address 执行 encapsulation（添加外层）。Forwarding table 中会有每个 destination VM 的 entry，这些 destination VM 是这台 server 上任一 VM 可能想要通信的对象。我们可以支持这个规模，因为我们假设 VM 不需要和 datacenter 中的每一台其他 VM 通信。不同于标准 routing algorithm，我们不需要 any-to-any routing（不需要到每一台其他 VM 的 path）。

Virtual switch 还需要一个额外规则来 decapsulate packet。如果 outer（underlay）packet destination 是 switch 自己，就应该 decapsulate（移除 outer header），并把 packet 传给 inner header 中的 VM address。这个规则的规模随 server 上 VM 数量增长，而这个数量通常足够小，可以管理。

添加这个功能困难吗？幸运的是，virtual switch 是用软件实现的，所以添加这个功能只需要写代码（不需要额外硬件）。不过，在实践中，encapsulation 非常常见，所以有时也会在硬件中实现。

Datacenter 中的 switch 和引入 virtualization 之前完全一样。Forwarding table 只包含 physical server address，而我们知道这些地址可以基于 physical topology 用 aggregation 技巧扩展。

## Multi-Tenancy 和 Private Network

Datacenter 由单个 operator 管理，但不同组织可能都在这个 datacenter 中运行 application。例如，一个由 Google 运营的 datacenter 可能有一些 virtual server 运行 Gmail，也有一些运行 Google Maps。把多个 service 托管在一个 datacenter 中的这种方法称为 **multi-tenancy（多租户）**。

Cloud provider 也使用 datacenter 为 customer 提供 virtual machine。例如，Amazon Web Services（AWS）和 Google Cloud Platform（GCP）允许 user 在 datacenter 中启动一台 virtual machine，随意使用它，并在完成后销毁这台 virtual machine。

Multi-tenancy 的一个问题是，我们并不总是希望不同 tenant 能够彼此通信。例如，如果一个 customer 请求一台 VM，他们可能不应该能连接到 datacenter 中的每一台其他 VM。

另一个问题是，datacenter 中的 tenant 在选择地址时彼此不协调。例如，假设我们的 datacenter 有两个 tenant，Pepsi 和 Coke。每个 tenant 都创建自己的 private network，并在其中为 virtual machine 分配 internal IP address。Private network 只用于 datacenter 内部 host 之间相互通信，这些 host 永远不会被 public Internet 联系到。由于这些 network 是 private 的，两个 tenant 可以使用同一个专门分配的 private range 中的地址（RFC 1918 address）。Pepsi 的 private network 可能有一台 IP address 为 192.0.2.2 的 VM，而 Coke 的 private network 可能有另一台 IP address 也是 192.0.2.2 的 VM。（实践中，我们使用 private range 是为了复用 IPv4 address，因为它们快用完了。）

<img width="900px" src="/assets/datacenter/6-058-tenancy1.png">

从每个 tenant 的视角看，这不是问题。Pepsi 的 192.0.2.2 永远不会与 Coke 的 192.0.2.2 通信，并且两个 host 都无法被 global Internet 访问。但是，这对 datacenter 来说是个问题。如果使用 destination-based forwarding，而我们看到一个 destination 为 192.0.2.2 的 packet，就不知道这个地址指的是哪台 VM。

Duplicate IP address 在实践中出现有两个原因。第一，datacenter 通常无法控制 tenant 给自己的 VM 分配什么地址。第二，在 IP 中，为 private network 使用特定地址范围是标准做法，这往往会导致 duplicate address。

## 用于 Multi-Tenancy 的 Encapsulation

我们可以再次使用 encapsulation 的思想来解决这个问题。我们可以添加一个新 header，其中包含 **virtual network ID**，用于标识特定 tenant（例如 Pepsi 的 ID 是 1，Coke 的 ID 是 2）。这个新 header 不包含用于 forwarding 和 routing 的信息，但它提供了额外 context。现在，如果一台 physical server 上有多个 tenant 的 VM，它就可以把 packet 向上传递给正确的 virtual network。

<img width="900px" src="/assets/datacenter/6-059-tenancy2.png">

<img width="900px" src="/assets/datacenter/6-060-tenancy3.png">

当 virtual switch 收到一个 packet 并解开 outer（underlay）header 时，它会查看我们的新 header，决定这个 packet 是给哪个 tenant 的。然后，它查看 overlay header，把 packet 转发给属于正确 tenant 的某台具体 VM。

## 堆叠 Encapsulation

我们可以多次使用 encapsulation 思想，添加多个新 header，以同时支持 virtualization 和 multi-tenancy。

首先，virtual machine 创建一个标准 TCP/IP packet，其中包含 virtual IP destination。

在第一步 encapsulation 中，我们添加一个 virtual network header，它告诉我们这个 packet 是哪个 tenant 发送的。这帮助我们消除两个 tenant 使用同一地址时的歧义，也防止 packet 被发送到不同 tenant。

在第二步 encapsulation 中，我们添加一个 underlay network header，它告诉我们与 virtual IP destination 对应的 physical server address。

<img width="900px" src="/assets/datacenter/6-061-stack1.png">

当我们堆叠 encapsulation 时，抽象 layer 仍然成立。Underlay network 不需要知道同一个 datacenter 中有多个 tenant。Underlay network 只查看最外层 header 中的 physical server address，并据此转发 packet。

Decapsulation step 按相反顺序工作。Destination server 上的 virtual switch 收到一个带有两个额外 header 的 packet。

在第一步 decapsulation 中，我们移除 outer underlay header。由于 packet 已经到达 destination physical server，这个 header 不再必要。

在第二步 decapsulation 中，我们使用 virtual network header 决定应该考虑哪一组 VM。Physical server 可能有多个 tenant 的 VM，这帮助我们缩小到单个 tenant。

最后，我们使用最内层 IP header，把 packet 发送给正确 virtual network 中的正确 VM。

<img width="900px" src="/assets/datacenter/6-062-stack2.png">

注意：使用 encapsulation 时，我们在读取 5-tuple（IP、port 和 protocol）以便把 packet load-balance 到多条 path 上时必须小心。幸运的是，现代 router hardware 擅长解析 packet，即使插入了额外 header，也能理解相关 header 在 packet 中的位置。

在实践中，存在许多不同的 encapsulation protocol。我们可以使用 IP-in-IP 来支持两个 IP header（一个用于 overlay，一个用于 underlay）。

MPLS 是一种简单 header，用于添加标识某个 service（例如 virtual network、tenant）的 label。它可用于为 multi-tenancy 添加 encapsulation。

随着 datacenter 变得越来越流行，GRE、VXLAN 和 GENEVE 等许多其他 protocol 也被开发出来。它们大多运行在 IP 之上，因此这些 custom protocol 是内部 overlay header，而普通 IP 是外部 underlay header。
