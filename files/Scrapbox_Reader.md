## Scrapbox Reader
- 対外向け説明
    - [/villagepump/超軽量なScrapboxクライアントを作った](https://scrapbox.io/villagepump/超軽量なScrapboxクライアントを作った)
- 開発者の内部メモ
    - [/yuta0801/Scrapbox Reader](https://scrapbox.io/yuta0801/Scrapbox Reader)
- ソース
    - <https://github.com/yuta0801/scrapbox-reader>
    - パーサー
        - <https://github.com/progfay/scrapbox-parser>

<br>

reading reader

- to markdownの部分に興味がある
- レンダリングはnext.js
    - テンプレートエンジンっぽい
- <https://github.com/yuta0801/scrapbox-reader/blob/master/components/Block.tsx#L37>
    - たぶん
    - scrapbox parser側でjs objectになってるので、
    - それをテンプレート中の適切な場所に埋め込むだけ
    - ってイメージかしら
- ああ、やっぱこのアプローチか
    - リンク部分の再帰
        - <https://github.com/yuta0801/scrapbox-reader/blob/master/components/LinkNode.tsx#L6>

<br>

reading parser

- <https://github.com/progfay/scrapbox-parser/tree/master/src/block>
- やっぱりそうか、木構造つくっていくイメージよな
    - <https://github.com/progfay/scrapbox-parser/blob/master/src/block/Table.ts#L15>
    - <https://github.com/progfay/scrapbox-parser/blob/master/src/block/Line.ts#L14>
    - <https://github.com/progfay/scrapbox-parser/blob/master/src/block/index.ts#L14>
        - entrypoint
        - title, codeblock, table, lineの4つ
    - lineとかcodebolockとか、そういうのは全部オブジェクトにする
    - 1-obj 1-nodeにして、木構造をつくる
    - [Scrapbox to Markdown](Scrapbox_to_Markdown.md)の行指向は修羅の道だよなぁ……:sta:
- :train:しかしNotaのエンジニアだけあってコードもやり方も強すぎる
    - 参考にすれば強くなれそう

<br>

