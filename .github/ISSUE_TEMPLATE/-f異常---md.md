---
name: "-f異常--.md"
about: Describe this issue template's purpose here.
title: ''
labels: ''
assignees: ''

---

---
name: "[異常營收排查] "
about: 排查營收異常的版位
title: "[營收異常排查] "
labels: 'Priority: High'
assignees: ''

---

## Context
版位：

頁面：

營收：

Remark：

## Checklist
### Slot 整體走勢
- https://metabase.gliaoffice.com/dashboard/89
slot 換成要偵錯的 slot
  - [ ] 截圖：
- Revenue/RPM 是某一天開始變低，還是一直很低？
  - [ ] 某天開始變低，日期：
  - [ ] 一直都很低
- [ ] Traffic 有明顯變化，日期：
- [ ] 主要營收由哪些 demand 來：
  - [ ] demand 突然變低，日期：
  - [ ] Glia, Dormknight adx 沒有在 top demands 裡。adx 不是主要 demands 的 slot 就比較屬於異常，表示這個站叫不到 adx 的廣告。
- [ ] Slot 上線日期 (最早有數據的日期)：
  - [ ] 可能被蜜月期影響 (前幾天營收特別高)

### 設定
最近有改動的設定，請 AM 先填知道的
RD 檢查 Slot, SlotSetting history
- [ ] 後台設定：
- [ ] 頁面版位位置


### 偵錯
  - 頁面
    - [ ] player 沒有出現
      - [ ] 沒出現的時候 devtools element 裡其實有 player 的 code，可能有錯誤導致沒 init 成功？
    - 肉眼檢查有沒有明顯的問題
      - [ ] 容易被其他廣告/內容擋住
      - [ ] player 太小 (小於 256px)
      - [ ] 其他可能問題：
    - [ ] player 運作不符設定：
  - Player
    - [ ] RPM 變化時間點有上版
    - https://metabase.gliaoffice.com/dashboard/89
      - [ ] Player 行為段落截圖：
      - [ ] 數據在 RPM 改變時間點附近有變化
- GAM
  - 報表拉出 slot 相關數字，ad unit contains 改成 slot name
https://admanager.google.com/21818843116#reports/report/detail/report_id=13351255631
    - [ ] 截圖：
    - [ ] 平均 daily match rate：
      - [ ] match rate 偏低
整體 adx match rate 低於 0.5% 左右就算偏低
    - [ ] 平均 ad request 次數與 slot traffic 的比例：
如果 ad request 沒有達到 slot traffic ~10 倍，可能表示有設定讓 ad request 不足，檢查頁面 adx adtag 有沒有出現在 network
  - 報表 dimension 加上 by ad unit
一般 request 順序就是從底價高到低，glia_adx_3_... 就是底價 $3 的 ad unit
    - [ ] 截圖：
    - [ ] 看低底價的 ad request 有沒有比高底價的少很多，有的話可能表示頁面停留時間很短，來不及叫到低的那邊就離開了
    - [ ] 從哪個底價開始 match rate 才超過 0.5%：
match rate ~0% 的 ad unit 可能可以測試關掉不要去叫，節省時間
  - 檢查 GAM 關鍵指標（ Ad Exchange ad requests、Bids、Unfilled impressions 等 )
      - 報表未紀錄到 「Ad Exchange ad requests
        - 可能屬於 「MCM帳戶終止」，可檢查帳戶狀態：https://admanager.google.com/22825748039#admin/mcm/child_publisher/list
          - [ ] 子帳戶狀態異常（子帳戶名稱）：
        - 可能 Sites 驗證沒通過：https://admanager.google.com/22825748039#inventory/site/mcm/list
          - [ ] Site 狀態異常：
      - 報表有紀錄到 「Ad Exchange ad requests」但 未紀錄到「Bids」可能為「ads.txt 被移除」，可檢查 Account 
        - [ ] ads.txt 移除
      - 上述關鍵指標只有數值降低且排除前述狀態，可能屬於 bid 出價降低，可檢查 adx bidder：https://admanager.google.com/21818843116#reports/report/detail/report_id=13554450357
        - [ ] 有 bidder 突然變低（主要出價平台、異常時間）：
  - 檢查 policy center 
    - [ ] 出現全站 violation
    - [ ] page violations request 量很高
      - [ ] 主要違規原因：
- Ad Units
  - [ ] Slot admin 裡沒有該有的 Ad Units
  - 頁面上有發出 request
    - [ ] ad request:
  - [ ] request parameters 異常 (Macro 沒填入、...)
- Account
  - [ ] is_active 沒開啟
  - [ ] demand verification 沒有通過 Glia AdExchange

### 優化
- Slot 有沒有本來就不利營收的設定
大部分額外的設定會減少 ad request，源頭減少自然曝光的次數也會減少。這些一般是來自媒體的要求，就看 AM 覺得能不能先關掉。
  - [ ] float mode: none
  - [ ] floatEnd on close button, floatStart on scroll
  - [ ] maxAd, maxRequest
  - [ ] waterfall mode: mid-roll, pre-roll
  - [ ] viewability mode: pause
  - [ ] lazyLoad
