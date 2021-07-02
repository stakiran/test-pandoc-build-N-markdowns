## Scrapbox活用事例集の別アイデア
- 1user 1page
- pageのコンテンツは機械的につくる
    - project name
    - user name
    - user icon
    - project summary
        - ページ数
            - ページ数タグをつける
                - 100, 300, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000+ とか？
                - 100, 500, 1000, 3000, 5000, 10000？
    - 主なページ
        - most linked 上位nを列挙する
        - ブラケティングもする
    - generated_at
- :sta:フォーマット適当に定めて「どう書くかを機械的に定めてしまえば」迷わない、書きやすい（投入しやすい）のではないかとひらめいた
    - 技術的に（≒API的に）できるかは不明だが
    - 最悪愚直にスクレイピングすれば良いと思うけど
- UI
    - たぶん[UserScript](UserScript.md)か[Tampermonkey](Tampermonkey.md)？
    - 「今開いてるprojectのコンテンツをつくるスクリ」を実行する
        - クリップボードにでもコピーすればいい
    - あ、ブックマークレットみたいにやるのは？
        - このフォーマットで投入する個人projectXつくっておいて、
        - project Aでスクリ実行すると、Xに下記サンプルのようなページを挿入する
            - write APIはないから、新規タブで開く + クリップボードにコンテンツコピーで「あとは手作業でペーストしてね」かな
- 用途
    - [Scrapbox活用事例集](Scrapbox活用事例集.md)の一運用として
    - [Scrapboxサーフィン](Scrapboxサーフィン.md)の記録として

<br>

Q&A

- Q: 勝手に掲載されたくない人は？
    - robots.txtじゃないけど「私のprojectは[ディスプレイング](ディスプレイング.md)禁止です」みたいな宣言する
- Q: フォーマット案、アイデアあります？
    - 基本は以下サンプル
        - most linked 上位nを並べることで、主要コンテンツを表現する
        - 並べた各々はブラケティングすることで、project内の繋がりをアシストする
    - most viewed はどう？
        - 個人的には見たい
        - でも[Scrapboxの哲学](Scrapboxの哲学.md)的には微妙（承認欲求刺激する）
- Q: 小説設定資料集の場合はどうなるんです？
    - たとえば[/sta-book15](https://scrapbox.io/sta-book15)のmost linked見せられても意味わからんよな
    - どんな感じの小説かはわかるからいいんじゃない？
        - まあこれは「15番目の本」で小説かどうかさえわからないが
    - Q: 手動でpurposeとか記入可能にするのは？
        - 書きたいなら書いていいけど、あまりおすすめはしない
        - 機械的につくれるという手間の無さが最大の恩恵であって、手動記入入れちゃうと揺らぐ

<br>

[#開発ネタ](開発ネタ.md)

<br>

:hr:

ちょっとサンプル書いてみる（リンクはつけたくないのでリテラルで記載）

<br>

<a href="https://gyazo.com/505861e8a5c21ae87eb972c4affd8841" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/505861e8a5c21ae87eb972c4affd8841/raw)</a>

- Project: [/sta](https://scrapbox.io/sta)
- UserPage: [/sta/sta](https://scrapbox.io/sta/sta)

<br>

project information

- 4296 pages `#4000`
- created at `2020/03`

<br>

main pages

- `[大企業病](大企業病.md)`
- `[創作](創作.md)`
- `[ビジネスネタ](ビジネスネタ.md)`
- `[創作ネタ](創作ネタ.md)`
- `[Scrapbox](Scrapbox.md)`
- `[知的生産](知的生産.md)`
- `[ダンスラ](ダンスラ.md)`
- `[タスク管理](タスク管理.md)`
- `[ランニングマン](ランニングマン.md)`
- `[リーンスタートアップ](リーンスタートアップ.md)`

<br>

genereted at 2021/03/29

<br>

必要ならここに本人があれこれ書いてもいい

他人が何か書いてもいい（ただし（質問などの場合でも）本人が答える義務はない）

<br>

:hr:

[ディスプレイング](ディスプレイング.md)を禁止する例

<br>

[/sta](https://scrapbox.io/sta)をここで紹介することは禁止します

see: [/sta/ディスプレイングは禁止します](https://scrapbox.io/sta/ディスプレイングは禁止します)

<br>

↑ こんなことをsta本人が書いておく

書いておけば、誰かがディスプレイングすることはなくなる

アバターさえ載せるのが嫌なら載せなくてもいい

<br>

## Links
- ← [✅index.mdを自動生成する](✅index.mdを自動生成する.md)
- ← [Scrapbox活用事例集が使いにくい？](Scrapbox活用事例集が使いにくい_.md)

## 2hop Links
- → [Scrapboxサーフィン](Scrapboxサーフィン.md)
    - ← [ScrapBubble](ScrapBubble.md)
    - ← [Scrapboxでリンク先をバルーンでどんどん辿っていく](Scrapboxでリンク先をバルーンでどんどん辿っていく.md)
    - ← [デジタルサーフィン](デジタルサーフィン.md)
- → [Scrapboxの哲学](Scrapboxの哲学.md)
    - ← [このサイトについて](このサイトについて.md)
    - ← [shokai](shokai.md)
    - ← [汎用的なツールとして提供する](汎用的なツールとして提供する.md)
- → [Scrapbox活用事例集](Scrapbox活用事例集.md)
    - ← [知的生産の5つのフェーズ](知的生産の5つのフェーズ.md)
    - ← [知的生産者間のコミュニケーション](知的生産者間のコミュニケーション.md)
    - ← [ディスプレイング](ディスプレイング.md)
- → [UserScript](UserScript.md)
    - ← [Scrapboxへの要望](Scrapboxへの要望.md)
    - ← [ScrapCalc](ScrapCalc.md)
    - ← [Scrapbox As A Brarea](Scrapbox_As_A_Brarea.md)
- → [ディスプレイング](ディスプレイング.md)
    - ← [今日整理したこと](今日整理したこと.md)
    - ← [スタンス表明としてのタグ](スタンス表明としてのタグ.md)
