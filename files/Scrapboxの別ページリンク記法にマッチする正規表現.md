## Scrapboxの別ページリンク記法にマッチする正規表現
linktoのみ検出したい

<br>

- o
    - [リンク](リンク.md)
    - [リンク](リンク.md)と[リンク](リンク.md)
- x
    - `[りんく](りんく.md)`
    - **太字**
    - **太字**
    - ~~斜体~~
    - [存在しないリンク](存在しないリンク.md)
    - [/sta](https://scrapbox.io/sta)
    - [google(text後)](http://www.google.co.jp)
    - [google(text前)](http://www.google.co.jp)
    - <a href="https://gyazo.com/505861e8a5c21ae87eb972c4affd8841" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/505861e8a5c21ae87eb972c4affd8841/raw)</a>
    - :sta:
- [Repl.itでPythonの正規表現reを試す](Repl.itでPythonの正規表現reを試す.md)

<br>

うーん……

- 一つの正規表現だけで頑張るのは無理がありそう
- n個の正規表現使った方がいいか
    - xの方を除外する正規表現を複数用意して、判定したいline（のコピー）を書き換える
    - で、最後に、そのコピーに対して、シンプルに`[xxx](xxx.md)`を探す正規表現を使う
- これ使う？
    - <a href="https://gyazo.com/de8a245a5c67b82f945649fa508e37a8" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/de8a245a5c67b82f945649fa508e37a8/raw)</a>
    - が、問題が二点
    - 1 そもそも他から使えるようI/F整えてない
        - ここに書くのも違うし
    - 2 これは to markdown 用の正規表現であって、純粋にscb記法のリンクを取りたい場合とは文脈が違う
        - たとえばRE_LINK_ANOTHER_PAGEは、（既にmarkdown記法のリンクに変換された後に生成される）`[](`の`(`の存在を前提とした表現になっている
- もうこれ愚直にparseした方が早くね？
    - いや、状態遷移ゲーはもうこりごり。。。
- 実装し直すかー
    - <https://github.com/stakiran/scbjson2ghpages/commit/39f0ba9adafc4ecafbc327f5febecfe93b6620c1>
- 粗いけどいったんdone

<br>

いやハッシュタグがまだ

- そして難しい

```py
RE_HASHTAG = re.compile(r'( |^|\n|\r)#(.+?)( |$|\n|\r)')
```

- ...
    - これだと`#hash [#hash`みたいにスペース区切りで連続してるケースをキャプチャできん](hash`みたいにスペース区切りで連続してるケースをキャプチャできん.md)
    - どうすれば
    - `\b`？
        - <blockquote>単語の境界。これはゼロ幅アサーションで、単語の始まりか終わりにのみマッチします。単語は英数文字のシーケンスとして定義されます、つまり単語の終わりは空白か非英数文字として表われます。 [正規表現 HOWTO — Python 3.9.4 ドキュメント](https://docs.python.org/ja/3/howto/regex.html)</blockquote>
        - たぶんこれだ
        - あ、でも日本語も非英数文字なのでダメかな

```py
RE_HASHTAG = re.compile(r'\b#(.+?)\b')
```

- ...
    - ...
        - だめ

```py
RE_HASHTAG = re.compile(r'( |^|\n|\r|\b)#(.+?)( |$|\n|\r)')
```

- ...
    - ...
        - これだと`あああ#ここは検出されない`も検出されてしまう
    - ドキュメント見ても無さそうだが
    - 先読みアサーション？
        - <blockquote>(?=...)</blockquote>
        - <blockquote>肯定先読みアサーション。 ... で表わす正規表現が現在位置でマッチすれば成功し、それ以外の場合失敗します。しかし、表現が試行された場合でもエンジンは先に進みません</blockquote>
        - エンジンを先に進ませないんだよな、つまりは

```整理
今起きてるの
 aaa #hash1 #hash2 aaa
    ^^^^^^^^
 aaa #hash1 #hash2 aaa
            ^
          エンジンはここからスタートしてしまう
          しかし #(.+?) みたいな表現にすると aaa#aaa こういう文字列もヒットしてしまう
```

- ...
    - ...
        - んー、ちょっとわからん
- ググる
    - [Python - Python 正規表現で適切にハッシュタグを抽出したい｜teratail](https://teratail.com/questions/299251)
        - ダメ。`aaa#aaa`もヒットしちまう
    - 他にヒットした記事も同じ感じでうーん:sta:
- 仕方ない、プリプロセスで対処する

```プリプロセス対象の考察
#hash
#hash #hash
#hash aaa #hash
#hash #hash #hash
     ^^    ^^
```

- ...
    - ` [#`を`](`を`.md)  [#`などに変えてしまう、が思いついたんだが](`などに変えてしまう、が思いついたんだが.md)
        - 原意削がれないよな？
- 対応してみた
    - <https://github.com/stakiran/scbjson2ghpages/commit/603868e64d57e9e09a94f5976981382e4c620d18>
    - 実装がエレガントじゃなくて[不吉な臭い](不吉な臭い.md)するけど。。。:sta:

<br>

まだ

- codeの中身を弾く

<br>

## Links
- ← [✅Linksに相当するFooterをつける](✅Linksに相当するFooterをつける.md)

## 2hop Links
