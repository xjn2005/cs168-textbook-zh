---
title: "DHCP: Joining Networks"
parent: End-to-End
nav_order: 4
layout: page-with-toc
---

# DHCP：加入网络

## 加入网络

当一台计算机第一次加入网络时，它需要哪些信息才能连接到 Internet？

我们总是知道自己的 MAC 地址，因为它被写入了硬件。

我们需要被分配一个 IP 地址，才能发送和接收 packet。回忆一下，IP 地址是按地理位置分配的，所以当我们连接到一个新网络时，必须有人给我们一个可用的 IP 地址。

我们需要知道 subnet mask，这样才能知道本地 IP 地址的范围。给定 mask（固定 bit 全为 1，不固定 bit 全为 0），我们可以把 mask 与自己的 IP 地址做 bitwise AND，从而得到本地 IP prefix。

我们需要知道本地网络中的 router 是谁，这样才能把所有非本地 packet 发送给这个 router。有时我们把这个 router 称为 **default gateway**。

我们还可能需要知道这个网络的 DNS recursive resolver 位于哪里。

用户可以在第一次加入网络时手动配置这些值。但这很耗时，尤其是每次加入不同网络都要重新配置。另外，普通 Internet 用户大概也不知道怎样手动配置这些值。话虽如此，手动配置有时确实适用于 router 这类不太会移动的机器。

我们需要一个 protocol，让新的 host 能够自动学习这些值（也可能学习其他有用信息）。


## DHCP：Dynamic Host Configuration Protocol

DHCP 有四个步骤：

1. 新 client 广播一条 **Discover** 消息，请求配置信息。

    <img width="800px" src="/assets/end-to-end/5-050-dhcp1.png">

2. 任何能够提供帮助的 **DHCP server** 都会向 client unicast 一个 **Offer**，其中包含 client 可以使用的配置（例如 IP 地址、gateway 地址、DNS 地址）。

    <img width="800px" src="/assets/end-to-end/5-051-dhcp2.png">

3. client 会广播一条 **Request** 消息，说明它接受了哪个 offer。这条消息要广播，是因为 client 可能收到多个 offer。通过告诉所有人它接受了哪个 offer，client 允许那些被拒绝的 offer 释放出来，供之后的 client 使用。

    <img width="800px" src="/assets/end-to-end/5-052-dhcp3.png">

4. server 发送 acknowledgement，确认这个 request 已被批准。

    <img width="800px" src="/assets/end-to-end/5-053-dhcp4.png">


## DHCP Server

在第 2 步中，谁能够提供配置？DHCP server 会被加入网络，它们的目标是向新的 host 提供这些信息。在你的家庭网络这类较小网络中，家庭 router 本身通常也充当 DHCP server。在较大的网络中，可能会有一台单独的机器作为 DHCP server。

DHCP server 需要和 client 位于同一个本地网络中，因为这个 protocol 在本地网络内部运行。在较大的网络中，我们可能不想在每台 router 里运行 DHCP server 代码，因此本地 router 可以把请求 relay 给一个远程的中央 DHCP server，由后者真正运行这个 protocol。

DHCP server 会在固定端口 UDP port 67 上监听来自新机器的请求。server 配置了所有必要信息：它们知道 gateway 和 DNS server，并且拥有一组可用 IP 地址，可以分配给新的用户。

<img width="900px" src="/assets/end-to-end/5-054-dhcp-over-ip.png">

注意，IP 地址只是临时租给 host 的。租约只在有限时间内有效（例如数小时或数天的量级）。如果 host 想继续使用这个地址，就必须续租。如果某个 IP 地址当前已经租给了某台 host，DHCP server 就不能把同一个地址 offer 给其他 client。


## DHCP 实现

注意，DHCP 是一个 Layer 7 application protocol，它运行在 UDP 之上，而 UDP 又运行在 IP 之上。

在第 1 步中，client 如何通过 IP 广播消息？它发送一个目的 IP 为 255.255.255.255（全 1）的 packet，这是 IPv4 broadcast address。当这个 packet 被交给 Layer 2 时，不会用 ARP 转换这个 IP 地址，而是把 IPv4 broadcast address 映射到 Ethernet broadcast address FF:FF:FF:FF:FF:FF（全 1）。这样，packet 就能在 Layer 2 中广播到整个网络。

source IP 呢？client 在 protocol 开始时还没有 source IP，因此把 source IP 设为 0.0.0.0。

有了硬编码的 source IP 0.0.0.0 和 destination IP 255.255.255.255，client 不需要知道任何本地网络信息，就可以开始运行这个 protocol。

如果没有 source IP，DHCP server 怎么知道如何 unicast offer？DHCP server 可以广播 offer，也可以使用 client 的 MAC 地址来 unicast offer。


## IPv6 中的自动配置

DHCP 也存在于 IPv6 网络中。不过，由于 IPv6 地址更长，我们实际上可以给自己分配一个保证唯一的 IPv6 地址，而不需要其他人管理地址池并出租地址。这个 protocol 称为 **Stateless Address Autoconfiguration（SLAAC）**。

技巧是利用 MAC 地址，因为我们知道它对每台机器都是唯一的。和之前一样，我们会请求本地网络信息，其中包括 gateway 地址、DNS 地址，以及尤其重要的本地网络 prefix。这个 prefix 通常是 64 bit 长。然后，我们把自己的 MAC 地址 bit 复制到 IPv6 地址的 host bit 中。我们可以相信没有其他人拥有这个 IPv6 地址：其他网络中的用户会有不同的 prefix，而这个网络中（或其他任何地方）也不会有人拥有相同的 MAC 地址 bit。

<img width="900px" src="/assets/end-to-end/5-055-slaac.png">

为了获取本地网络信息，我们可以扩展 Neighbor Discovery protocol（IPv6 版本的 ARP）。Router Solicitation 消息允许用户广播本地网络信息请求，而 Router Advertisement 消息允许 router 回复这些信息。

SLAAC 还有额外机制来检测重复地址，以防万一。
