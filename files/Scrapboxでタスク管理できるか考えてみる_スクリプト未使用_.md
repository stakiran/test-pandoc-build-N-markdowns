## Scrapboxでタスク管理できるか考えてみる（スクリプト未使用）
- 「Scrapboxだけ使ってタスク管理をしなければなりません」としたら
- まずは実行日の概念
    - [2020/06/04](2020_06_04.md)みたいなページをデイリーリストにする
    - [2020/06/05](2020_06_05.md)
- タスク
    - せっかくならページ持たせたいよな
    - 入力補完で再利用性＆入力簡略化できそう
- ルーチンタスク
    - ページ名に属性を持たせる
        - @3
        - セクションは？
            - a 午前
            - b 昼休憩
            - c 午後前半
            - d おやつタイム
            - e 午後後半
            - f 撤収
            - g 夜休憩
            - h 就寝前フリー
            - z いつでも
        - [@3 a 洗濯](@3_a_洗濯.md)
        - [@3 a 掃除 床 トイレ](@3_a_掃除_床_トイレ.md)
        - [@3 a 掃除 床 リビング](@3_a_掃除_床_リビング.md)
        - [@3 z 掃除 机 ほこり](@3_z_掃除_机_ほこり.md)
- 終了操作
        - [@3 a 洗濯](@3_a_洗濯.md)
    - ↓ complete
        - ~~[@3 a 洗濯](@3_a_洗濯.md)~~ `~~[@3 a 洗濯~~(@3_a_洗濯.md)]`
        - ~~@3 a 洗濯~~ `~~@3 a 洗濯~~`
        - [@3 a 洗濯](@3_a_洗濯.md)] `[@3 a 洗濯](@3_a_洗濯.md)]`
        - [[@3 a 洗濯]([@3_a_洗濯.md)] `[[@3 a 洗濯]([@3_a_洗濯.md)]`
        - ~~@3 a 洗濯~~] `~~@3 a 洗濯~~]`
        - ~~[@3 a 洗濯~~(@3 a 洗濯.md) `~~[@3 a 洗濯~~(@3 a 洗濯.md)`
    - 正解
        - todo
            - - [@3 a 洗濯](@3_a_洗濯.md)]
                - こっちが打ちやすいかな
            - [ [@3 a 洗濯](_[@3_a_洗濯.md)]
        - done `~~[@3 a 洗濯~~(@3 a 洗濯.md)]`
            - ~~[@3 a 洗濯](@3_a_洗濯.md)~~
    - `- [@3 a 洗濯](@3_a_洗濯.md)]` これを手で打つのはしんどい
        - [UserScript](UserScript.md)でAdd Task的な操作を用意してやる
            - possible?
                - yes!
                    - <a href="https://gyazo.com/d86fdcf9b38ec0a3b1bdc1161b1d488a" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/d86fdcf9b38ec0a3b1bdc1161b1d488a/raw)</a>
                    - `.cursor-line`でselectできる
                    - insert時はちょっと煩雑
                        - <a href="https://gyazo.com/4e326876b592bb480067762a8c618748" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/4e326876b592bb480067762a8c618748/raw)</a>
                        - spanタグ一つに1文字
                - [console.log(scrapbox)](console.log(scrapbox).md) scrapbox objではダメね
                - クリップボード？ [クリップボードとのやりとり - Mozilla - MDN](https://developer.mozilla.org/ja/docs/Mozilla/Add-ons/WebExtensions/Interact_with_the_clipboard)
                - keypush?
                    - [javascript - Is it possible to simulate key press events programmatically? - Stack Overflow](https://stackoverflow.com/questions/596481/is-it-possible-to-simulate-key-press-events-programmatically)
                        - 無理やりそうで動くかわかんねぇ
    - `- [★]](★].md)`
        - ★にカーソル
        - ちゃんと補完きく
- 一日のデイリータスクリスト組み立て
    - その日のデイリーページつくる
    - タスク列挙
    - ルーチンタスク列挙
        - ここがだるいよなぁ
        - @3 とかだとカウントできない
        - 曜日固定？
            - [wed トイレ 掃除](wed_トイレ_掃除.md)
            - これだと水曜固定になるが
                - いや、木曜のデイリーページから補完して書くってのもできる
            - @2ならたとえば木土にして[thu トイレ 掃除](thu_トイレ_掃除.md)と[sat トイレ 掃除](sat_トイレ_掃除.md)をつくっておくとか
            - トイレ掃除をfriにしたい
                - [fri トイレ 掃除](fri_トイレ_掃除.md)つくればいいさー
                - で、各タスクページみたら「何月何日にリストに入れたか」が全部見える
            - 水曜のページだと機械的に wed- と打ちたいよな
                - いや we- でいい
        - 曜日prefixでいけそうやぞ
- ★続きここから

<br>

**3**

- TODOリストとしての使用に落ち着きそう？
    - [Scrapbox上でルームツアーやってみる Ver4.0](Scrapbox上でルームツアーやってみる_Ver4.0.md)で試しに
    - <a href="https://gyazo.com/0c93ced160579189e4e45714e656afb8" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/0c93ced160579189e4e45714e656afb8/raw)</a>
    - あと `]` を書くだけで strike out になるわけよ

<br>

**2**

- 記録ベースにするなら
    - 06:26:45 タスクA
    - 06:26:49 タスクBをした この時間はつらい
    - 06:26:59 タスクC 
    - ……
- デイリーログをベースにするのがやりやすいかも
    - taskchuteみたく家事など些細なことの管理はやめる
    - これ、もろ[日記の魔力](日記の魔力.md)読んでて思いついたやつなんだがｗ
- こうか？
    - 計画的タスク管理……宣言的。いつ何をやるか、後で何するかを先に入れておく。
    - 記録的タスク管理……報告的。やったことを簡潔に記録し、あとでやるレビューや内省の材料にする。

<br>

**1**

- [#Scrapbox](Scrapbox.md) で [#タスク管理](タスク管理.md) 、考えてみたら面白そう
- ~~script？使ったら [#Tritask~~(Tritask.md) 的な行指向できそうだが](-#Tritask]_Tritask.md) 的な行指向できそうだが.md) いったん手作業オンリーを想定する
- アウトライナーでやるみたいになるのかなぁ……
- バレットジャーナル
- 本質的には手作業で [DWMY](DWMY.md) なエリアをつくってる
- Scrapbox の性質
    - プロジェクト
    - ページ
    - リスト
    - リンク
    - code
    - 同時編集ができる
        - パートナータスク管理しやすそう
        - Slack 夫婦で使ってる、の Scrapbox 版
            - Slack はフローなやり取りメイン
            - Scrapbox はストックなやり取りメイン？
- ルーチンタスク
    - ページにストックしていたのを毎日デイリータスクリストにコピペ？
    - 前日のデイリータスクリストを見て「これ要るわ」な分を今日のリストにコピペ？
    - テーブルつくったら「家事当番テーブル」みたいな感じで実現できないか？
        - [ルーチンエリア](ルーチンエリア.md)
        - table:routines

|  |  |  | ↓ |  |  |  |  |  |
| - | - | - | - | - | - | - | - | - |
| taskname | 毎日 | 月 | 火 | 水 | 木 | 金 | 土 | 日 | やった人 |
| routine1 | * |  |  |  |  |  |  |  |  |
| routine2 |  | * |  |  | * |  |  |  |  |
| routine3 |  | * |  |  |  | * |  |  |  |
| routine4 |  | * | * | * | * | * |  |  |  |
| routine5 |  |  |  |  |  |  | * | * | :sta: |
| routine6 |  |  | * | * | * |  | * |  |  |

- ...
    - ...
        - ↑ こんな感じであらかじめつくっておく
        - ページにストック、の「テーブルで書いておく」版か
        - 今日は目印として `↓` でも書いておけばいい
        - 惜しい、アイコンまではかけねえかー
- `-` つけるだけで todo リストできる？
    - `[ todo](_todo.md)` ダメ。リンクになる
    - `[-0 todo]` 0 を消せば打ち消し線になる
        - 何文字だと一番いい？
        - [-0 todo]
        - [-= todo]
        - [-todo]
            - 間にスペース入れて打ち消しできる
            - が、リンクになっちゃうな
        - [- todo
            - これは？
            - 終わったら末尾に `]` つけるだけでいい
                - ---- 画像 ----
                - <a href="https://gyazo.com/2d260e0ddd0204c846bab6c59fbe12df" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/2d260e0ddd0204c846bab6c59fbe12df/raw)</a>
                - ---- 画像 ----
            - 先頭も `[` がついてるので視覚的に todo だとわかりやすい

<br>

**0**

- :sta:ちょっとガチりたい
    - タスク管理じゃない情報蓄積ツール上でタスク管理を実現する
    - いわばタスク管理システムの[DIY](DIY.md)ともいうべき考え方
        - いや[DDIY](DDIY.md)か
- 違うかも
    - 「n種類のタスク」セット
    - これをどのように管理するかを考えることで、色んなシステムを想定することができる的な

<br>

<br>

## Links
- ← [Scrapboxでタスク管理](Scrapboxでタスク管理.md)

## 2hop Links
- → [DDIY](DDIY.md)
    - ← [ガラケーどうする](ガラケーどうする.md)
    - ← [家計簿をDDIYする](家計簿をDDIYする.md)
    - ← [連番を自動生成したい](連番を自動生成したい.md)
- → [タスク管理](タスク管理.md)
    - ← [ScrapboxだとExpose my lifeが加速できる気がする](ScrapboxだとExpose_my_lifeが加速できる気がする.md)
    - ← [タスク管理の体系化](タスク管理の体系化.md)
    - ← [不発](不発.md)
- → [Scrapbox上でルームツアーやってみる Ver4.0](Scrapbox上でルームツアーやってみる_Ver4.0.md)
    - ← [デスク1](デスク1.md)
    - ← [僕のミニマリズム](僕のミニマリズム.md)
    - ← [ルームツアー日記](ルームツアー日記.md)
- → [UserScript](UserScript.md)
    - ← [Scrapboxへの要望](Scrapboxへの要望.md)
    - ← [ScrapCalc](ScrapCalc.md)
    - ← [Scrapbox As A Brarea](Scrapbox_As_A_Brarea.md)
- → [日記の魔力](日記の魔力.md)
    - ← [タスクランチャー](タスクランチャー.md)
    - ← [知的生産入門者のための「知的生産のABCD」](知的生産入門者のための「知的生産のABCD」.md)
    - ← [航海日誌スタイル](航海日誌スタイル.md)
- → [console.log(scrapbox)](console.log_scrapbox_.md)
    - ← [takker-tritask-scrapboxの実装を読む](takker-tritask-scrapboxの実装を読む.md)
    - ← [tritask-scrapboxの初期検討残骸](tritask-scrapboxの初期検討残骸.md)
- → [DIY](DIY.md)
    - ← [面白ければなんでもあり　発行累計6000万部――とある編集の仕事目録](面白ければなんでもあり_発行累計6000万部――とある編集の仕事目録.md)
    - ← [充電ケーブル類をぶらさげて保管したい](充電ケーブル類をぶらさげて保管したい.md)
    - ← [じぶんリリースノート 0.32.10](じぶんリリースノート_0.32.10.md)
- → [DWMY](DWMY.md)
    - ← [締切制約](締切制約.md)
    - ← [起承転結](起承転結.md)
    - ← [Habitica](Habitica.md)
- → [ルーチンエリア](ルーチンエリア.md)
    - ← [scrapbox-routinearea](scrapbox-routinearea.md)
