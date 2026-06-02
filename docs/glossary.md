---
title: Glossary
nav_order: 9
---

# 术语表

本术语表改编自 [CS 168 过往开课版本](https://sp24.cs168.io/glossary)。

<table>
        <thead>
          <th>术语</th>
          <th>定义</th>
        </thead>
        <tbody><tr>
            <td>ACK</td>
            <td align="left"><p>设置了 ACK flag 的 TCP packet，表示数据已经被接收。</p>
</td>
          </tr><tr>
            <td>ARP</td>
            <td align="left"><p>Address Resolution Protocol。允许设备把 IP 地址映射到 MAC address 的 protocol。设备会发送（broadcast）ARP <strong>Request</strong> message，以找出某个 IP address 对应的 MAC address。被查询的设备会用 ARP <strong>Response</strong> message 进行响应（unicast）。MAC address 和 IP address 之间的 mapping 存储在 ARP table 中，ARP table 作为 cache 使用。ARP table 中的 entry 会 timeout（soft state）。</p>
</td>
          </tr><tr>
            <td>Autonomous System</td>
            <td align="left"><p>由单个实体或组织统一管理和监督的一个 network 或一组 network。单个 ISP 通常是一个 AS；不过，有些 ISP 会把自己的 network 划分为多个 AS。每个 AS 都会被分配一个 number，在 BGP 中用于标识 path。</p>
</td>
          </tr><tr>
            <td>AXE</td>
            <td align="left"><p>一种提出过的 STP 替代方案，它不需要 spanning tree，而是通过 duplicate suppression 来防止 loop。也是一些绝妙诗歌的来源。</p>
</td>
          </tr><tr>
            <td>Bad things that can happen to packets</td>
            <td align="left"><p>丢失、损坏、乱序、延迟、重复。</p>
</td>
          </tr><tr>
            <td>Bandwidth-Delay Product</td>
            <td align="left"><p>即 (bandwidth) * (propagation delay)，表示「填满管道」所需的 bit 数量。换句话说，如果 sender 以 link 的 bandwidth 发送数据，这就是已经发送但尚未收到的 bit 数量。</p>
</td>
          </tr><tr>
            <td>Bellman Ford Equation</td>
            <td align="left"><p>这个方程表示：你到某个 destination 的 shortest distance，是所有 neighbor 中「你到该 neighbor 的 cost 加上该 neighbor 到 destination 的 distance」的最小值。更具体地说，Node u 到给定 destination v 的 cost 是：d(u,v) = min(nbrs w) [c(u,w) + d(w,v)]。</p>
</td>
          </tr><tr>
            <td>Best Effort</td>
            <td align="left"><p>按需交付方式；系统除了会尽力而为之外，不提供任何性能保证。</p>
</td>
          </tr><tr>
            <td>Border Router</td>
            <td align="left"><p>连接到另一个 network 中 router 的 router。</p>
</td>
          </tr><tr>
            <td>Checksum</td>
            <td align="left"><p>用于检测 corruption 的数值，它基于 packet 的某一部分计算得到（具体取决于 protocol）。</p>
</td>
          </tr><tr>
            <td>CIDR</td>
            <td align="left"><p>Classless Interdomain Routing 的缩写。它把 IP address 和 network mask 结合起来，用于确定哪些 bit 是 network bit。相比原始 IP addressing scheme 或 classful addressing，它灵活得多。</p>
</td>
          </tr><tr>
            <td>Circuit Switching</td>
            <td align="left"><p>一种数据传输方法，其中 end system 会沿一条 path 预留 bandwidth，也就是建立一条 circuit，用于通信。不需要 packet。</p>
</td>
          </tr><tr>
            <td>Classful Addressing</td>
            <td align="left"><p>一种确定 IP address 中 network bit 和 host bit 的方案。我们处理三类地址：<strong>Class A</strong> address 以 0 开头，用前 8 bit 标识 network，后 24 bit 标识 host。<strong>Class B</strong> address 以 10 开头，用前 16 bit 标识 network，后 16 bit 标识 host。<strong>Class C</strong> address 以 110 开头，用前 24 bit 标识 network，后 8 bit 标识 host。</p>
</td>
          </tr><tr>
            <td>Control Plane</td>
            <td align="left"><p>指用于计算 routing table 和其他 forwarding information 的网络机制。</p>
</td>
          </tr><tr>
            <td>Convergence</td>
            <td align="left"><p>当所有参与方都拥有最新信息，并且在 network topology 不变的情况下，之后发送和接收的所有「update」都不会影响 routing state 时，我们说这个 algorithm 已经 converged。</p>
</td>
          </tr><tr>
            <td>Core/Backbone Router</td>
            <td align="left"><p>连接到其他 internal router 的 router。</p>
</td>
          </tr><tr>
            <td>Cost Table</td>
            <td align="left"><p>router 上的数据结构，包含到所有 neighbor 的 cost 集合。</p>
</td>
          </tr><tr>
            <td>Count-to-Infinity Problem</td>
            <td align="left"><p>由于使用 Distance Vector 时信息传播具有 asynchronous 特性而可能发生的一类 routing loop。它通常由 link down 引起：某个 router 原本使用一条已经 broken 的 path 到达某个 destination，却以为自己的 neighbor 仍然拥有到该 destination 的 valid path，于是在不知道这条 path 包含自己原先 broken path 的一部分时采用了它。两个 neighbor 会不断收到彼此的 update，并不断采用这条 broken path。</p>
</td>
          </tr><tr>
            <td>Cumulative ACK</td>
            <td align="left"><p>ACK 表示「直到这个 packet（或 byte）之前的所有 packet（或 byte）我都已经收到」。</p>
</td>
          </tr><tr>
            <td>Data Plane</td>
            <td align="left"><p>指用于转发 data 的网络机制。</p>
</td>
          </tr><tr>
            <td>Datacenters</td>
            <td align="left"><p>由大量机器组成的集合。</p>
</td>
          </tr><tr>
            <td>David Clark</td>
            <td align="left"><p>Internet 的无名英雄。他是 chief architect，并提出了 end-to-end principle。</p>
</td>
          </tr><tr>
            <td>Dead End</td>
            <td align="left"><p>当 packet 到达 router 或 switch，但 forwarding decision 没有得到 outgoing port，迫使 packet 被丢弃时，就出现 dead end。</p>
</td>
          </tr><tr>
            <td>Destination-Based Routing</td>
            <td align="left"><p>只依赖 destination 的 routing。从两个不同 source 到同一个 destination 的 path 一旦重叠，后续路径必须一致。</p>
</td>
          </tr><tr>
            <td>DHCP</td>
            <td align="left"><p>Dynamic Host Configuration Protocol。当 host 连接到 network 时，为它提供 IP address 的 protocol。host 连接到新 network 时，会发送 DHCP <strong>Discovery</strong> message，通知 DHCP server 自己需要一个 IP address。server 发送 <strong>Offer</strong> message，其中包含一个 offered IP address、subnet mask、first-hop router 的 IP address，以及 lease time。host 会发送与自己想接受的 offer 对应的 <strong>Request</strong>。server 用 <strong>Acknowledgement/Acceptance</strong> message 响应。所有 DHCP message 都是 broadcast 的。</p>
</td>
          </tr><tr>
            <td>Distance Vector Routing</td>
            <td align="left"><p>Distance vector routing 是一种 scalable 且 distributed 的 routing algorithm，其中每个 router 都维护一个 distance「vector」，以及到每个 destination 的 next-hop router。每个 node 会把自己的 shortest distance vector flood 给 neighbor；收到 vector 后，每个 router 使用 Bellman-Ford 更新自己的 vector。</p>
</td>
          </tr><tr>
            <td>DNS</td>
            <td align="left"><p>Domain Name Service，一个把 name 与 address 关联起来的系统，常用于在给定 name 时查找 host 的 address。</p>
</td>
          </tr><tr>
            <td>Dotted-quad notation</td>
            <td align="left"><p>一种 IPv4 address 记法，把地址写成 4 个数字，每个 byte 一个数字。例如 12.34.158.5。</p>
</td>
          </tr><tr>
            <td>Duplicate ACKs</td>
            <td align="left"><p>一连串确认同一批已接收数据的 cumulative ACK；这是 isolated packet loss 的信号，因为这些额外 ACK 表明 data 仍在被接收。</p>
</td>
          </tr><tr>
            <td>Edge Router</td>
            <td align="left"><p>连接 end host 的 router。</p>
</td>
          </tr><tr>
            <td>End to End Principle</td>
            <td align="left"><p>帮助判断某个功能应该在 network 中实现，还是只在 end host 中实现。本课程给出三种解释：<strong>Only-if-necessary</strong>：如果某个功能可以由 host 实现，就不要在 network 中实现。<strong>Only-if-sufficient</strong>：只有当某个功能可以在这一层完整实现，并且能减轻 host 负担时，才在这一层实现它。<strong>Only-if-useful</strong>：如果某个功能在 network 中实现可以提升性能，且不会给不需要它的 application 增加负担，就在 network 中实现它。</p>
</td>
          </tr><tr>
            <td>Enterprises</td>
            <td align="left"><p>公司和大学。</p>
</td>
          </tr><tr>
            <td>Fate Sharing</td>
            <td align="left"><p>把 state 存储在依赖该 state 的实体中，使该实体不会被其他 failure 影响。</p>
</td>
          </tr><tr>
            <td>First-hop router</td>
            <td align="left"><p>当 host 想把 packet 发送到 L2 network 之外的 destination 时，会先把 packet 发给的 router。</p>
</td>
          </tr><tr>
            <td>Flooding</td>
            <td align="left"><p>在本课程中，flooding 指在单个 switch 中，把 packet 从所有 port（incoming port 除外）发出去的行为。</p>
</td>
          </tr><tr>
            <td>Flow</td>
            <td align="left"><p>两个 process 之间的一串 packet。</p>
</td>
          </tr><tr>
            <td>Forwarding</td>
            <td align="left"><p>把 packet 朝 destination 发送。具体做法是读取 packet header 中的 address，在 routing state 中查找正确 output port，并从该 port 发送 packet。这是 router 内部的 local process，发生在 data plane 中，并且必须快速完成。</p>
</td>
          </tr><tr>
            <td>Forwarding Entry</td>
            <td align="left"><p>forwarding table 中的一条 entry，把一个 address 或一组 address 映射到 outgoing port。</p>
</td>
          </tr><tr>
            <td>Forwarding Table</td>
            <td align="left"><p>router 为自己计算的一张 table，用来指导 forwarding decision。forwarding table 使用 peer table 和 cost table 中的信息计算得到。</p>
</td>
          </tr><tr>
            <td>Fragmentation</td>
            <td align="left"><p>把一个 packet 分割成更小的 packet，以适配某条 link 的 maximum transmission unit（MTU）。</p>
</td>
          </tr><tr>
            <td>Full-information ACK</td>
            <td align="left"><p>描述目前为止所有已接收 data 的 ACK，可以表示为「直到这个 packet 之前的所有 packet 我都已经收到，此外还收到了这些额外 packet」。</p>
</td>
          </tr><tr>
            <td>Hard State</td>
            <td align="left"><p>处于「hard state」的系统不会让信息 timeout；它们假设一旦获得某些知识，这些知识就会一直真实有效，直到被明确告知相反信息。</p>
</td>
          </tr><tr>
            <td>Host bits</td>
            <td align="left"><p>IP address 中用于标识该 network 内 host 的部分。</p>
</td>
          </tr><tr>
            <td>Host/End System</td>
            <td align="left"><p>network 的 endpoint。这些实体负责生成 data packet，然后这些 packet 会在 network 中被 route。</p>
</td>
          </tr><tr>
            <td>Individual ACK</td>
            <td align="left"><p>表示「我收到了这个单独、特定 packet」的 ACK。</p>
</td>
          </tr><tr>
            <td>Internet</td>
            <td align="left"><p>连接所有联网计算设备的核心网络基础设施。</p>
</td>
          </tr><tr>
            <td>IP Address</td>
            <td align="left"><p>Layer 3 使用的 addressing scheme。</p>
</td>
          </tr><tr>
            <td>IPv4</td>
            <td align="left"><p>IP protocol 的第 4 版。</p>
</td>
          </tr><tr>
            <td>ISP (Internet Service Provider)/ISP Network</td>
            <td align="left"><p>由 packet switch 和 communication link 组成、为 end system 提供 network access 的 network。</p>
</td>
          </tr><tr>
            <td>LAN</td>
            <td align="left"><p>Local area network，一个覆盖较小地理范围的 L2 network，例如一户家庭。</p>
</td>
          </tr><tr>
            <td>Layering</td>
            <td align="left"><p>一般来说，layering 是把复杂系统拆分成彼此构建在对方之上或彼此依赖的独立层级。在 Internet 语境中，它指一组特定 layer（physical = L1，datalink = L2，internetworking = L3，transport = L4），每一层只与正上方或正下方的 layer 交互。</p>
</td>
          </tr><tr>
            <td>Layers</td>
            <td align="left"><p><strong>Application</strong>（对 app 的 network support）。4：<strong>Transport</strong>（可靠/不可靠的 end-to-end delivery）。3：<strong>Network</strong>（全局 best-effort delivery）。2：<strong>Datalink</strong>（本地 best-effort delivery）。1：<strong>Physical</strong>（bit 通过某种 medium 传输）。</p>
</td>
          </tr><tr>
            <td>Learning Switches</td>
            <td align="left"><p>通常在 L2 与 spanning tree protocol 结合使用。Learning switch 维护一张 forwarding table，把 destination 映射到 output link。它们从 packet 的「source」field 学习。当 packet 到达时，switch 检查 destination 是否在自己的 table 中。如果在，就沿对应 link 转发 packet。如果不在，就 flood 这个 packet。</p>
</td>
          </tr><tr>
            <td>Linecard</td>
            <td align="left"><p>router 中用于接收/发送 packet 的硬件部件。它们会更新各种 field（checksum、TTL 等）并选择 outgoing port。</p>
</td>
          </tr><tr>
            <td>Link</td>
            <td align="left"><p>连接 router 的物理基础设施组件。</p>
</td>
          </tr><tr>
            <td>Link-State Routing</td>
            <td align="left"><p>在 Link-State routing 中，每个 router 会把自己的 link state 发送给 network 中所有其他 router（使用 protocol-specific broadcast mechanism）。这样，每个 router 都会学到完整的 network graph。然后，每个 router 使用某种有效 algorithm（例如 Dijkstra）计算自己到所有其他 node 的 least-cost path。</p>
</td>
          </tr><tr>
            <td>Loop</td>
            <td align="left"><p>packet 永远在同一组 node 之间循环。</p>
</td>
          </tr><tr>
            <td>LPM</td>
            <td align="left"><p>Longest-prefix-match：当一个 IP Address 匹配多个 prefix 时，选择最长的匹配。（可以理解为沿 prefix tree 遍历，直到 address「掉出」树。）</p>
</td>
          </tr><tr>
            <td>MAC Address</td>
            <td align="left"><p>用于 L2 routing。MAC Address 是一个 48 bit number，写入 host 和 router 的 network interface 中。MAC address 编码在存储于 Read-Only memory 的物理硬件中，因此是永久 identifier。</p>
</td>
          </tr><tr>
            <td>Maximum Transmission Unit (MTU)</td>
            <td align="left"><p>一条 link 能作为单个 unit 传输的最大 bit 数，也就是可以跨 link 发送的最大 packet size。</p>
</td>
          </tr><tr>
            <td>Modularity</td>
            <td align="left"><p>把一个问题分解为 task 或 abstraction。这会导向 layering 的设计原则。</p>
</td>
          </tr><tr>
            <td>Multihoming</td>
            <td align="left"><p>把一个 host 连接到多个不同 network，使得某个 parent network 离线时，该 host 仍然可达。它会阻碍 aggregation。</p>
</td>
          </tr><tr>
            <td>NACK</td>
            <td align="left"><p>「Non-acknowledgement」message，即「我没有收到这份 data（我原本期望收到它）」。</p>
</td>
          </tr><tr>
            <td>Network</td>
            <td align="left"><p>非正式使用时，它指由 end system、router/switch 和 link 组成，并能在 host 之间传输 data 的系统（例如 Berkeley 的 campus network）。正式使用时，它指共享同一个 IPv4 network address 的一组 network element，并且常与 subnet 同义使用。</p>
</td>
          </tr><tr>
            <td>Network Address</td>
            <td align="left"><p>IP address 中指代 network（或 subnet）而不是 host 的组成部分。</p>
</td>
          </tr><tr>
            <td>Network bits</td>
            <td align="left"><p>IP address 中用于标识 host 所在 network 的部分。</p>
</td>
          </tr><tr>
            <td>Network mask</td>
            <td align="left"><p>一串类似 IP address 的 bit，用来标识 IP Address 中的 network 部分。它由固定数量的 1（每个 network address bit 一个 1）后接全 0 构成。</p>
</td>
          </tr><tr>
            <td>Network Name</td>
            <td align="left"><p>host 的 name（对人类友好的东西）。</p>
</td>
          </tr><tr>
            <td>Network Stack</td>
            <td align="left"><p>host 上的 networking software。它复制了一些 router 中也有的功能，并添加额外功能（例如 socket、TCP header 等）。</p>
</td>
          </tr><tr>
            <td>Packet</td>
            <td align="left"><p>一包 bit。它由两部分组成：<strong>Header</strong>，包含让 network 和 network stack 做 decision 的有意义信息；<strong>Body</strong>，包含 payload。例如 file、image、application header 等。</p>
</td>
          </tr><tr>
            <td>Packet Switching</td>
            <td align="left"><p>一种数据传输方法，其中 data 被切分为 packet，router/switch 会检查每个收到 packet 的 header，并独立服务每个 packet。</p>
</td>
          </tr><tr>
            <td>Path Vector Routing</td>
            <td align="left"><p>类似 distance vector routing，但向 neighbor advertise 时，不是发送自己的 shortest distance，而是发送自己到 destination 的 path。</p>
</td>
          </tr><tr>
            <td>Payload</td>
            <td align="left"><p>packet 中携带的 data。</p>
</td>
          </tr><tr>
            <td>Peer Table</td>
            <td align="left"><p>router 上的数据结构，包含该 router 的各个「peer」或「neighbor」发送给它的信息副本。</p>
</td>
          </tr><tr>
            <td>Poison Reverse</td>
            <td align="left"><p>一种试图缓解 count-to-infinity problem 的方法：对某个你在通往 destination 的 path 上使用的 neighbor，不 advertise 自己能够到达该 destination（也就是 advertise distance 为 infinity）。例如，router A 创建一份临时 vector 副本发给 router C，其中对所有 router A 使用 link AC 的 destination，都 advertise distance 为 infinity。</p>
</td>
          </tr><tr>
            <td>Port (Logical)</td>
            <td align="left"><p>OS 分配给 socket、用于标识该 socket 的 number。</p>
</td>
          </tr><tr>
            <td>Port (Router)</td>
            <td align="left"><p>把 router 通过 link 连接到另一个 router 的物理 port。</p>
</td>
          </tr><tr>
            <td>Prefix Aggregation</td>
            <td align="left"><p>使用共同 prefix 把 routing table entry 合并为一条 entry（例如把 101 和 100 合并为 10*）。</p>
</td>
          </tr><tr>
            <td>Prefix Tree</td>
            <td align="left"><p>表示 IP address lookup 中 matching bit 的 binary tree（也就是 lookup table 的遍历方式）。</p>
</td>
          </tr><tr>
            <td>Reliability (see Robustness)</td>
            <td align="left"><p>两种解释：1）network 能从 failure 中快速恢复，让两个未被 partition 的 endpoint 能够通信。2）network failure 不会干扰 endpoint semantics。</p>
</td>
          </tr><tr>
            <td>Reliable Delivery</td>
            <td align="left"><p>在 best-effort delivery 之上构建可靠的 transport service。</p>
</td>
          </tr><tr>
            <td>Reliable Transport</td>
            <td align="left"><p>一个 transport mechanism 当且仅当满足以下条件时是「reliable」的：（a）重发所有 dropped 或 corrupted packet；（b）尝试取得 progress。</p>
</td>
          </tr><tr>
            <td>Resource Accountability</td>
            <td align="left"><p>知道谁正在使用哪些 resource（bandwidth）的能力，从而可以让他们对此负责。这是 Internet architecture 的一个失败之处。</p>
</td>
          </tr><tr>
            <td>Robustness (see Reliability)</td>
            <td align="left"><p>只要 network 没有被 partition，两个 host 最终应该能够通信，并且 failure 永远不应该干扰 application semantics。</p>
</td>
          </tr><tr>
            <td>Route Aggregation</td>
            <td align="left"><p>不为每台 host 保留一条 forwarding entry，而是为一组拥有相同 prefix、且都从同一个 port 发出的 host 保留一条 entry。</p>
</td>
          </tr><tr>
            <td>Route Poisoning</td>
            <td align="left"><p>一种缓解 network inconsistency 的过程：当 A 和 B 之间的 link down 时，router B 应该向所有 neighbor advertise 自己不再拥有到 router A 的 link（也就是 B advertise distance 为 infinity），以表示自己不能再到达 A。</p>
</td>
          </tr><tr>
            <td>Routing</td>
            <td align="left"><p>把 packet 从 source 引导到 destination（可以用许多方式完成，见 link-state、distance vector、spanning tree 等）。这是一个天然的 global process，因此必须 scale。它发生在 control plane 中，可以较慢完成。</p>
</td>
          </tr><tr>
            <td>Routing Table</td>
            <td align="left"><p>类似 Forwarding Table，但可以指 router 拥有的全部信息（包括来自其他 peer 的信息），而不只是最佳 forwarding entry。</p>
</td>
          </tr><tr>
            <td>Slash notation</td>
            <td align="left"><p>一种谈论 subnet 的 notation。形式类似 1.2.0.0/10，其中 1.2.0.0 的前 10 bit 是 subnet prefix。</p>
</td>
          </tr><tr>
            <td>Sliding window</td>
            <td align="left"><p>允许处于 in flight 状态且尚未被 ack 的 packet 的有限数量；出于效率目的，在达到这个数量前我们可以继续发送更多 packet。</p>
</td>
          </tr><tr>
            <td>Socket</td>
            <td align="left"><p>OS 用来把 process 连接到 networking stack 的机制。</p>
</td>
          </tr><tr>
            <td>Soft State</td>
            <td align="left"><p>允许存储的知识「time out」的概念，前提是假设这些知识可能已经改变、不再 valid 等。运行在 soft state 下的系统会周期性「忘记」自己知道的内容，并需要通过再次请求信息、等待新 message 和新 information 等方式重新学习。带有 lease time 的 DHCP offer、会 timeout 的 cached ARP entry，以及 Distance-Vector Routing 中的 periodic message，都是 soft-state 的例子。</p>
</td>
          </tr><tr>
            <td>Spanning Tree Protocol</td>
            <td align="left"><p>一种 distributed protocol，其中 switch 会从 node X 发送格式为 (Y, d, X) 的 message，提议 Y 作为 root，并 advertise 自己到 Y 的 distance 为 d。这个 protocol 会识别 ID 最低的 node，并以该 node 为 root 构建一棵 spanning tree。</p>
</td>
          </tr><tr>
            <td>Split Horizon</td>
            <td align="left"><p>Split horizon 提供与 poison reverse 相同的功能，但用不同方式表达信息。Split Horizon 用于 full update 的语境中，router 不会把任何到 destination X 的 route advertise 给它用来到达 destination X 的 neighbor。</p>
</td>
          </tr><tr>
            <td>Statistical Multiplexing</td>
            <td align="left"><p>各个 flow 最大速率之和，大于把这些 flow 合并后再寻找最大值所得的结果。</p>
</td>
          </tr><tr>
            <td>Subnet</td>
            <td align="left"><p>在本课程中，我们用这个术语指 network 的一部分；它由 L2 连接，并共享相同 network address。</p>
</td>
          </tr><tr>
            <td>Time to Live (TTL)</td>
            <td align="left"><p>在 IP 中，它指 packet 在被丢弃前可以经过的 hop 数，这有助于防止 loop。更一般地说，TTL 指某个东西到期前的时间（例如 cached entry）。</p>
</td>
          </tr><tr>
            <td>Valid Routing State</td>
            <td align="left"><p>当且仅当不存在 loop 且不存在 dead end（假设没有 packet replication）时，routing state 是 valid 的。如果存在 packet replication，则条件变为至少一个 replica 不会遇到 dead end。</p>
</td>
          </tr><tr>
            <td>WAN</td>
            <td align="left"><p>它可以指任意 L3 network（也就是说，不只是 local area network），也可以指跨越较大地理距离的 network（也就是说，不是 datacenter）。</p>
</td>
          </tr></tbody>
    </table>
