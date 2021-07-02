## ScrapboxではLinksや2hop-linkの表示個数をどう制御しているか
2

- と思ったけど、違う
    - たとえば	[/sta/今日整理したこと](https://scrapbox.io/sta/今日整理したこと)や[/sta/知的生産の技術](https://scrapbox.io/sta/知的生産の技術)では1つもつくってない
    - [/sta/井戸端](https://scrapbox.io/sta/井戸端)は表示されてる
        - links48個
- 100は「linksと2hop-linkの合計」に対して、ってこと？
    - linksが97なら、2hop-linkは3までしか表示しないとか
- いや、単純じゃない
    - [/sta/GitHub](https://scrapbox.io/sta/GitHub)
        - 2hop link表示されてないが、[/sta/ルーチンタスク](https://scrapbox.io/sta/ルーチンタスク)の一行をリンクさせたらその分は表示される
        - しかし大企業病では表示されないどころか有効なリンクにさえならない
            - <a href="https://gyazo.com/7caadf15a381a9d76de7a986517b80d0" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/7caadf15a381a9d76de7a986517b80d0/raw)</a>
    - [/sta/能ある日向は爪隠す](https://scrapbox.io/sta/能ある日向は爪隠す)
        - [/sta/Githubのダークモード](https://scrapbox.io/sta/Githubのダークモード)を書くと、これも表示される
        - しかし[/sta/GitHub](https://scrapbox.io/sta/GitHub)では表示されない
    - わからんですねぇ……:sta:

<br>

1

- Q: Scrapboxはどうしてるんだっけ？
- 1: linksが100以上の場合は表示しない
    - たとえば[/sta/自分汎用デザイン](https://scrapbox.io/sta/自分汎用デザイン)だと
        - linktoはドッグフーディング、ぼっち、大企業病の3つ
        - 2hopとして表示されてるのはドッグフーディングとぼっちのみ
        - ああ、そういえば「でかすぎるリンクは省く」って言うてた気がする:sta:
            - 大企業病はハッシュタグ的で毛玉だもんな、ここでは
    - [/sta/大企業で働く理由](https://scrapbox.io/sta/大企業で働く理由)
        - ですわ
        - 上位n個というより、でかすぎるリンクを弾いてる
        - 何個？
            - ぼっちは（俺の計算によると57links）だが、表示されてる
            - 100？
            - としたら[/sta/知的生産](https://scrapbox.io/sta/知的生産)はまだ表示されるはず
            - [/sta/noratetsu](https://scrapbox.io/sta/noratetsu) ビンゴ
                - <a href="https://gyazo.com/09b1c00f8810e1682fb46438efa937d6" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/09b1c00f8810e1682fb46438efa937d6/raw)</a>
            - たぶん100だと思う:sta:
- 2: A.linktoの個数は？
    - 制限なさそう
    - [/sta/大企業病](https://scrapbox.io/sta/大企業病)
        - <a href="https://gyazo.com/c3291501e19e16aed4bf745becd0c36a" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/c3291501e19e16aed4bf745becd0c36a/raw)</a>
        - pagenationの単位は50っぽい
        - いや、...押したら残り全部(50よりでかくても全部一気に)表示する感じだわ
        - ~~いや、159個まで？~~関係ない
            - 大企業病は204
            - 知的生産の技術は159
    - まあ俺のはテキストリンクだし、全部出してもええか:sta:

<br>

## Links
- ← [✅Linksに相当するFooterをつける](✅Linksに相当するFooterをつける.md)

