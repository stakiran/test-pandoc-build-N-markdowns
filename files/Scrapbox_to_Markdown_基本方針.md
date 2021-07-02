## Scrapbox to Markdown 基本方針
bra3 at 2021/04/07

- まとめ
    - [connect.sid](connect.sid.md)は使いたくないので、json用意するところは手作業かな。。。
    - [Scrapbox記法](Scrapbox記法.md) to [Markdown](Markdown.md)の変換処理は、勉強もかねて自製してみる
    - index.mdどう表示させるかがミソやぞ
- 名前迷う
    - scb2mb的な名前は違うと思ってる
        - 単一のscbページをmarkdownにするわけじゃない
        - ghpagesに置けるセットをつくる
    - scrapbox json to markdown
    - scrapbox json to ghpages
- repo設計
    - stakiran/scbjson2ghpages
    - .gitignore
        - *.json
    - docs/
        - テスト用projectでto markdownした結果を載せる
    - config.py
    - convert.py
    - readme.md
    - build.bat
        - docs/ 全部消して
        - python convert.py
- 進め方
    - テストページをつくった小さなprojectをexportしよう
        - [/sta](https://scrapbox.io/sta)だとでかすぎて[TAE効率](TAE効率.md)が悪い
        - [/testdata-for-to-markdown](https://scrapbox.io/testdata-for-to-markdown)
            - :sta:拡充中
- jsonパースは[sbq](sbq.md)が使えそう
- repo迷ってる
    - scbjson2ghpagesにするか、sbq側で to markdown を一通りつくってみるか
    - sbqの話だが
        - to markdownでパーサの範囲超えてるよな
        - 本当に忠実にするなら「sbqでpage lines切り出したデータ」に対してto markdownする、[KISS](KISS.md)みたいなことするべき
        - つまりsbqは「to markdownしやすいつくり」にする
    - とすると、scbjson2ghpagesかな
        - で、sbqコピってきて改造していこう

<br>

bra2

- 指定タグを含むページの一覧
    - `#ビジネスネタ`とか`#創作ネタ`とか欲しい
    - 別観点でソートしたい
        - 文字数、被リンク数 etc

<br>

bra

- [GitHub Pages](GitHub_Pages.md)に公開すればいい
- markdownが必要
- exportしたjsonをmarkdownにする
- 1-page → 1-file に対応付け
- テスト用ページつくるといい
    - yutaさんあたりがつくってた覚えがあるが見つからん
    - :train:[/yuta0801/Scrapboxをソースにした静的サイトジェネレーターを作る案](https://scrapbox.io/yuta0801/Scrapboxをソースにした静的サイトジェネレーターを作る案)
        - その結果、[/yuta0801/Scrapbox Reader](https://scrapbox.io/yuta0801/Scrapbox Reader)に至ったみたい
- scrapboxの語彙力とmarkdownの語彙力は一致しない
    - nested listの中でコードブロック ← これはmarkdownでは不可能
- index.htmlはどうするか
    - 4444ページのリンク並べる？（4444行）
    - paginationする？
    - ランキングは？
        - most linked
        - date modified
        - date created
    - リンク並べる形式にしたいなー
        - 縦長はイヤなので、横にも並べたいかしら
        - 敷き詰める
        - 1行にnページ分並べるとか
            - n=5？
            - n=10？
        - date modified（などランキング観点）でグルーピングする
            - 1day以内に更新された
            - 3day以内に更新された
            - 1w以内に更新された
            - 4w以内に更新された
            - ……
            - ↑ この観点一つごとに1行でリンク並べる
                - 1day以内が7ページあったら、1行に7リンク並ぶ
    - css工夫してカードにするってアイデアもある
    - [JAMstack](JAMstack.md)使えばjsで見た目いじれるんだっけ？
- seoの工夫は？
    - `#xxx` というタグ文字列を検出して、meta keywordsに並べるとか……
- あえて「上位n件だけ表示」にすればいいんじゃね？
    - それ以外のページは、表示されたそいつらからのリンクで辿れる（ことがある） ← こうする
    - 宝探し感覚になるかもしれない
- 自動ビルドさせたいなー
    - 定期的に export to json して、それを to markdown にして push to ghpages
    - github actionsでできるでしょ
    - export to json する scrapbox apiもあったはずだ？
        - importやexportするAPI、どこだろ
        - <blockquote>export, importはScrapbox APIからできる [/programming-notes/scrapbox-sync#6055ae72e5172d00000cbfcd](https://scrapbox.io/programming-notes/scrapbox-sync#6055ae72e5172d00000cbfcd)</blockquote>
        - [/scrapboxlab/APIの書式](https://scrapbox.io/scrapboxlab/APIの書式)
        - [Scrapboxでexport to jsonするAPI](Scrapboxでexport_to_jsonするAPI.md)
        - [Scrapboxでimport from jsonするAPI](Scrapboxでimport_from_jsonするAPI.md)
    - そもそも[PythonからScrapboxのAPIを叩く方法](PythonからScrapboxのAPIを叩く方法.md)がわからん
        - export to json時のowner認証とかどうやるんだ？
- 恥ずかしいコンテンツがネットに残る可能性
    - 既にscrapboxでも残ってる（seoはゴミだが）
    - バズってしまったら？
        - scrapboxでも同じこと
        - スクショされたり魚拓取られたりしたらどうやっても残る
- 実装はこれパクる？
    - <https://github.com/kondoumh/sb2md/blob/master/cmd/md.go>
    - それともあえて自分で頑張ってみる？

<br>

## Links
- ← [Scrapbox to Markdown](Scrapbox_to_Markdown.md)

## 2hop Links
- → [Scrapboxでexport to jsonするAPI](Scrapboxでexport_to_jsonするAPI.md)
    - ← [PythonからScrapboxのAPIを叩く方法](PythonからScrapboxのAPIを叩く方法.md)
- → [KISS](KISS.md)
    - ← [1-neta 1-pageの原則](1-neta_1-pageの原則.md)
    - ← [ツールボックスアプローチ](ツールボックスアプローチ.md)
    - ← [Terraform学習](Terraform学習.md)
- → [JAMstack](JAMstack.md)
    - ← [Gyampっぽいの自作したい](Gyampっぽいの自作したい.md)
- → [TAE効率](TAE効率.md)
    - ← [今日整理したこと](今日整理したこと.md)
    - ← [高速試行錯誤](高速試行錯誤.md)
    - ← [そろそろペインでもタブでもない新しいUIが欲しい](そろそろペインでもタブでもない新しいUIが欲しい.md)
- → [sbq](sbq.md)
    - ← [Scrapbox Editor](Scrapbox_Editor.md)
- → [Markdown](Markdown.md)
    - ← [Obsidian](Obsidian.md)
    - ← [Scrapbox to Markdown](Scrapbox_to_Markdown.md)
    - ← [✅秀丸エディタでScrapbox風味の文法とシステムを実現したい](✅秀丸エディタでScrapbox風味の文法とシステムを実現したい.md)
