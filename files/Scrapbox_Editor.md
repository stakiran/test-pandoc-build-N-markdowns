## Scrapbox Editor
**[sta.icon**[sbq]でやります]

<br>

<br>

- 以下のようなことがしたい
    - uglyマークをつけたページを一気に削除する
        - [taint](taint.md)
    - 全ページをまたいだ置換
    - 行数、文字数、リンク数など数値データのビジュアライズ
- どうするか？
    - エクスポートしたjsonをいじるしかあるまい
    - 必要なら「加工後のjson」も出力して、こいつをインポートせい、にする

<br>

- :sta:直近欲しいのが「（転職活動のために）このScrapboxから醜いページを消したい」「でもそいつらもせっかく書いたものなので保持しておきたい」
    - このEditorがあればできる
        - uglyマークで消す
        - 消したのを別jsonに出しておく
        - :sta:これ無理だった
            - ページAが存在する場合、json側でAを消してインポートし直してもAは消えない（当たり前だが
            - 一度つくったページを import 操作で消す手段はない

<br>

- I/F
    - 自分用ならPythonでCLI
    - もうちょっとグラフィカルな操作が必要そうなら、jsonを適当にjs化した上で、フロントエンドで処理する

<br>

## Links
- ← [sbq](sbq.md)

## 2hop Links
- → [sbq](sbq.md)
    - ← [Scrapbox to Markdown 基本方針](Scrapbox_to_Markdown_基本方針.md)
- → [taint](taint.md)
    - ← [Terraform学習](Terraform学習.md)
