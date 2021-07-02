## ScrapboxのSEO
まとめ

- ブラウザからアクセス時はService Workerがキャッシュを返してる
    - ここにメタ情報は含まれてない
- ~~直にサーバーに~~Service Workerなしの環境からアクセスすると、メタ情報含んだHTMLが見れる

<br>

詳しい解説

- [/nwtgck/Scrapboxはクローラーに優しく、SEO的にも良い感じなことが分かった](https://scrapbox.io/nwtgck/Scrapboxはクローラーに優しく、SEO的にも良い感じなことが分かった)
- [/shokai/ScrapboxはSEO意外と強い？](https://scrapbox.io/shokai/ScrapboxはSEO意外と強い？)

<br>

:sta:

- [/villagepump/ScrapboxのSEOは強くない](https://scrapbox.io/villagepump/ScrapboxのSEOは強くない)
    - 井戸端に書いたの
    - ページランク高いのは、やはり単にバズってるから説
        - ただしバズりの中では弱い方なので、ネタが一般的すぎると上位に来ない
        - [/nishio/やる気のなくなるコメントの対処法](https://scrapbox.io/nishio/やる気のなくなるコメントの対処法)
            - やる気の対処、はブロガーのレッドオーシャンなのでバズった程度では上位には来ない
        - [/shokai/サーバーサイドレンダリングしないReact SPAのSEO](https://scrapbox.io/shokai/サーバーサイドレンダリングしないReact SPAのSEO)
            - これはReact、サーバーサイドレンダリング、SPAと三重で絞られているのでたぶんブルーオーシャン
- [ここをcurlで取ってみた](ここをcurlで取ってみた.md)見る限りだと、以下が言えそうか
    - 1-line 1-divなのであまり強いページではない
        - 強いページにするにはHタグとか使って「文章っぽさ」を出さないといけない
    - pinned pageから辿れる範囲≒Googleが拾ってくれる範囲
        - なのでpinned pageからproject全部に辿れるように設計してあげれば、拾われやすい
    - が、これは2017年くらいの僕の所感なので、今のGoogleアルゴリズムは違うかもしんない:sta:

<br>

## 2hop Links
