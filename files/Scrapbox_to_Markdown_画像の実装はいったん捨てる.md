## Scrapbox to Markdown 画像の実装はいったん捨てる
画像いったん捨てませんか？

- 目的は「ghpagesに公開してみたらどうなるかを手早く試したい」なので素早い方がいい
    - 画像はテキトーなアイコンを決め打ちしつつ、View at scrapboxリンクつけておけば「オリジナルはscrapbox側見てね」にできる
    - [/sta](https://scrapbox.io/sta)はテキストメインなので、たぶん画像はなくても大丈夫
    - :sta:いや、リンクにしちゃえばいいのでは？
        - x `![](https://i.gyazo.com/e4aae2345d1927c777db267138d1e419.jpg)`
        - o `[image](https://gyazo.com/e4aae2345d1927c777db267138d1e419)`
- ~~これ[本心ではもう決めている](本心ではもう決めている.md)っぽいけど、本当にこれでいいか少し寝かせたい~~数時間寝かせた結果、yes
- from
    - <https://github.com/stakiran/scbjson2ghpages/commit/3699779f691c77111337379b35d1bdf3b3bb9c39>
- これ、画像だけでなくて`[url](url.md)`を`[media](url)`に一般化できない？
    - scb記法改めて調べてみる
    - [Scrapboxで書けるmedia系の記法](Scrapboxで書けるmedia系の記法.md)
    - 基本的に`[]`で統一されている
        - 地図は違う
    - :sta:拡張性持たせないとダメだなこりゃ
        - `scb_to_markdown_in_line()`に追加してテストコード使えばよろしい
    - 地図は使ってないしいったんスルー
    - `[MEDIAURL](MEDIAURL.md)`は`[media](MEDIAURL)`にしたい
    - `[link](link.md)`は`[link](link.md)`にしたい
    - できた
- あとはicon記法の撲滅
    - 1
        - `:xxx:` → ``
        - `:xxx:` → ``
    - 2
        - `:xxx:` → `(XXX.ICON)`
        - `:xxx:` → `(XXX.ICON*3)`
    - 3
        - `:xxx:` → `(xxx)`
        - `:xxx:` → `(xxx)`
    - 4
        - `:xxx:` → `:xxx:`
        - `:xxx:` → `:xxx:`
        - [/icons](https://scrapbox.io/icons)のような使い方してたとしたら絵文字としてヒットワンチャンある
        - どうせ文字で示すだけだし、これでいいか？
        - ok

<br>

## Links
- ← [Scrapbox to Markdown](Scrapbox_to_Markdown.md)

## 2hop Links
