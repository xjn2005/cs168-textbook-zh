---
title: "NAT: Network Address Translation"
parent: End-to-End
nav_order: 5
layout: page-with-toc
---

# NAT锛歂etwork Address Translation

## 鍔ㄦ満锛欼Pv4 鍦板潃鑰楀敖

鍥炲繂涓€涓嬶紝鎴戜滑鍙湁 $2^{32}$ 涓笉鍚岀殑 IPv4 鍦板潃锛岃繖涓嶈冻浠ョ粰 Internet 涓婄殑姣忓彴 host 閮藉垎閰嶅湴鍧€銆傛垜浠凡缁忕湅鍒帮紝IPv6 鏄В鍐?IPv4 鍦板潃鑰楀敖闂鐨勭ǔ鍋ユ柟妗堬紝浣?IPv6 鐨勯噰鐢ㄤ竴鐩寸浉褰撶紦鎱€?
涓庢鍚屾椂锛屼负浜嗚妭鐪佸湴鍧€锛屽洖蹇嗕竴涓嬶紝IANA 鍒嗛厤浜?RFC 1918 涓壒娈婄殑 private IP address 鑼冨洿锛屼换浣曚笉闇€瑕?Internet 鍦板潃鐨勭綉缁滈兘鍙互浣跨敤瀹冧滑锛?92.168.0.0/16銆?0.0.0.0/8 鍜?172.16.0.0/12銆備簨瀹炶瘉鏄庯紝杩欎簺鍦板潃涔熺粡甯哥敤鍦ㄤ綘鐨勫搴綉缁滀腑锛岃繖鏍蜂綘鑷繁鐨勪釜浜鸿澶囧氨涓嶉渶瑕佹嫢鏈夊敮涓€ IP 鍦板潃銆備絾鏄紝浣犵‘瀹為渶瑕?Internet access锛岄偅涔堜綘鎬庢牱鎵嶈兘浣跨敤 private IP address 鍛紵


## NAT锛氭蹇?
鍦?NAT 涓紝鐩爣鏄敤涓€涓?public IP address 浠ｈ〃 local network 涓殑璁稿 host銆傛妧宸ф槸鍦ㄥ彂閫?message 涔嬪墠锛岃 gateway router 鎶?private IP address 杞崲鎴愯繖涓崟涓€鐨?public address銆傜劧鍚庯紝瀵逛簬 incoming reply锛宺outer 鍐嶆妸 public address 杞崲鍥?private address銆?
Alice銆丅ob 鍜?Chuck 閮藉湪 Joe's Tire Shop 宸ヤ綔銆備粬浠嫢鏈?private IP address A銆丅 鍜?C锛岃繖浜涘湴鍧€涓嶈兘鍦ㄥ箍鍩?Internet 涓婁娇鐢紝鍥犱负瀹冧滑涓嶆槸鍞竴鐨勩€傜浉鍙嶏紝Joe's Tire Shop 涓殑鎵€鏈変汉蹇呴』鍏变韩涓€涓?public IP address锛岃繖鏄粬浠敮涓€鎷ユ湁鐨勩€佸叏灞€鍞竴涓斿鐣岃兘鐞嗚В鐨?IP 鍦板潃銆?
<img width="900px" src="/assets/end-to-end/5-056-nat1.png">

Alice 鎯冲悜涓€涓?public IP address 涓?S 鐨勫閮?public server 鍙戦€?message銆傚ス鍙戦€佷竴涓?packet锛屼笂闈㈠啓鐫€銆孎rom: A, To: S銆嶃€傚鏋滄垜浠湸绱犲湴鍙戦€佽繖涓?packet锛孲 灏嗘棤娉曞彂閫?reply锛屽洜涓?A 鏄?private IP address銆?
<img width="900px" src="/assets/end-to-end/5-057-nat2.png">

鐩稿弽锛屽綋 packet 鍒拌揪 gateway router 鏃讹紝router 浼氶噸鍐?header锛岃瀹冨彉鎴愩€孎rom: R1, To: S銆嶃€俽outer 杩樹細鍋氫竴鏉¤褰曪細濡傛灉鎴戞敹鍒版潵鑷?S 鐨勪换浣?reply锛屽畠浠簲璇ュ彂缁?A銆?
<img width="900px" src="/assets/end-to-end/5-058-nat3.png">

鐜板湪锛屽綋 S 鏀跺埌 packet 鏃讹紝瀹冨彲浠ュ悜 public address R1 鍙戦€?reply锛氥€孎rom: S, To: R1銆嶃€傚綋 gateway router R1 鏀跺埌 reply 鏃讹紝瀹冧細妫€鏌ヨ嚜宸辩殑璁板綍锛屽苟鎶?header 閲嶅啓涓恒€孎rom: S, To: A銆嶃€傜劧鍚庯紝杩欎釜 packet 琚彂閫佸洖 A銆?
<img width="900px" src="/assets/end-to-end/5-059-nat4.png">

鐜板湪锛孉lice銆丅ob 鍜?Chuck 閮藉彲浠ュ彂閫?outgoing packet銆傚綋 router 鏀跺埌涓€涓?packet 鏃讹紝瀹冨繀椤昏浣?external destination 鍜?internal sender 涔嬮棿鐨?mapping銆傦紙銆孊 鍒氬垰鍚?N 鍙戦€佷簡涓€涓?packet锛屾墍浠ユ潵鑷?N 鐨勪换浣?reply 閮藉簲璇ュ彂鍥炵粰 B銆傘€嶏級

濡傛灉 Alice 鍜?Bob 閮芥兂鍜?S 閫氫俊锛屽氨浼氬嚭鐜颁竴涓棶棰樸€?
<img width="900px" src="/assets/end-to-end/5-060-nat5.png">

鐜板湪锛屽鏋滄潵鑷?S 鐨?reply 鍒拌揪锛屽氨浼氫骇鐢熸涔夈€俽outer 搴旇鎶婅繖涓?reply 鍙戠粰 A 杩樻槸 B锛?
<img width="900px" src="/assets/end-to-end/5-061-nat6.png">

鎴戜滑鍙互鐢?Layer 4 鐨?logical port 瑙ｅ喅杩欎釜闂銆侫lice 鐨?connection 鍐欑潃锛氥€孎rom: A, Port 50000, To: S, Port 80銆傘€峳outer 鍍忎箣鍓嶄竴鏍锋妸瀹冮噸鍐欐垚銆孎rom: R1, Port 50000, To: S, Port 80銆傘€嶇幇鍦ㄨ褰曚細鍐欑潃锛氬鏋滄垜鏀跺埌鏉ヨ嚜 S銆丳ort 80锛屽彂寰€ R1銆丳ort 50000 鐨勪换浣?reply锛屽畠搴旇鍙戠粰 A銆?
<img width="900px" src="/assets/end-to-end/5-062-nat7.png">

Bob 鍙互鍒涘缓涓€涓崟鐙殑 connection锛屽啓鐫€锛氥€孎rom B, Port 60000, To: S, Port 80銆傘€峳outer 鍍忎箣鍓嶄竴鏍锋妸瀹冮噸鍐欐垚銆孎rom: R1, Port 60000, To: S, Port 80銆傘€嶈繖鏉?connection 鐨勮褰曞啓鐫€锛氬鏋滄垜鏀跺埌鏉ヨ嚜 S銆丳ort 80锛屽彂寰€ R1銆丳ort 60000 鐨勪换浣?reply锛屽畠搴旇鍙戠粰 B銆?
<img width="900px" src="/assets/end-to-end/5-063-nat8.png">

鏇翠竴鑸湴璇达紝router 鐜板湪鐢?source IP銆乨estination IP銆乸rotocol銆乻ource port 鍜?destination port 缁勬垚鐨?5-tuple 鏉ヨ窡韪?connection銆傚綋 router 鏀跺埌 outgoing packet 鏃讹紝瀹冩妸 private source IP 鏀规垚 public source IP锛屽苟璁板綍杩欎釜 5-tuple銆傜劧鍚庯紝褰?router 鏀跺埌 incoming packet 鏃讹紝瀹冩煡鎵捐繖涓?packet 灞炰簬鍝釜 connection锛屽苟鎶?packet 鍙戦€佺粰鍚堥€傜殑 client锛堜娇鐢ㄥ畠浠殑 private IP锛夈€?
<img width="900px" src="/assets/end-to-end/5-064-nat9.png">


## 閲嶅啓 Client Port Number

鎴戜滑杩樻湁鏈€鍚庝竴涓棶棰橈細濡傛灉 Alice 鍜?Bob 娌℃湁閫夋嫨 Port 50000 鍜?Port 60000锛岃€屾槸閮介€夋嫨浜嗗悓涓€涓?port number锛堜緥濡?Port 50000锛夛紝浼氭€庢牱锛?
<img width="900px" src="/assets/end-to-end/5-065-nat10.png">

鐜板湪锛宺outer 璁颁綇浜嗕袱鏉?connection锛氾紙A Port 50000 to S Port 80锛夊拰锛圔 Port 50000 to S Port 80锛夈€傚鏋?router 鏀跺埌涓€涓?incoming packet銆孎rom: S, Port 80, To: R1 Port 50000銆嶏紝灏辨棤娉曞垽鏂繖涓?packet 鏉ヨ嚜 A 鐨?connection 杩樻槸 B 鐨?connection銆?
<img width="900px" src="/assets/end-to-end/5-066-nat11.png">

鎴戜滑瑕佸仛鐨勬渶鍚庝竴涓慨姝ｏ紝鏄篃鍏佽 router 閲嶅啓 port number銆傚綋 Bob 鍙戦€併€孎rom: B, Port 50000, To: S, Port 80銆嶆椂锛宺outer 鎰忚瘑鍒板凡缁忔湁浜轰娇鐢?Port 50000 鍒?S Port 80 鐨?connection銆傚洜姝わ紝router 涓?Bob 缂栭€犱竴涓€宖ake銆峱ort number锛堣繖閲屼娇鐢?60000锛夛紝骞跺悓鏃堕噸鍐?source IP 鍜?source port锛屽緱鍒帮細銆孎rom: R1, Port 60000, To: S, Port 80銆傘€?
鍜屼箣鍓嶄竴鏍凤紝router 璁颁綇 active connection锛圓 Port 50000 to S Port 80锛夛紝浣嗗 Bob锛宺outer 杩樹細棰濆璁板綍杩欎釜 fake port number锛氾紙B Port 50000, faked as 60000, to S Port 80锛夈€?
<img width="900px" src="/assets/end-to-end/5-067-nat12.png">

鐜板湪锛屽鏋?router 鏀跺埌 incoming packet銆孎rom: S, Port 80, To: R1, Port 50000銆嶏紝瀹冧竴瀹氭槸鍙戠粰 Alice 鐨勩€傜浉鍙嶏紝甯︽湁 fake port number 鐨?incoming packet锛屼緥濡傘€孎rom: S, Port 80, To: R1, Port 60000銆嶏紝涓€瀹氭槸鍙戠粰 Bob 鐨勩€?
<img width="900px" src="/assets/end-to-end/5-068-nat13.png">

娉ㄦ剰锛孊ob 骞朵笉鐭ラ亾 router 姝ｅ湪淇敼浠栫殑 port number銆傚綋 router 鎶婅繖涓?packet 杞彂鍥?Bob 鏃讹紝fake port number 蹇呴』鏀瑰洖鍘熷 port number銆傘€孎rom: S, Port 80, To: R1, Port 60000銆嶅繀椤昏閲嶅啓涓哄彂缁?Bob 鍘熸潵 port 鐨?packet銆傛洿涓€鑸湴璇达紝浠讳綍 private client 閮戒笉搴旇闇€瑕佺煡閬撴垨鍏冲績鑷繁鐨?packet 琚噸鍐欍€俽outer 搴旇缁欏畠浠竴绉嶅够瑙夛細瀹冧滑姝ｅ湪浣跨敤鑷繁鐨?private IP address 鍜岃嚜宸遍€夋嫨鐨勪换鎰?port 鏉ュ彂閫佸拰鎺ユ敹 packet銆?

## NAT锛氬疄鐜?
褰撳搴?router 绗竴娆¤繛鎺ュ埌 ISP 鏃讹紝瀹冨彲浠ヨ繍琛?DHCP 鏉ユ帴鏀朵竴涓?IP 鍦板潃銆傦紙鍓嶉潰鎴戜滑璁ㄨ杩?host 杩愯 DHCP锛屼絾 router 涔熷彲浠ヨ繍琛?DHCP銆傦級ISP 鐨?DHCP server 浼氬洖澶嶅苟缁欏搴?router 鍒嗛厤涓€涓?IP 鍦板潃銆傝繖灏辨槸杩欎釜 router 鐨勫搴綉缁滀腑鎵€鏈?host 灏嗗叡浜殑鍗曚竴 public address銆?
<img width="800px" src="/assets/end-to-end/5-069-nat-dhcp.png">

NAT 鏈夊嚑绉嶄笉鍚屾ā寮忋€傛垜浠垰鎵嶇湅鍒扮殑妯″紡绉颁负 **Port Address Translation锛圥AT锛?*锛屽畠璁╂垜浠兘澶熷紩鍏ュ墠闈㈢湅鍒扮殑 fake port number銆侾AT 妯″紡瑕佹眰 router 鐭ラ亾 Layer 4 protocol锛岃繖鏍峰畠浠墠鑳借В鏋?packet銆佽窡韪?connection 骞堕噸鍐?header銆?
PAT 鏄渶澶嶆潅銆佷篃鏈€骞挎硾浣跨敤鐨?NAT 妯″紡锛屼絾涔熷瓨鍦ㄦ洿绠€鍗曠殑涓€瀵逛竴 address translation NAT 妯″紡銆傚鏋滄瘡鍙?host 瀹為檯涓婇兘鏈夎嚜宸辩殑 IP 鍦板潃锛屼絾瀹冧滑浠?private address 鍙戦€?packet锛岄偅涔?router 鍙互鍙仛涓€瀵逛竴杞崲锛屾妸 10.0.0.1锛坧rivate锛夋槧灏勫埌 42.0.2.1锛坧ublic锛夛紝鎶?10.0.0.2锛坧rivate锛夋槧灏勫埌 42.0.2.2锛坧ublic锛夛紝渚濇绫绘帹銆傝繖绉嶆洿绠€鍗曠殑妯″紡涓嶈兘閫氳繃鎶婂鍙?host 闅愯棌鍦ㄥ崟涓?public address 鍚庨潰鏉ヨ妭鐪?IP 鍦板潃锛屼絾鍦ㄥ叾浠栧満鏅腑浠嶇劧鏈夌敤銆?
<img width="400px" src="/assets/end-to-end/5-070-simpler-nat.png">


## NAT 鐢ㄥ湪鍝噷锛?
NAT 澧炲姞浜?router 杞彂 packet 鐨勫鏉傛€с€俽outer 鐜板湪涓嶄粎瑕佽В鏋?Layer 3 header锛岃繕蹇呴』鑳藉瑙ｆ瀽 Layer 4 header銆傚彟澶栵紝router 蹇呴』鑳藉閲嶅啓 Layer 3 鍜?Layer 4 header銆傛渶鍚庯紝router 蹇呴』缁存姢涓€寮?connection state table锛岃窡韪墍鏈夌粡杩?router 鐨?flow銆傛墍鏈夎繖浜涘姛鑳介兘浼氬鍔犺浆鍙戞瘡涓?packet 鎵€闇€鐨?CPU cycle 鏁伴噺锛屼篃浼氬鍔?router 涓婃瘡涓?flow 鎵€闇€鐨勫唴瀛橀噺銆?
鍥犱负 NAT 澧炲姞浜?router 澶嶆潅鎬э紝鎵€浠ュ畠浼氬敖鍙兘闈犺繎缃戠粶杈圭紭鎵ц锛屼互闄愬埗缁忚繃 router 鐨?flow 鏁伴噺銆傚湪浣犵殑瀹跺涵 router 涓婅繍琛?NAT 鏄釜濂戒富鎰忥紝鍥犱负浣犲閲屼笉浼氭湁澶璁惧鎶?connection 鍙戣繃瀹跺涵 router銆傜浉姣斾箣涓嬶紝鍦ㄩ珮鎬ц兘 datacenter router 涓婅繍琛?NAT 浼氭槸涓潖涓绘剰銆?
瀹炶返涓紝鍗充娇鍦ㄤ粖澶╋紝灏忚妯?NAT 涔熺敤浜庡嚑涔庢瘡涓釜浜猴紙瀹跺涵/鍔炲叕瀹わ級IPv4 缃戠粶銆傞殢鐫€ IPv4 鍦板潃鑰楀敖锛孖SP 鏃犳硶缁欐瘡涓?customer锛堜篃灏辨槸姣忎釜瀹跺涵 router锛変竴涓?public address銆傚洜姝わ紝ISP network 鏈韩涔熷繀椤昏繍琛屾洿澶嶆潅鐨?NAT 鐗堟湰锛岀О涓?Carrier Grade NAT锛圕GNAT锛夈€傝繖绉?NAT 閮ㄧ讲鍦ㄧ綉缁滄洿娣卞锛屽苟瑕佹眰 router 璺熻釜澶氬緱澶氱殑 connection銆?
娉ㄦ剰锛屾垜浠€氬父涓嶅 IPv6 浣跨敤 NAT锛屽洜涓?IPv6 鍦板潃瓒冲澶氾紝鍙互缁欎笘鐣屼笂姣忓彴璁＄畻鏈哄垎閰嶄竴涓敮涓€鐨?public address銆?

## Inbound Connection

鍒扮洰鍓嶄负姝紝鎴戜滑涓€鐩村亣璁?connection 鎬绘槸鐢辨嫢鏈?private IP address 鐨?client 鍙戣捣銆傛崲鍙ヨ瘽璇达紝绗竴涓?packet 鎬绘槸 outgoing锛屼粠 client 鍙戝線 server銆傝繖涓庡ぇ澶氭暟瀹跺涵缃戠粶鐨勮繍琛屾柟寮忎竴鑷淬€傚綋浣犲湪 browser 涓姞杞界綉绔欐椂锛屼綘灏辨槸鍙戣捣 connection 鐨?client銆傞€氬父涓嶄細鏄叾浠栦汉璇曞浘杩炴帴鍒颁綘銆?
浣嗘槸锛屽鏋滀綘姝ｅ湪杩愯涓€涓?server锛屽苟涓旂‘瀹炲笇鏈涘閮ㄤ笘鐣岀殑浜鸿兘澶熶富鍔ㄨ繛鎺ュ埌杩欎釜 server锛屼細鎬庢牱锛熷閮ㄧ敤鎴蜂笉鑳藉悜 private IP address 鍙戦€?packet銆備粬浠彲浠ュ皾璇曞悜 router 鐨?IP 鍦板潃鍙戦€?packet锛屼絾濡傛灉 router 鏀跺埌绫讳技銆孎rom: outside user, To: R1, Port 28銆嶇殑 packet锛宺outer 涓嶇煡閬撳簲璇ユ妸杩欎釜 packet 杞彂缁欏摢涓?private client銆傝繖鏄柊 connection 鐨勭涓€涓?packet锛屽洜姝?router 鐨勮〃涓繕娌℃湁鍏充簬杩欎釜 connection 鐨勪俊鎭€?
<img width="900px" src="/assets/end-to-end/5-071-inbound-nat.png">

涓轰簡鍏佽 inbound connection锛屾墽琛?NAT 鐨?router 闇€瑕佷竴寮?**port mapping table**銆傜綉缁滃唴閮ㄤ笖鍙湁 private IP address 鐨?Alice 鍛婅瘔 router锛氭垜瑕佽繍琛屼竴涓柊鐨?server锛屽苟鍦?Port 28 涓婄洃鍚?request銆傜幇鍦紝濡傛灉 router 鐪嬪埌鏌愪釜鏉ヨ嚜澶栭儴鐢ㄦ埛銆佸彂寰€ R1銆丳ort 28 鐨?packet锛宺outer 灏辩煡閬撳簲璇ユ妸杩欎釜 packet 杞彂缁?Alice銆?
port mapping table 涓殑 entry 鍙兘闇€瑕佹墜鍔ㄦ寚瀹氾紙渚嬪 Alice 鎵嬪姩閰嶇疆 router锛夈€俇PnP锛圲niversal Plug-n-Play锛夊拰 NAT-PMP锛圢AT Port Mapping Protocol锛夌瓑 dynamic protocol 鍏佽鍔ㄦ€侀厤缃?open port銆傝繖浜?protocol 鏈夋椂琚湪绾挎父鎴忕瓑闇€瑕?inbound connection 鐨?application 浣跨敤銆?

## NAT 鐨勫畨鍏ㄥ惈涔?
NAT 鎵撶牬浜?end-to-end principle銆傚埌鐩墠涓烘锛屾垜浠杩囧湪 Layer 3 涓紝Internet 涓婁换浣曚汉閮藉彲浠ュ埌杈句换浣曞叾浠栦汉銆傜劧鑰岋紝鐢变簬 NAT 榛樿涓嶅厑璁?inbound connection锛屽搴綉缁滀腑鍙湁 private IP address 骞跺叡浜?public IP address 鐨勭敤鎴锋棤娉曡鑷姩鍒拌揪銆備粬浠繀椤诲厛閰嶇疆 router锛屾墠鑳芥帴鍙?inbound packet銆?
NAT 鏈変竴涓€ц川锛氶粯璁や笉鍏佽 inbound connection銆傝繖鍙互琚湅浣滀竴绉嶅畨鍏ㄧ壒鎬э紝涓嶈繃瀹冩洿鍍忓壇浣滅敤锛岃€屼笉鏄湁鎰忚璁＄殑瀹夊叏鍔熻兘銆侼AT 浼氶粯璁ら樆姝?inbound connection锛岃繖鍙兘鏈夊姪浜庨樆姝㈡敾鍑昏€呭皾璇曡繛鎺ョ綉缁滃唴閮ㄧ殑 host銆傝繖绉嶈涓哄疄闄呬笂鍜?firewall 寰堢浉浼硷紙鏇村淇℃伅瑙?UC Berkeley CS 161 notes锛夛紝firewall 涔熺粡甯搁粯璁ら樆姝?inbound connection銆傝瘽铏藉姝わ紝杩欎富瑕佹槸宸у悎锛屾墍浠?NAT 骞舵病鏈夊疄鐜颁竴涓湁鍘熷垯鐨?security policy锛屼篃涓嶅簲璇ヨ璁や负鏄墷涓嶅彲鐮寸殑闃插尽銆?
NAT 杩樻湁涓€涓壇浣滅敤锛氬畠鍙互甯姪淇濇姢 client privacy銆傚悓鏍凤紝杩欏苟涓嶆槸鐪熸鏈夋剰璁捐鐨勫畨鍏ㄧ壒鎬с€傚洜涓?router 浼氶噸鍐?client 鐨?IP 鍦板潃锛屾墍浠ュ綋 server 鏀跺埌 packet 鏃讹紝瀹冨苟涓嶇煡閬撳師濮?sender 鐨勮韩浠斤紙鍙兘鏄?Alice銆丅ob 鎴?Chuck锛夈€?
鐩告瘮涔嬩笅锛屽鏋滄垜浠笉浣跨敤 NAT锛宻erver 鍙互鐭ラ亾 sender 鐨勭‘鍒囪韩浠姐€傚彟澶栵紝濡傛灉鎴戜滑涓嶄娇鐢?NAT 骞朵娇鐢?IPv6锛宻erver 鍙兘鑳藉鐭ラ亾 sender 姝ｅ湪浣跨敤鐨勫叿浣撹绠楁満锛屽洜涓?IPv6 鍦板潃鏈夋椂浼氱敤 MAC address 鑷姩閰嶇疆锛堟妸 MAC address bit 澶嶅埗鍒?IP 鍦板潃涓級銆傚鏋滄垜浠娇鐢?IPv6 涓斾粛鐒跺笇鏈涗繚鎶?client privacy锛屼篃瀛樺湪涓€浜涙浛浠ｆ柟妗堬紝渚嬪 IPv6 temporary/privacy address銆?
