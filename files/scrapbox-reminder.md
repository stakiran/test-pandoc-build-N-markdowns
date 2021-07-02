## scrapbox-reminder
んー、微妙かも

- まとめ
    - 必要性はないです
    - 遊びや勉強としてつくるのは面白そうだけど
- :sta:は必要性を感じない
    - キッチンタイマー使えばいい
- ただUserScriptで遊ぶ題材としては面白そう
- あとは[ScrapboxでGTD](ScrapboxでGTD.md)か
    - 「Scrapboxにこもる」コンセプトなので、リマインダーもScrapboxでやりたい思いが強い
    - でも利用者にUserScript使わせる負担ができてしまう
    - 普通に「キッチンタイマー各自で使ってね」が良い気がする

<br>

実装方針

- 設定ページ名
    - .remind
    - :sta:[Scrapbox As A Configuration]として共通フォーマット定めた方が良い気がしている
        - [Dotfiles](Dotfiles.md)文化に乗っ取ると`.pagename`なんだよな
        - これかなぁ
    - config-remind
        - これはちょっとダサいか
- 文法
    - まとめ

```remind
1030メシ買う
1445そろそろ会議やぞ
```

- ...
    - ...
        - 順不動
        - リスト表記も不要 or パース時に吸収しても良い
    - `(DateRange) (Time) (Message)` この路線だろう
        - ~~DateRangeは「毎日」「一回だけ(Once)」の2つでいい~~毎日さえも要らないな、まずはシンプルにすべき
        - それ以外の細かいリマインドはカレンダーアプリでやればいい
    - `(Time) (Message)` この路線
        - 10:30にリマインド
            - `10:30 会議だしメシ買いに行くか`
        - ~~今から30分後にリマインド~~シンプルにしたいのでいったんなし
            - `30m そろそろメシ買いに行くか`
            - 設定ページでこれ実現するのはきついな
            - or `30m そろそろメシ買いに行くか(from 09:17)` みたいな基準記入が必要になる
    - あとは書き方
        - `10:30 メシ買う`
        - `1030 メシ買う`
        - `1030メシ買う`
        - これは要らんか、一度に2メッセージをリマインドはおかしい

```remind
1030
 メシ買う
 ★このやり方だと一つのtimeに複数のメッセージをぶら下げされる
```

<br>

これがあると何が嬉しい？

- .remindページに「1030メシ」と書いておくだけで、10:30になると「メシ」と表示される
    - Scrapboxから外に出る必要がない
- Q:プライベートなこと書けないのでは？
    - それはある
    - ちょっと極端な例を書くけど
        - 「あ、今日は妻が～～で余裕あるからセックスできそうだ」
        - 「打診しておかないとな」
        - `1120妻とセックス交渉`
    - さすがにこういうのは書けないだろうｗ
    - Aさんのpublic project `/a-public`があるとして、`/a-public/.remind`にこういうことが書かれていたら、まあ引くよね（ひく人がマジョリティだよね）
        - 僕は別に引かないけど
        - むしろ[下ネタを隠す教](下ネタを隠す教.md)から逸脱している点で好感さえ持てる
- Q:public projectにこもっているときはリマインドできないの？
    - できない
    - というより作用範囲は「"このリマインダーを仕込んでいるproject" を開いていること」になる

<br>

背景

- [UserScript](UserScript.md)だけでリマインダーを実現する
- 実装方針
    - UserScriptだけ使う
    - [ゲームループ](ゲームループ.md)つくってインターバルで一致判定する
    - リマインド設定は`.remind`みたいな設定ページに列挙する

<br>

[#開発ネタ](開発ネタ.md)

<br>

## Links
- ← [UserScriptでリマインダーを実現する](UserScriptでリマインダーを実現する.md)

## 2hop Links
- → [ScrapboxでGTD](ScrapboxでGTD.md)
    - ← [UserScriptでリマインダーを実現する](UserScriptでリマインダーを実現する.md)
- → [UserScript](UserScript.md)
    - ← [Scrapboxへの要望](Scrapboxへの要望.md)
    - ← [ScrapCalc](ScrapCalc.md)
    - ← [Scrapbox As A Brarea](Scrapbox_As_A_Brarea.md)
- → [Scrapbox As A Configuration](Scrapbox_As_A_Configuration.md)
    - ← [Scrapbox As A XXXX](Scrapbox_As_A_XXXX.md)
    - ← [Scrapbox As A Matching](Scrapbox_As_A_Matching.md)
    - ← [詰めマイン](詰めマイン.md)
