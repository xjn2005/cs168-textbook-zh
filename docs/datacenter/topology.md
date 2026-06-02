---
title: Topologies
parent: Datacenters
nav_order: 1
layout: page-with-toc
---

# Datacenter Topology

## 浠€涔堟槸 Datacenter锛?
鍒扮洰鍓嶄负姝紝鍦ㄦ垜浠殑 Internet 妯″瀷涓紝鎴戜滑灞曠ず鐨勬槸 end host 褰兼鍙戦€?packet銆侲nd host 鍙兘鏄竴鍙?client machine锛堜緥濡備綘鐨勬湰鍦扮數鑴戯級锛屼篃鍙兘鏄竴鍙?server锛堜緥濡?YouTube锛夈€備絾鏄紝YouTube 鐪熺殑鏄?Internet 涓婄殑涓€鍙版満鍣紝璐熻矗鍚戝叏涓栫晫鎻愪緵瑙嗛鍚楋紵

<img width="800px" src="/assets/datacenter/6-001-single-server.png">

鐜板疄涓紝YouTube 鏄竴鏁存爧鐢变簰杩炴満鍣ㄧ粍鎴愮殑寤虹瓚锛岃繖浜涙満鍣ㄥ崗鍚屽伐浣滐紝鍚?client 鎻愪緵瑙嗛銆傛墍鏈夎繖浜涙満鍣ㄩ兘鍦ㄥ悓涓€涓?local network 涓紝骞朵笖鍙互鐩镐簰閫氫俊鏉ュ畬鎴?request锛堜緥濡傦紝濡傛灉浣犺姹傜殑瑙嗛鍒嗗竷瀛樺偍鍦ㄤ笉鍚屾満鍣ㄤ笂锛夈€?
<img width="800px" src="/assets/datacenter/6-002-many-servers.png">

鍥炲繂涓€涓嬶紝鍦?Internet 鐨?network-of-network 妯″瀷涓紝姣忎釜 operator 閮藉彲浠ユ寜鑷繁鎯宠鐨勬柟寮忕鐞嗚嚜宸辩殑 local network銆傚湪鏈妭涓紝鎴戜滑浼氳仛鐒︿簬涓撻棬杩炴帴 datacenter 鍐呴儴 server 鐨?local network锛堣€屼笉鏄儚浣犵殑涓汉鐢佃剳杩欐牱鐨?user锛夈€傛垜浠細璁ㄨ杩欎簺 local network 鐙湁鐨勬寫鎴橈紝浠ュ強涓撻棬璁捐鏉ラ€傚悎 datacenter 鍦烘櫙鐨勭綉缁滈棶棰樿В鍐虫柟妗堬紙渚嬪 congestion control 鍜?routing锛夈€?
鐜板疄涓紝datacenter 浣嶄簬涓€涓墿鐞嗕綅缃紝閫氬父寤哄湪涓撻棬鐨勫満鍦颁笂銆傞櫎浜嗚绠楀熀纭€璁炬柦锛堜緥濡?server锛変箣澶栵紝datacenter 杩橀渶瑕佸喎鍗寸郴缁熷拰渚涚數绛夋敮鎾戝熀纭€璁炬柦锛屼笉杩囨垜浠細閲嶇偣鍏虫敞杩炴帴杩欎簺 server 鐨?local network銆?
Datacenter 涓?application 鎻愪緵鏈嶅姟锛堜緥濡?YouTube 瑙嗛銆丟oogle 鎼滅储缁撴灉绛夛級銆傝繖鏄綘鍙兘鎯宠閫氫俊鐨?end host 鎵€鍦ㄧ殑鍩虹璁炬柦銆傛敞鎰忥紝杩欎笉鍚屼簬鎴戜滑鍒扮洰鍓嶄负姝㈣杩囩殑 Internet 鍩虹璁炬柦銆備箣鍓嶆垜浠湅鍒拌繃 carrier hotel锛屼篃灏辨槸璁稿 network锛堢敱涓嶅悓鍏徃鎷ユ湁锛夌敤澶у瀷 router 褰兼杩炴帴鐨勫缓绛戙€傝繖鏄?router 灏嗕綘鐨?packet 杞彂鍒板悇绉?destination 鐨勫熀纭€璁炬柦锛屼絾 application 閫氬父涓嶄細鎵樼鍦?carrier hotel 涓€?
Datacenter 閫氬父鐢卞崟涓粍缁囨嫢鏈夛紙渚嬪 Google銆丄mazon锛夛紝鑰岃缁勭粐鍙互鍦ㄤ竴涓?datacenter 涓墭绠¤澶氫笉鍚?application锛堜緥濡?Gmail銆乊ouTube 绛夛級銆傝繖鎰忓懗鐫€璇ョ粍缁囨帶鍒?datacenter 鐨?local network 鍐呴儴鐨勬墍鏈夌綉缁滃熀纭€璁炬柦銆?
鎴戜滑鐨勯噸鐐规槸鐜颁唬 hyperscale datacenter锛屼篃灏辨槸鐢?Google銆丄mazon 杩欐牱鐨勭鎶€宸ㄥご杩愯惀鐨勫ぇ瑙勬ā datacenter銆傚ぇ瑙勬ā浼氬甫鏉ヤ竴浜涚嫭鐗规寫鎴橈紝浣嗘垜浠皢鐪嬪埌鐨勬蹇典篃閫傜敤浜庤緝灏忚妯°€?
<img width="900px" src="/assets/datacenter/6-003-wan1.png">

杩欏紶鍦板浘灞曠ず浜嗗儚 Google 杩欐牱鐨勭鎶€宸ㄥご鎵€鎷ユ湁鐨勬墍鏈?network 鏋勬垚鐨?wide area network锛圵AN锛夈€?
Peering location 灏?Google 杩炴帴鍒?Internet 鐨勫叾浣欓儴鍒嗐€傝繖浜涗綅缃富瑕佺敱 Google 杩愯惀鐨?router 鏋勬垚锛屽畠浠繛鎺ュ埌鍏朵粬 autonomous system銆?
<img width="900px" class="real-photo" src="/assets/datacenter/6-004-peering.png">

闄や簡 peering location锛孏oogle 杩樿繍钀ヨ澶?datacenter銆侱atacenter 涓殑 application 鍙互閫氳繃 peering location 涓?Internet 鐨勫叾浣欓儴鍒嗛€氫俊銆侱atacenter 鍜?peering location 閮介€氳繃 Google wide area network 涓敱 Google 绠＄悊鐨?router 鍜?link 鐩镐簰杩炴帴銆?
<img width="900px" class="real-photo" src="/assets/datacenter/6-005-datacenter-irl1.png">

Datacenter 鍜?peering location 閽堝涓嶅悓鐨勬€ц兘鐩爣浼樺寲锛屽洜姝ゅ畠浠€氬父浣嶄簬涓嶅悓鐨勭墿鐞嗗湴鐐广€?
Peering location 鍏冲績鍦ㄧ墿鐞嗕笂闈犺繎鍏朵粬鍏徃鍜?network銆傚洜姝わ紝carrier hotel 閫氬父浣嶄簬鍩庡競涓紝浠ヤ究鍦ㄧ墿鐞嗕笂鏇存帴杩?customer 鍜屽叾浠栧叕鍙搞€?
鐩告瘮涔嬩笅锛宒atacenter 涓嶅お鍏冲績闈犺繎鍏朵粬鍏徃锛岃€屾槸浼樺厛鑰冭檻鐗╃悊绌洪棿銆佺數鍔涘拰鍐峰嵈绛夐渶姹傘€傚洜姝わ紝datacenter 閫氬父浣嶄簬浜哄彛杈冨皯鐨勫湴鍖猴紝鏈夋椂闄勮繎鏈夋渤娴侊紙鐢ㄤ簬鍐峰嵈锛夋垨鍙戠數绔欙紙datacenter 鍙兘闇€瑕佹瘮 peering location 澶氭暟鐧惧€嶇殑鐢靛姏锛夈€?
<img width="800px" class="real-photo" src="/assets/datacenter/6-006-datacenter-irl2.png">

## Datacenter 涓轰粈涔堜笉鍚岋紵

Datacenter 鐨?local network 涓?Internet 鍏朵綑閮ㄥ垎鐨勯€氱敤锛坵ide area锛塶etwork 鏈変粈涔堜笉鍚岋紵

Datacenter network 鐢卞崟涓粍缁囪繍琛岋紝杩欒鎴戜滑瀵圭綉缁滃拰 host 鏈夋洿澶氭帶鍒躲€備笉鍚屼簬閫氱敤 Internet锛屾垜浠彲浠ヨ繍琛岃嚜宸辩殑瀹氬埗纭欢鎴栬蒋浠讹紝骞朵笖鍙互寮哄埗姣忓彴鏈哄櫒閬靛惊鍚屼竴绉嶅畾鍒?protocol銆?
Datacenter 寰€寰€鏄?homogeneous锛堝悓璐級鐨勶紝姣忓彴 server 鍜?switch 閮戒互瀹屽叏鐩稿悓鐨勬柟寮忔瀯寤哄拰杩愯惀銆備笉鍚屼簬閫氱敤 Internet锛屾垜浠笉蹇呰€冭檻涓€浜?link 鏄?wireless銆佸彟涓€浜?link 鏄?wired銆傚湪閫氱敤 Internet 涓紝鏈変簺 computer 鍙兘姣斿叾浠?computer 鏇存柊锛屼絾鍦?datacenter 涓紝姣忓彴 computer 閫氬父閮藉睘浜庡悓涓€浠ｏ紝鏁翠釜 datacenter 涔熶細鍚屾椂鍗囩骇銆?
Datacenter network 浣嶄簬涓€涓墿鐞嗕綅缃紝鍥犳鎴戜滑涓嶅繀鑰冭檻娴峰簳鍏夌紗杩欑被闀胯窛绂?link銆傚湪杩欎釜鍗曚竴浣嶇疆鍐咃紝鎴戜滑蹇呴』鏀寔鏋侀珮鐨?bandwidth銆?
## Datacenter Traffic Pattern

褰撲綘鍚?datacenter application 鍙戝嚭 request 鏃讹紝浣犵殑 packet 浼氱┛杩囬€氱敤 Internet 涓殑 router锛屾渶缁堝埌杈?Google 杩愯惀鐨?router銆傝 router 浼氭妸浣犵殑 packet 杞彂缁?datacenter 鐨勪竴涓?edge router锛屽悗鑰呭啀鎶?packet 杞彂缁?datacenter 涓煇鍙板叿浣?server銆?
杩欎竴鍙?server 鍙兘骞朵笉鎷ユ湁澶勭悊浣犵殑 request 鎵€闇€鐨勫叏閮ㄤ俊鎭€備緥濡傦紝濡傛灉浣犺姹?Facebook feed锛屼笉鍚?server 鍙兘闇€瑕佸崗鍚岀粍鍚堝箍鍛娿€佺収鐗囥€佸笘瀛愮瓑淇℃伅銆傚鏋滄瘡鍙?server 閮藉繀椤昏嚜宸辩煡閬撳叧浜?Facebook 鐨勬墍鏈夊唴瀹规墠鑳藉鐞嗕綘鐨?request锛岄偅骞朵笉鐜板疄銆?
涓轰簡璁╀笉鍚?server 鍗忚皟锛岀涓€鍙?server 浼氳Е鍙戣澶?backend request锛屾敹闆嗕綘鐨?request 鎵€闇€鐨勫叏閮ㄤ俊鎭€傚崟涓?user request 鍙兘鍦?response 鑳借繑鍥炵粰鐢ㄦ埛涔嬪墠瑙﹀彂鏁扮櫨涓?backend request锛堟牴鎹?2013 骞翠竴绡?Facebook paper锛屽钩鍧囦负 521 涓級銆備竴鑸潵璇达紝server 涔嬮棿鐨?backend traffic 鏄庢樉鏇村锛岃€屼笌鐢ㄦ埛涔嬮棿鐨?external traffic 鐩告瘮闈炲父灏忋€?
<img width="900px" src="/assets/datacenter/6-007-nsew-traffic1.png">

澶у鏁扮幇浠?application 閮戒互鍐呴儴鍒嗗竷鍦ㄦ満鍣ㄤ箣闂寸殑 traffic 涓轰富銆備緥濡傦紝濡傛灉杩愯 mapreduce 杩欐牱鐨?distributed program锛屼笉鍚?server 闇€瑕佸郊姝ら€氫俊锛屽叡鍚岃В鍐充竴涓ぇ鍨?query銆傛湁浜?application 鐢氳嚦鍙兘瀹屽叏娌℃湁闈㈠悜鐢ㄦ埛鐨?network traffic銆備緥濡傦紝Google 鍙兘杩愯鍛ㄦ湡鎬у浠斤紝杩欓渶瑕?server 涔嬮棿閫氫俊锛屼絾涓嶄細涓?end user 浜х敓鍙缁撴灉銆?
绂诲紑 network 鐨?connection锛堜緥濡傚埌 end user 鎴栧叾浠?datacenter锛夎绉颁负 **north-south** traffic銆傜浉姣斾箣涓嬶紝network 鍐呴儴鏈哄櫒涔嬮棿鐨?connection 琚О涓?**east-west** traffic銆侲ast-west traffic 姣?north-south traffic 澶у嚑涓暟閲忕骇锛岃€屼笖杩戝勾鏉?east-west traffic 鐨勮妯¤繕鍦ㄥ闀匡紙渚嬪闅忕潃 machine learning 鐨勫彂灞曪級銆?
<img width="300px" src="/assets/datacenter/6-008-nsew-traffic2.png">

## Rack

Datacenter 浠庢牴鏈笂鐢辫澶?server 缁勬垚銆傝繖浜?server 琚粍缁囧湪鐗╃悊 rack 涓紝姣忎釜 rack 鏈?40-48 涓?rack unit锛坰lot锛夛紝姣忎釜 rack unit 鍙互鏀惧叆 1-2 鍙?server銆?
<img width="500px" class="real-photo" src="/assets/datacenter/6-009-rack1.png">

鎴戜滑甯屾湜 datacenter 涓墍鏈?server 閮借兘褰兼閫氫俊锛屽洜姝ら渶瑕佹瀯寤轰竴涓?network 鎶婂畠浠叏閮ㄨ繛鎺ヨ捣鏉ャ€傝繖涓?network 鐪嬭捣鏉ュ簲璇ユ槸浠€涔堟牱锛熸垜浠浣曢珮鏁堝湴瀹夎 link 鍜?switch 鏉ユ弧瓒抽渶姹傦紵

棣栧厛锛屾垜浠彲浠ヨ繛鎺ュ悓涓€涓?rack 鍐呯殑鎵€鏈?server銆傛瘡涓?rack 鏈変竴涓?switch锛岀О涓?**top-of-rack锛圱OR锛塻witch**锛況ack 涓殑姣忓彴 server 閮芥湁涓€鏉?link锛堢О涓?**access link** 鎴?**uplink**锛夎繛鎺ュ埌杩欎釜 switch銆俆OR 鏄竴涓浉瀵硅緝灏忕殑 router锛屽叿鏈夊崟涓?forwarding chip锛屼互鍙婅繛鎺?rack 涓婃墍鏈?server 鐨勭墿鐞?port銆傛瘡鏉?server uplink 鐨勫閲忛€氬父绾︿负 100 Gbps銆?
<img width="500px" class="real-photo" src="/assets/datacenter/6-010-rack2.png">

鎺ヤ笅鏉ワ紝鎴戜滑蹇呴』鎬濊€冨浣曟妸 rack 杩炴帴鍦ㄤ竴璧枫€傜悊鎯虫儏鍐典笅锛屾垜浠笇鏈涙瘡鍙?server 閮借兘浠?full line rate锛堜篃灏辨槸浣跨敤瀹屾暣 uplink bandwidth锛変笌鍏朵粬浠绘剰 server 閫氫俊銆?
<img width="500px" src="/assets/datacenter/6-011-rack3.png">

## Bisection Bandwidth

鍦ㄦ€濊€冨浣曡繛鎺?rack 涔嬪墠锛岃鎴戜滑鍏堟彁鍑轰竴涓?metric锛岀敤鏉ヨ　閲忎竴缁?computer 杩炴帴寰楁湁澶氬厖鍒嗐€?
<img width="800px" src="/assets/datacenter/6-012-bisection1.png">

鐩磋涓婏紝铏界劧杩欎笁涓?network 閮芥槸 fully connected锛屽乏杈?network 鐨勮繛鎺ユ€ф渶寮猴紝涓棿 network 娆′箣锛屽彸杈?network 鏈€寮便€備緥濡傦紝宸﹁竟鍜屼腑闂寸殑 network 鍙互鏀寔 1-4 鍜?3-6 鍚屾椂浠?full line rate 閫氫俊锛岃€屽彸杈?network 涓嶈銆?
涓€绉嶈鏄庡乏杈?network 杩炴帴鎬ф洿寮虹殑鏂规硶鏄锛氭垜浠繀椤诲垏鏂洿澶?link 鎵嶈兘鏂紑 network銆傝繖琛ㄦ槑瀛樺湪澶ч噺 redundant link锛屼娇鎴戜滑鍙互杩愯璁稿鍚屾椂鍙戠敓鐨勯珮 bandwidth connection銆傜被浼煎湴锛屼竴绉嶈鏄庡彸杈?network 杩炴帴鎬ф洿寮辩殑鏂规硶鏄锛氭垜浠彧闇€瑕佸垏鏂?2-5 link 灏辫兘鏂紑 network锛岃繖琛ㄦ槑瀛樺湪涓€涓?bottleneck锛屼細闃绘鍚屾椂鍙戠敓鐨勯珮 bandwidth connection銆?
**Bisection bandwidth锛堜簩鍒嗗甫瀹斤級** 鏄噺鍖?network 杩炴帴鎬х殑涓€绉嶆柟娉曘€備负浜嗚绠?bisection bandwidth锛屾垜浠绠楅渶瑕佺Щ闄ゅ灏?link锛屾墠鑳芥妸 network 鍒嗘垚涓や釜澶у皬鐩哥瓑銆佸郊姝ゆ柇寮€鐨勫崐鍖恒€侭isection bandwidth 鏄鍒囨柇 link 涓?bandwidth 鐨勬€诲拰銆?
<img width="900px" src="/assets/datacenter/6-013-bisection2.png">

鍦ㄦ渶鍙宠竟鐨勭粨鏋勪腑锛屾垜浠彧闇€瑕佺Щ闄や竴鏉?link 灏辫兘鍒嗗壊 network锛屾墍浠?bisection bandwidth 灏辨槸杩欎竴鏉?link銆傜浉姣斾箣涓嬶紝鍦ㄦ渶宸﹁竟鐨勭粨鏋勪腑锛屾垜浠渶瑕佺Щ闄?9 鏉?link 鎵嶈兘鍒嗗壊 network锛屾墍浠?bisection bandwidth 鏄墍鏈?9 鏉?link 鐨?combined bandwidth銆?
瀹氫箟 bisection bandwidth 鐨勭瓑浠锋柟寮忔槸锛氭垜浠妸 network 鍒嗘垚涓ゅ崐锛屽叾涓竴鍗婁腑鐨勬瘡涓?node 閮芥兂鍚屾椂鍚戝彟涓€鍗婁腑瀵瑰簲鐨?node 鍙戦€佹暟鎹€傚湪鎵€鏈夊彲鑳界殑 node partition 涓紝杩欎簺 node 鑳藉叡鍚屽彂閫佺殑鏈€灏?bandwidth 鏄灏戯紵鑰冭檻 worst case锛堟渶灏?bandwidth锛変細杩娇鎴戜滑鎬濊€?bottleneck銆?
<img width="900px" src="/assets/datacenter/6-014-bisection3.png">

杩炴帴鎬ф渶寮虹殑 network 鍏锋湁 full bisection bandwidth銆傝繖鎰忓懗鐫€娌℃湁 bottleneck锛屽苟涓旀棤璁哄浣曟妸 node 鍒嗗埌涓や釜 partition 涓紝涓€涓?partition 涓殑鎵€鏈?node 閮藉彲浠ュ悓鏃朵互 full rate 涓庡彟涓€涓?partition 涓殑鎵€鏈?node 閫氫俊銆傚鏋滄湁 N 涓?node锛屽苟涓斿乏渚?partition 涓墍鏈?N/2 涓?node 閮戒互 full rate R 鍙戦€佹暟鎹紝閭ｄ箞 full bisection bandwidth 灏辨槸 N/2 涔樹互 R銆?
**Oversubscription** 琛￠噺鎴戜滑绂?full bisection bandwidth 鏈夊杩滐紝鎴栬€呯瓑浠峰湴璇达紝network 鐨?bottleneck 閮ㄥ垎杩囪浇浜嗗灏戙€傚畠鏄?bisection bandwidth 涓?full bisection bandwidth锛堟墍鏈?host 閮戒互 full rate 鍙戦€佹椂鐨?bandwidth锛夌殑姣斿€笺€?
<img width="900px" src="/assets/datacenter/6-015-bisection4.png">

鍦ㄦ渶鍙宠竟鐨勪緥瀛愪腑锛屽亣璁炬墍鏈?link 閮芥槸 1 Gbps锛岄偅涔?bisection bandwidth 鏄?2 Gbps锛堟妸宸﹁竟 4 鍙?host 鍜屽彸杈?4 鍙?host 鍒嗗紑锛夈€傚綋宸﹁竟 4 鍙?host 鍚屾椂鍙戦€佹暟鎹椂锛宖ull bisection bandwidth 鏄?4 Gbps銆傚洜姝わ紝2/4 杩欎釜姣斿€煎憡璇夋垜浠紝host 鍙兘浠ュ叾 full rate 鐨?50% 鍙戦€併€傛崲鍙ヨ瘽璇达紝鎴戜滑鐨?network 鏄?2x oversubscribed锛屽洜涓哄鏋?host 閮戒互 full rate 鍙戦€侊紝bottleneck link 灏变細 2x overloaded锛堝湪 2 Gbps 鐨?link 涓婃壙杞?4 Gbps锛夈€?
## Datacenter Topology

鎴戜滑鐜板湪宸茬粡瀹氫箟浜?bisection bandwidth锛屽畠鏄竴涓敱 network topology 鍐冲畾鐨勮繛鎺ユ€ф寚鏍囥€傚湪 datacenter 涓紝鎴戜滑鍙互閫夋嫨 topology锛堜緥濡傞€夋嫨鍦ㄥ摢閲屽畨瑁?cable锛夈€傛垜浠簲璇ユ瀯寤轰粈涔?topology 鏉ユ渶澶у寲 bisection bandwidth锛?
涓€绉嶅彲鑳芥柟娉曟槸鎶婃瘡涓?rack 杩炴帴鍒颁竴涓法澶х殑 cross-bar switch銆傚乏渚ф墍鏈?rack 鍙互鍚屾椂浠?full rate 鎶婃暟鎹彂鍏?switch锛岃€?switch 浠?full rate 鎶婃墍鏈夋暟鎹浆鍙戝埌鍙充晶銆傝繖璁╂垜浠兘澶熻揪鍒?full bisection bandwidth銆?
<img width="500px" src="/assets/datacenter/6-016-topology1.png">

杩欑鏂规硶鏈変粈涔堥棶棰橈紵Switch 闇€瑕佷负姣忎釜 rack 鎻愪緵涓€涓墿鐞?port锛堝彲鑳藉杈?2500 涓?port锛夈€傛垜浠湁鏃舵妸 external port 鐨勬暟閲忕О涓?switch 鐨?**radix**锛屽洜姝よ繖涓?switch 闇€瑕佸緢澶х殑 radix銆傚彟澶栵紝杩欎釜 switch 杩橀渶瑕佹嫢鏈夊法澶х殑瀹归噺锛堝彲鑳借揪鍒版瘡绉?petabit 绾у埆锛夋墠鑳芥敮鎸佹墍鏈?rack銆備笉鍑烘墍鏂欙紝杩欐牱鐨?switch 涓嶇幇瀹烇紙鍗充娇鑳藉仛鍑烘潵锛屼环鏍间篃浼氶珮鍒版棤娉曟帴鍙楋級銆?
瓒ｉ椈锛氬湪 2000 骞翠唬锛孏oogle 鏇剧粡瑕佹眰 switch vendor 鍒堕€犱竴涓?10,000-port switch銆俈endor 鎷掔粷浜嗭紝璇翠笉鍙兘鍒堕€犺繖绉嶈澶囷紱鍗充娇鑳藉埗閫狅紝涔熷彧鏈変綘浠細瑕侊紙鎵€浠ュ埗閫犲畠娌℃湁鍒╂鼎锛夈€?
鍙︿竴涓棶棰樻槸锛岃繖涓?switch 鏄崟鐐规晠闅滐紱濡傛灉瀹冨潖浜嗭紝鏁翠釜 datacenter network 閮戒細鍋滄宸ヤ綔銆?
鍙︿竴绉嶅彲鑳芥柟娉曟槸鎶?switch 鎺掑垪鎴?tree topology銆傝繖鍙互甯姪鎴戜滑闄嶄綆姣忔潯 link 鐨?radix 鍜?bandwidth銆?
<img width="500px" src="/assets/datacenter/6-017-topology2.png">

杩欑鏂规硶鏈変粈涔堥棶棰橈紵Bisection bandwidth 鏇翠綆銆俆ree 涓ゅ崐涔嬮棿鐨勪竴鏉?link 鏄?bottleneck銆?
涓轰簡鎻愰珮 bisection bandwidth锛屾垜浠彲浠ュ湪鏇撮珮灞傚畨瑁呮洿楂?bandwidth 鐨?link銆?
<img width="500px" src="/assets/datacenter/6-018-topology3.png">

鍦ㄨ繖绉嶆儏鍐典笅锛屽鏋?4 鏉¤緝浣庡眰 link 鏄?100 Gbps锛岃€?2 鏉¤緝楂樺眰 link 鏄?300 Gbps锛岄偅涔堟垜浠氨绉婚櫎浜?bottleneck锛屽苟鎭㈠浜?full bisection bandwidth銆?
杩欑 topology 鍙互浣跨敤锛屽敖绠℃垜浠粛鐒舵病鏈夎В鍐抽《灞?switch 鏄傝吹涓旀墿灞曟€у樊鐨勯棶棰樸€?
## Clos Network

鍒扮洰鍓嶄负姝紝鎴戜滑灏濊瘯浣跨敤瀹氬埗 switch 鏋勫缓 network锛岃繖浜?switch 鍙兘鍏锋湁闈炲父楂樼殑 bandwidth 鎴?radix銆傝繖浜?switch 浠嶇劧鏄傝吹銆傛垜浠兘鍚︽敼涓鸿璁′竴绉?topology锛岀敤渚垮疁鐨?commodity element 瀹炵幇楂?bisection bandwidth锛熷叿浣撴潵璇达紝鎴戜滑甯屾湜浣跨敤澶ч噺渚垮疁鐨勭幇鎴?switch锛屽叾涓墍鏈?switch 閮芥湁鐩稿悓鏁伴噺鐨?port锛屾瘡涓?switch 鐨?port 鏁伴噺杈冧綆锛屽苟涓旀墍鏈?link speed 鐩稿悓銆?
<img width="600px" src="/assets/datacenter/6-019-clos1.png">

**Clos network** 閫氳繃鍦?network 涓紩鍏ュぇ閲?node 涔嬮棿鐨?path锛屼娇鐢?commodity part 瀹炵幇楂?bandwidth銆傜敱浜庣綉缁滀腑鏈夎繖涔堝 link 鍜?path锛屾垜浠彲浠ヨ姣忎釜 node 娌夸笉鍚?path 鍙戦€佹暟鎹紝浠庤€屽疄鐜伴珮 bisection bandwidth銆?
<img width="600px" src="/assets/datacenter/6-020-clos2.png">

涓嶅悓浜庨€氳繃鍒堕€犳洿澶?switch 鏉ユ墿灞?network 鐨勫畾鍒?switch锛屾垜浠彲浠ラ€氳繃绠€鍗曞湴澧炲姞鏇村鐩稿悓 switch 鏉ユ墿灞?Clos network銆傝繖涓柟妗堟棦鍒掔畻鍙堝彲鎵╁睍锛?
Clos network 涔熻鐢ㄤ簬鍏朵粬搴旂敤锛屽苟浠ュ叾鍙戞槑鑰呭懡鍚嶏紙Charles Clos锛?952锛夈€?
鍦ㄧ粡鍏?Clos network 涓紝鎴戜滑浼氳宸﹁竟鎵€鏈?rack 鍚戝彸杈?rack 鍙戦€佹暟鎹€傚湪 datacenter 涓紝rack 鏃㈠彲浠ュ彂閫佷篃鍙互鎺ユ敹鏁版嵁锛屽洜姝ゆ垜浠笉鍐嶈缃垎绂荤殑 sender layer 鍜?recipient layer锛岃€屾槸璁剧疆涓€涓寘鍚墍鏈?rack 鐨勫崟涓€ layer锛堝畠浠棦鍙互浣滀负 sender锛屼篃鍙互浣滀负 recipient锛夈€傜劧鍚庯紝鏁版嵁娌胯澶?path 涓殑涓€鏉″悜缃戠粶鏇存繁澶勪紶杈擄紝鍐嶈繑鍥炲嚭鏉ュ埌杈?recipient銆傝繖涓粨鏋滅О涓?**folded Clos network**锛屽洜涓烘垜浠妸 sender 鍜?recipient layer 鈥滄姌鍙犫€濇垚浜嗕竴灞傘€?
<img width="900px" src="/assets/datacenter/6-021-clos3.png">

## Fat-Tree Clos Topology

Fat-tree topology 涓瘡涓?switch 鐨?radix 杈冧綆锛屽苟鑳藉疄鐜?full bisection bandwidth銆備笉杩囷紝tree 椤堕儴鐨?switch 鏄傝吹銆佹墿灞曟€у樊锛屽苟涓斾粛鐒舵槸鍗曠偣鏁呴殰銆?
Clos topology 鍏佽鎴戜滑浣跨敤 commodity switch 鎵╁睍 network銆傚鏋滄妸 Clos topology 鍜?fat-tree topology 缁撳悎璧锋潵锛屾垜浠氨鑳界敤 commodity switch 鏋勫缓鍙墿灞?topology锛?
杩欓噷灞曠ず鐨?topology 鏉ヨ嚜涓€绡?2008 骞?SIGCOMM paper锛屾爣棰樻槸 鈥淎 Scalable, Commodity Data Center Network Architecture鈥濓紙Mohammad Al-Fares銆丄lexander Loukissas銆丄min Vahdat锛夈€?
鍦?k-ary fat tree 涓紝鎴戜滑鍒涘缓 k 涓?pod銆傛瘡涓?pod 鏈?k 涓?switch銆?
鍦ㄤ竴涓?pod 鍐咃紝k/2 涓?switch 浣嶄簬涓婃柟 aggregation layer锛屽彟澶?k/2 涓?switch 浣嶄簬涓嬫柟 edge layer銆?
锛堟敞鎰忥細杩欎釜 topology 涓哄伓鏁?k 瀹氫箟锛岃繖鏍锋垜浠墠鑳芥妸 switch 鍧囧寑鍒嗗埌 aggregation layer 鍜?edge layer 涓€傦級

<img width="900px" src="/assets/datacenter/6-022-pods1.png">

Pod 涓殑姣忎釜 switch 閮芥湁 k 鏉?link銆備竴鍗?link锛坘/2锛夊悜涓婅繛鎺ワ紝鍙︿竴鍗?link锛坘/2锛夊悜涓嬭繛鎺ャ€?
鑰冭檻涓婃柟 aggregation layer 涓殑涓€涓?switch銆傚畠鐨勪竴鍗?link锛坘/2锛夊悜涓婅繛鎺ュ埌 core layer锛坈ore layer 璐熻矗杩炴帴 pod锛岀◢鍚庝細杩涗竴姝ヨ璁猴級銆傚彟涓€鍗?link锛坘/2锛夊悜涓嬭繛鎺ュ埌 edge layer 涓殑 k/2 涓?switch銆?
绫讳技鍦帮紝鑰冭檻涓嬫柟 edge layer 涓殑涓€涓?switch銆傚畠鐨勪竴鍗?link锛坘/2锛夊悜涓婅繛鎺ュ埌 aggregation layer 涓殑 k/2 涓?switch銆傚彟涓€鍗?link锛坘/2锛夊悜涓嬭繛鎺ュ埌杩欎釜 pod 涓殑 k/2 鍙?host銆?
<img width="900px" src="/assets/datacenter/6-023-pods2.png">

鎺ヤ笅鏉ワ紝璁╂垜浠湅鐪嬭繛鎺?pod 鐨?core layer銆傛瘡涓?core switch 鏈?k 鏉?link锛屽垎鍒繛鎺ュ埌 k 涓?pod銆?
鍏辨湁 $(k/2)^2$ 涓?core switch銆傝繖涓暟瀛楁槸鎬庝箞鎺ㄥ鍑烘潵鐨勶紵鏈?k 涓?pod锛屾瘡涓?pod 鍦ㄤ笂鏂?aggregation layer 涓湁 k/2 涓?switch锛屽洜姝?aggregation layer 鎬诲叡鏈?$k^2/2$ 涓?switch銆傛瘡涓?aggregation-layer switch 鏈?k/2 鏉″悜涓?link锛屽洜姝や竴鍏辨湁 $k^2/2 \times k/2 = k^3/4$ 鏉″悜涓?link銆傝繖鎰忓懗鐫€ core layer 闇€瑕佹€诲叡 $k^3/4$ 鏉″悜涓?link锛屾潵鍖归厤 aggregation layer 鐨勫悜涓?link 鏁伴噺銆?
姣忎釜 core layer switch 鏈?k 鏉″悜涓?link锛屽洜姝ゆ垜浠渶瑕?$k^2/4$ 涓?core layer switch锛堟瘡涓湁 k 鏉?link锛夋潵鍒涘缓 $k^3/4$ 鏉″悜涓?link銆傝繖璁?aggregation layer 鍚戜笂鐨?link 鏁伴噺鍜?core layer 鍚戜笅鐨?link 鏁伴噺鍖归厤銆?
鎴戜滑涔熷彲浠ヨ绠楀嚭锛屽湪杩欎釜 topology 涓瘡涓?pod 鏈?$(k/2)^2$ 鍙?host銆傝繖涓暟瀛楁槸鎬庝箞鎺ㄥ鍑烘潵鐨勶紵姣忎釜 pod 鐨?edge layer 鏈?k/2 涓?switch銆傛瘡涓?edge-layer switch 鏈?k/2 鏉″悜涓嬭繛鎺?host 鐨?link锛屽洜姝ゆ瘡涓?pod 涓叡鏈?$k/2 \times k/2 = (k/2)^2$ 鍙?host銆傛敞鎰忥紝姣忓彴 host 鍙繛鎺ュ埌涓€涓?edge-layer switch锛堝湪杩欎釜 topology 涓紝涓€鍙?host 涓嶄細杩炴帴鍒板涓?switch锛夈€傜敱浜庢€诲叡鏈?k 涓?pod锛屾垜浠繕鍙互鎺ㄥ嚭杩欎釜 topology 涓€诲叡鏈?$(k/2)^2 \times k$ 鍙?host銆?
<img width="900px" src="/assets/datacenter/6-024-pods3.png">

k = 4 鏄渶灏忎緥瀛愶紝浣嗕笉骞哥殑鏄湁鐐瑰鏄撴贩娣嗭紝鍥犱负鏈変簺鏁板瓧纰板阀鐩稿悓锛堜緥濡?$(k/2)^2 = k = 4$锛夈€備负浜嗙湅寰楁洿娓呮锛屾垜浠彲浠ョ湅 k = 6 鐨勪緥瀛愩€?
姣忎釜 pod 鏈?k = 6 涓?switch銆俴/2 = 3 涓?switch 浣嶄簬涓婃柟 aggregation layer锛宬/2 = 3 涓?switch 浣嶄簬涓嬫柟 edge layer銆?
涓€涓?edge layer switch 鏈?k/2 = 3 鏉″悜涓?link 杩炴帴鍒?3 鍙?host锛屼篃鏈?k/2 = 3 鏉″悜涓?link 杩炴帴鍒板悓涓€涓?pod 涓殑 3 涓?aggregation switch銆?
涓€涓?aggregation layer switch 鏈?k/2 = 3 鏉″悜涓?link 杩炴帴鍒?core layer锛堝叿浣撴潵璇达紝杩炴帴鍒?3 涓笉鍚?core layer switch锛夛紝涔熸湁 k/2 = 3 鏉″悜涓?link 杩炴帴鍒板悓涓€涓?pod 涓殑 3 涓?edge layer switch銆?
姣忎釜 pod 鏈?k/2 = 3 涓?edge switch锛屾瘡涓繛鎺ュ埌 k/2 = 3 鍙?host锛屽洜姝ゆ瘡涓?pod 鎬诲叡鏈?$(k/2)^2 = 9$ 鍙?host銆傝繖涓?topology 鎬诲叡鏈?k 涓?pod锛屽洜姝ゆ€诲叡鏈?$k \times (k/2)^2 = 54$ 鍙?host銆?
鍦?core layer锛屾垜浠湁 $(k/2)^2 = 9$ 涓?core switch銆傛瘡涓?switch 鏈?k = 6 鏉?link锛屽垎鍒悜涓嬭繛鎺ュ埌 k = 6 涓?pod銆?
鎬昏锛宑ore layer 鏈?$(k/2)^2 \times k$ 鏉″悜涓?link锛坈ore switch 鏁伴噺涔樹互姣忎釜 switch 鐨?link 鏁伴噺锛夈€侫ggregation layer 鏈?$k \times (k/2) \times (k/2)$ 鏉″悜涓?link锛坧od 鏁伴噺涔樹互姣忎釜 pod 鐨?aggregation switch 鏁伴噺锛屽啀涔樹互姣忎釜 aggregation switch 鐨勫悜涓?link 鏁伴噺锛夈€傝繖涓や釜琛ㄨ揪寮忕浉绛夛紙褰?k = 6 鏃堕兘绛変簬 54锛夛紝浠庤€岃 core layer 鑳藉涓?aggregation layer fully connected銆?
<img width="900px" src="/assets/datacenter/6-025-pods4.png">

杩欎釜 topology 瀹炵幇浜?full bisection bandwidth銆傚鏋滄妸 pod 鍒嗘垚涓ゅ崐锛堜緥濡傚乏鍗婂拰鍙冲崐锛夛紝閭ｄ箞宸﹀崐涓殑姣忓彴 host 閮芥湁涓€鏉?dedicated path 鍒板彸鍗婁腑瀵瑰簲鐨?host銆傝繖鍏佽鎵€鏈?host 閰嶅锛堜竴鍙板湪宸﹀崐锛屼竴鍙板湪鍙冲崐锛夛紝骞朵笖姣忎竴瀵归兘娌夸竴鏉?dedicated path 閫氫俊锛屾病鏈?bottleneck銆?
鍙﹀锛岃娉ㄦ剰锛岃繖涓?topology 鍙互鐢?commodity switch 鏋勫缓銆傛瘡涓?switch 鐨?radix 閮芥槸 k 鏉?link锛屼笉绠¤繖涓?switch 浣嶄簬鍝竴灞傘€傛澶栵紝姣忔潯 link 閮藉彲浠ユ湁鐩稿悓 bandwidth锛堜緥濡?1 Gbps锛夛紝鑰屾墿灞曟€ф潵鑷繖鏍蜂竴涓簨瀹烇細鎴戜滑鍦ㄤ换鎰?host pair 涔嬮棿鍒涘缓浜嗕竴鏉?dedicated path銆?
<img width="900px" src="/assets/datacenter/6-026-pods5.png">

鍙︿竴绉嶇悊瑙?full bisection bandwidth 鐨勬柟寮忥紝鏄笉鏂垹闄?link锛岀洿鍒?network 琚垎鍓叉垚涓ゅ崐锛堝乏鍗?pod 鍜屽彸鍗?pod锛夈€?
姣忎釜 core layer switch 鏈?k 鏉?link锛屾瘡鏉¤繛鎺ュ埌涓€涓?pod銆傝繖涔熸剰鍛崇潃姣忎釜 core layer switch 鏈?k/2 鏉?link 杩炴帴鍒板乏渚э紝k/2 鏉?link 杩炴帴鍒板彸渚с€?
涓轰簡瀹屽叏闅旂涓€渚э紙渚嬪瀹屽叏闅旂宸︿晶锛夛紝瀵逛簬姣忎釜 core switch锛屾垜浠繀椤诲垏鏂?k/2 鏉¤繛鎺ュ埌宸︿晶鐨?link銆傚叡鏈?$(k/2)^2$ 涓?core switch锛屽苟涓旀瘡涓?switch 蹇呴』鍒囨柇 k/2 鏉?link锛屽洜姝ゆ€诲叡鍒囨柇 $(k/2)^3$ 鏉?link銆傝繖鎰忓懗鐫€鎴戜滑鐨?bisection bandwidth 鏄?$(k/2)^3$ 鏉?link锛堝亣璁炬瘡鏉?link 鐨?bandwidth 鐩稿悓锛夈€?
姣忎釜 pod 鏈?$(k/2)^2$ 鍙?host锛屽乏渚ф湁 k/2 涓?pod锛屽洜姝ゅ乏渚ф€诲叡鏈?$(k/2)^3$ 鍙?host銆傜被浼煎湴锛屽彸渚т篃鏈?$(k/2)^3$ 鍙?host銆傚鏋滃乏渚ф瘡鍙?host 閮芥兂涓庡彸渚ф瘡鍙?host 閫氫俊锛屽氨闇€瑕佷环鍊?$(k/2)^3$ 鏉?link 鐨?bandwidth銆傛垜浠殑 bisection bandwidth 涓庤繖涓暟瀛楃浉鍚岋紝杩欐剰鍛崇潃瀹炵幇浜?full bisection bandwidth銆?
<img width="900px" src="/assets/datacenter/6-027-pods6.png">

杩欎釜 Clos fat-tree topology 鍜屽墠闈?rack 涓?top-of-rack switch 鐨勬蹇垫湁浠€涔堝叧绯伙紵

瀵逛簬涓€浜涘悎閫傜殑 k 鍊硷紝鎴戜滑鍙互鎶婁竴涓?pod 鍐呯殑 host 鍜?switch 鍒嗗埆鏀惧叆涓嶅悓 rack锛屽苟鎶?rack 褰兼杩炴帴璧锋潵銆?
渚嬪锛岃€冭檻 k = 48锛屼篃灏辨槸鍘熷 paper 涓娇鐢ㄧ殑绀轰緥鍊笺€傝繖鎰忓懗鐫€鍦ㄤ竴涓?pod 鍐咃紝鏈?k/2 = 24 涓?aggregation layer switch銆乲/2 = 24 涓?edge layer switch锛屼互鍙?$(k/2)^2$ = 576 鍙?host銆?
鎴戜滑鍙互瀹夋帓 switch 鍜?host锛屼娇鍏ㄩ儴 48 涓?switch 浣嶄簬涓棿鐨勪竴涓?rack 涓€傜劧鍚庯紝鐢?12 涓?rack 鍥寸粫杩欎釜 switch rack锛屾瘡涓?rack 瀹圭撼 48 鍙?host銆傝繖甯姪鎴戜滑鎶婃墍鏈?switch 鍜?host 鏀惧叆澶у皬鐩稿悓鐨?rack锛堟瘡涓?rack 48 鍙版満鍣級銆傛妸 switch 鏀惧湪涓棿 rack 涓篃鍑忓皯浜嗘瀯寤鸿繖涓?topology 鎵€闇€鐨勭墿鐞嗗竷绾块噺銆?
涓棿 rack 鏈?k = 48 涓?switch銆傛瘡涓?switch 鏈?k = 48 涓?port锛屽洜姝よ繖涓?rack 涓€诲叡鏈?$48^2 = 2304$ 涓?port銆?
鍦ㄨ繖 $k^2 = 2304$ 涓?port 涓紝涓€鍗婏紙$k^2/2 = 1152$锛夌敤浜庢妸 rack 鍐呯殑 switch 鐩镐簰杩炴帴銆傛垜浠槸鎬庝箞鎺ㄥ鍑?$k^2/2$ 鐨勶紵鐪嬬湅鍓嶉潰鐨勪竴浜涙蹇靛浘鍙兘浼氭湁甯姪銆俴/2 涓?aggregation layer switch 涓殑姣忎竴涓兘鏈?k/2 鏉″悜涓?link锛屽洜姝ゅ叡浣跨敤 $(k/2)^2$ 涓?port銆傜被浼煎湴锛宬/2 涓?edge layer switch 涓殑姣忎竴涓兘鏈?k/2 鏉″悜涓?link锛屽洜姝や篃鍏变娇鐢?$(k/2)^2$ 涓?port銆傚悎璁″緱鍒?$2 \times (k/2)^2 = k^2/2$ 涓?port銆?
娉ㄦ剰锛宎ggregation switch 鍜?edge switch 涔嬮棿鐨?link 杩炴帴鐨勬槸鍚屼竴涓?rack 鍐呯殑 switch銆傚洜姝わ紝姣忔潯 link 闇€瑕佷袱涓?port锛堜竴涓潵鑷?aggregation switch锛屼竴涓潵鑷?edge switch锛夛紝杩欏氨鏄负浠€涔堟垜浠妸 $(k/2)^2$ 杩欎釜鍊间箻浠?2锛堟垨鑰呯瓑浠峰湴锛屽湪 aggregation 鍜?edge 涓ゅ眰閮借鍏ヨ繖涓€硷級銆?
鍦?$k^2 = 2304$ 涓?port 涓紝鍙︽湁鍥涘垎涔嬩竴锛?$k^2/4 = 576$锛夌敤浜庢妸 switch 杩炴帴鍒板悓涓€涓?pod 鍐呯殑 host銆傝繖涓暟瀛楁槸鎬庝箞鎺ㄥ鍑烘潵鐨勶紵璁颁綇锛屼竴涓?pod 鍐呮湁 $(k/2)^2$ 鍙?host锛屽苟涓旀瘡鍙?host 绮剧‘杩炴帴鍒颁竴涓?switch銆傚洜姝わ紝鎴戜滑闇€瑕?switch 涓婄殑 $(k/2)^2 = k^2/4$ 涓?port 鏉ヨ繛鎺?host銆?
鏈€鍚庯紝鍦?$k^2 = 2304$ 涓?port 涓紝鍓╀笅鍥涘垎涔嬩竴锛?$k^2/4 = 576$锛夌敤浜庢妸 pod 杩炴帴鍒?core layer銆傝繖涓暟瀛楁槸鎬庝箞鎺ㄥ鍑烘潵鐨勶紵璁颁綇锛屽叡鏈?$(k/2)^2$ 涓?core switch锛屽苟涓旀瘡涓?core switch 閮芥湁涓€鏉?link 鍒版瘡涓?pod銆傛崲鍙ヨ瘽璇达紝涓€涓?pod 鍒?$(k/2)^2$ 涓?core switch 涓殑姣忎竴涓兘鏈変竴鏉?link銆傚洜姝わ紝鎴戜滑闇€瑕?switch 涓婄殑 $(k/2)^2 = k^2/4$ 涓?port 鏉ヨ繛鎺?core switch銆?
鎬荤粨涓€涓嬶細鍦ㄦ€诲叡 $k^2$ 涓?port 涓紝涓€鍗婄敤浜庝簰杩炲悓涓€灞備腑鐨?aggregation/edge switch锛堣繛鎺ュ畬鍏ㄥ彂鐢熷湪涓棿 rack 鍐咃級銆傚彟鏈夊洓鍒嗕箣涓€鐢ㄤ簬杩炴帴 edge switch 鍜?pod 涓殑 host锛堣繛鎺ュ彂鐢熷湪涓棿 rack 鍜屽懆鍥?12 涓?host rack 涔嬮棿锛夈€傛渶鍚庡洓鍒嗕箣涓€鐢ㄤ簬杩炴帴 aggregation switch 鍜?core layer锛堣繛鎺ュ彂鐢熷湪涓棿 rack 鍜屽叾浠?core-layer rack 涔嬮棿锛夈€?
<img width="600px" src="/assets/datacenter/6-028-pods7.png">

## 鐜板疄涓栫晫涓殑 Topology

<img width="900px" class="real-photo" src="/assets/datacenter/6-029-irl-topology1.png">

鍦ㄨ繖涓緥瀛愶紙2008锛変腑锛屼换鎰忎袱涓?end host 涔嬮棿閮芥湁璁稿涓嶅悓 path銆?
<img width="900px" class="real-photo" src="/assets/datacenter/6-030-irl-topology2.png">

鍦ㄨ繖绡?paper锛?015锛変腑锛岀爺绌朵簡澶氱 topology銆?
瀛樺湪璁稿鍏蜂綋鍙樹綋锛?009銆?015锛夛紝浣嗗畠浠兘鍏变韩鍚屼竴涓洰鏍囷細鍦ㄤ换鎰忎袱鍙?server 涔嬮棿瀹炵幇楂?bandwidth銆?
