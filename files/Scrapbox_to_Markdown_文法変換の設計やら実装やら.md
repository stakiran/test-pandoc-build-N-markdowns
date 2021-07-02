## Scrapbox to Markdown 文法変換の設計やら実装やら
[PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現](PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現.md)

<br>

impl4

- 各行の文法変換 with たぶん正規表現ゲー
    - どうしよう
        - 答えは既に先人がたくさんつくってるけど
        - あえて自分で書いてみるか

```py
def scb_to_markdown_in_line(line):
    return line
```

- ...
    - ここまではつくった
        - あとはこの中を増やしていくだけ
    - やっぱ正規表現しかないよなぁ
        - n回の出現を全部replaceしたいもの
        - import reの使い方いっつも迷ってる
        - [tfl](tfl.md)で使ってた
        - [Repl.it](Repl.it.md)で試~~そうとしてるんだけど、ログイン必須になってない？~~
            - ~~jsからアクセスしてPython選んだらいけるようになった~~
            - ~~意味不明~~直った
    - [PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現](PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現.md)
        - こっちでやりまふ
        - ok
- 最後に`<br>`が入る問題は？
    - last blank lineの違いだった
    - <a href="https://gyazo.com/e45eff19dd2ffe18da9d1ac219ca3293" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/e45eff19dd2ffe18da9d1ac219ca3293/raw)</a>
    - 152行目
    - これがあると入る
    - ないと完全一致することを確認した
    - 今はテストデータに入れてるので、expect側もbr入れるべきか

<br>

impl3

- 行指向の変換アルゴリズム、大体掴んだので次こそ実装していくよー
- :train:[Markdownの挙動調べてると1日30commitすぐに超える]
- 行判定部分つくりこんでる
    - デバッグで辿り着ける自信がないので足元から固めていく作戦
    - [impl](https://github.com/stakiran/scbjson2ghpages/blob/25c404a422f859a8ec4cb6ff7b4d672a07816592/lib_scblines2markdown.py)
    - [testcode](https://github.com/stakiran/scbjson2ghpages/blob/25c404a422f859a8ec4cb6ff7b4d672a07816592/test_lib_scblines2markdown.py)
    - :sta:この後が重いなー
- がー、状態ちゃんと設計しないとダメそう
    - オートマトン書いた方がいいかな
    - 状態
        - s: start
        - in-P: in paragraph
        - in-L: in list
        - in-B: in block
    - 遷移（矢印）
        - b: blankline 現在行は空行です
        - p: 段落です
        - l: リストです（深さ変わってません）
        - l+: リストです（深さ増えました）
        - l-: リストです（深さ減りました）
        - c: codeの始まりです（リストかもしれないし段落かもしれない）
        - t: tableの始まりです（リストかもしれないし段落かもしれない）
    - せっかくだからDrawingで書いてみるか
        - <a href="https://gyazo.com/d5d2c6327e5075bce45c1822b6056976" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/d5d2c6327e5075bce45c1822b6056976/raw)</a>
        - とりあえず状態が足らん（`l-`遷移を二箇所書くという二歩みたいなことしてるｗ
            - in-L に in-L(1) と in-L(2+) が要る
            - in-B に in-B(1) と in-B(2+) が要る
            - EOFに来た時（次行がない）も考慮要
        - :train:くそしんどい
            - 今回は上手く入ったけど、レイアウト的に入らない場合に書き直しになってしまう
            - そして俺には頭の中でレイアウトのあたりをつける能力はない
            - ので実質運ゲー
    - オートマトンをどうやってコードに落とせばいいかもわからん
        - [デザインパターン](デザインパターン.md)使えばいいんだっけ？
            - Stateパターンとか？
    - 愚直に実装すればいいよな
    - 実装するからにはちゃんと図つくってそのとおりに実装しないと後で死ぬ
        - 整合性が取れないとコード愚直に読んでデバッグするゲーになってしまう
- 待った
    - これ、状態なんか導入しなくても「インデントの深さ」一つだけ持っておけば済まない？
    - 要するにインデントの変化を見ればいい（N>=2とする）
        - 0 to 1
        - ~~0 to N~~ややこしいのでいったん考えない
        - 1 to 0
        - N to 0
        - 1 to N
        - N to 1
        - N to N+1
        - N to N-1
    - いや、「インデントの深さ」と「空行」の二つだな（N>=1とする）
        - 0 to N
        - N to 0
        - N to N+1
        - N to N-1
    - 再載
        - scbの段落行の前後には  `\n` を入れる
            - scbの段落行と段落行の間には `\n` が必要
            - scbの段落行とリスト行の間にも `\n` が必要
        - 空行は`<br>\n`に置換する
        - リスト行が終わった場合は `\n` が必要
            - （リスト行の次が空行だった場合は実質`\n<br>\n`となる）
- :sta:んー、スマートに全体像掴む見方が浮かばん
    - 最悪てきとーにつくりながら手探りで潰していく、だけど突貫的になるのでできればやめたい
- 空行解釈とインデント解釈を分けた方が良い気がする
    - input: `scblines[]`
    - output: `markdownlines[]`
    - まずは空行解釈する
        - 空行は `<br>\n` にする（ `['<br>', '']('_br_',_''.md)`）
    - インデント解釈では
        - 追加挿入のバリエーションだけ洗い出しておく
        - ---
        - 追加しない
        - ブロックの終わりを挿入する（`['｀｀｀']('｀｀｀'.md)`）
        - `\n`を挿入する（`['\n']('_n'.md)`）
    - ↑ うん、だいぶシンプルになった
        - 追加挿入が計4パターン（1+3）しかない
- 書いていきやしょ
    - step1: 空行の処理
        - input: scblines[]
        - output: outlines[]
            - scblineのうち、空行部分を`['<br>', '']('_br_',_''.md)`に置換したもの
    - step2: インデントの深さ変更に伴う挿入処理
        - input: lines[]
        - output: outlines[]
            - 以下が余分に挿入されている
                - `\n`
                - ブロックの終わり
        - こいつはprevを必要とする
    - step3: 各行の置換
        - input: lines[]
        - output: markdownlines[]
            - 文字装飾系（これは正規表現が良い）
- 書いてく
    - `python scbjson2ghpages.py -i testdata-for-to-markdown.json > actual_page.md`
    - これでexpect_page.mdと見比べながら泥臭く直していく
- `def judge_extra_insertion(cls, mode_of_prevline, mode_of_curline):`
    - モードじゃなくて「インデントの深さ」が良さそう（昨日の考察）
    - ただし`<br>`はすでに入ってるので無視してねー
    - ★1
        - リストやテーブルの場合、add \n で良い
        - コードブロックの場合、add `｀｀｀`
    - ★2
        - リストの場合、ingnore
        - ブロックの場合、かつ start line のインデントより深い場合、ignore
        - ブロックの場合、かつ start line のインデント以下の場合、:sta:このへんちょっと短期記憶追いつかん。。。
    - table:patterns

| curlineのインデント数 | prevlineのインデント数 | どう解釈すべき？ | 備考 |
| - | - | - | - |
| 0 | 0 | ignore | 空行または段落が続いている |
| 0 | 1 | ★1 | リスト or ブロックがおわた |
| 0 | 2+ | ★1 | リスト or ブロックがおわた |
| 1 | 0 | add \n | リスト or ブロックがはじまた |
| 1 | 1 | ignore | リスト or ブロックが続いてる |
| 1 | 2+ | ignore | リストが深くなった or ブロックが続いている |
| 2+ | 0 | ★1 | リスト or ブロックがおわた |
| 2+ | 1 | ★2 | リストが浅くなった or ブロックが続いてる or ブロックがおわた |
| 2+ | 2+ | ignore | リスト or ブロックが続いている or 深くなった |

- ...
    - ★1にせよ★2にせよ
        - 以下がいる
                - 現在特定のブロックに入っているかどうか
                - 入っている場合、何のブロックか（code or table）
                - 入っている場合、そのスタート時点のインデントの深さ
    - 以上を踏まえると、
        - bf: `def judge_extra_insertion(cls, mode_of_prevline, mode_of_curline):`
        - af: `def judge_extra_insertion(cls, prev_indentdepth, cur_indentdepth, inblock_state):`
        - class InBlockState
            - is_in_block
            - mode
            - indentdepth_of_start
    - あとは上記テーブル分の条件分岐をひたすら並べるだけだー
        - 綺麗に書きたい誘惑があるが、いったんあとで
- step2の一部まで実装してみた
    - <a href="https://gyazo.com/aefc3348957090544542361011f34781" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/aefc3348957090544542361011f34781/raw)</a>
        - 条件分岐の羅列！
        - [ガード節](ガード節.md)でせめてリーダブルにするくらいしか思いつかなかった
    - けど、全然expectに一致しない:sta:
    - 根気強くデバッグしていくフェーズ突入。。。
    - step1時点のoutも欲しいかもな:sta:
    - <a href="https://gyazo.com/65e0042988469344565099857807c22a" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/65e0042988469344565099857807c22a/raw)</a>
        - step1で `[''](''.md)` を `['<br>', '']('_br_',_''.md)`にしている（下方向にだけ空行入れてる）
        - っつーことは、全過程において「下方向に挿入する」で統一性持たせないといけない
            - たぶんどっかで統一ずれてる
        - or step1 で`['', '<br>', '']('',_'_br_',_''.md)`みたいに前後に空行入れてしまうか
    - 修正ok
- が、新たな問題が
    - prev indent depth と current indent depthだけで状態遷移網羅できる設計だが、そんなことはなかった
    - 空行かどうか、の prev と current も要る
    - step1, 2に分けたの間違いだったかしら……
    - メタで処理することで回避
        - <a href="https://gyazo.com/3f0b41d9e911d776a1316e818d814063" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/3f0b41d9e911d776a1316e818d814063/raw)</a>
- ★1の実装
    - inblockstate使います
    - inblockstateだけだときついのでwrapperつくった
        - <a href="https://gyazo.com/fdc04a0eb426149dcbcccf4e580488ee" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/fdc04a0eb426149dcbcccf4e580488ee/raw)</a>
        - あー、これ[未来の自分という他人](未来の自分という他人.md)もわからなくなるにほひ
            - テストコードはあるからホワイトボックス的な挙動確認はできる
            - ただ中身を理解しようとすると苦労しそうな気がする
            - :sta:**「未来の僕へ。たぶんコードだけで理解するのきついんで、このscrapboxページ読んで設計思い出してちょ」**
    - ok、だいぶ一致してきた
        - <a href="https://gyazo.com/767b63b3c2d1d253a73b3735b82c016d" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/767b63b3c2d1d253a73b3735b82c016d/raw)</a>
- ★2の実装
    - テストデータまだだから確認できてないけど、実装はおわた

<br>

impl2

- 実装していくよー
- 境界という概念がある
    - インデントが一段上がった → 記法のおわり
        - コードブロック
        - テーブル
- 空行の意味
    - 露骨な例

```scb
段落

 リスト
 リスト

 リスト
```

- ...
    - ...

```対応するmarkdown
段落

<br>

- リスト
- リスト

<br>

- リスト
```

- ...
    - 塊

```scb
段落
 リスト

 リスト
段落
```

- ...
    - ...

```md
段落

- リスト

<br>

- リスト

段落
```

- ...
    - 段落のバリエーション

```scb
段落1
段落2

段落3

段落4
段落5
```

- ...
    - ...

```md
段落1

段落2

<br>

段落3

段落4

段落5
```

- ...
    - リストのバリエーション

```scb
 リスト
 リスト
 
 リスト
  リスト
 
 リスト
```

- ...
    - ...

```md
- リスト
- リスト

<br>

- リスト
    - リスト

<br>

- リスト
```

- ...
    - 空行のバリエーション
        - [Markdownでn行分の空行を表現する](Markdownでn行分の空行を表現する.md)

```scb
段落

段落 差1


段落 差2



段落 差3
```

- ...
    - ...

```md
段落

<br>

段落 差1

<br>

<br>

段落 差2

<br>

<br>

<br>

段落 差3
```

- ...
    - つまり？
        - scbの段落行の前後には  `\n` を入れる
            - scbの段落行と段落行の間には `\n` が必要
            - scbの段落行とリスト行の間にも `\n` が必要
        - 空行は`<br>\n`に置換する
        - リスト行が終わった場合は `\n` が必要
            - （リスト行の次が空行だった場合は実質`\n<br>\n`となる）
- 変換時には状態という概念がある
    - つまりn行目の変換はn行目の内容だけで完結する**とは限らない**
        - n-1行目、n+1行目の内容が必要（なことがある）
    - もっというと
        - ここまでのパース時の状態を保持しておく必要がある
            - たとえば「今はリストをパース中でーす」とか
        - 次行が何の行かを見に行かねばならないかもしれない
            - 例浮かばないけど
- モード
    - ある行が何を表すか
    - 例: 空行、段落、リスト(indent=1)、リスト(indent=2)、codeblock開始、table開始 etc
- 状態
    - prev mode …… 前行のモード
    - current mode …… 現在行のモード
    - prevとcurrentを使えば、変換後に挿入する追加処理も決まる
- 表でまとめてみる
    - 空行、段落、リスト1、リスト2、codeblockの5つでいいか
    - table:状態遷移？

| prev | current | 行の間に何が必要か（何も必要ない、は - で示す） |
| - | - | - |
| 段落 | 段落 | \n |
| 段落 | 空行 | \n |
| 段落 | リストn | \n |
| 段落 | codeblock | \n |
| 空行 | 段落 | \n |
| 空行 | 空行 | \n |
| …… |  |  |
| リスト | 空行 | \n |
| リスト | 段落 | \n |
| リスト1 | リスト2 | - |
| リスト2 | リスト1 | - |
| リストi | リストi | - |
| リスト | codeblock | - |
| codeblock |  |

- ...
    - あれ、これほぼ`\n`じゃね？
- むしろ`\n`じゃないのってなに？
    - 連結してる文法
        - リスト
        - codeblock内
        - table内
    - 上に追加する
- あー、codeblockやtableの中に、さらにリストがあるんだ
    - 「リスト in the block」みたいなモードがある
    - indent=3でスタートすると、リスト in the blockモードは「indent=3以下」の行にぶち当たるまで続く
    - :sta:ぶちあたった時に何挿入するかで分岐があるな
        - スタート時点でリストに入ってた場合、何も挿入しなくていい
        - が、markdownではそもそもリスト中のブロックなんて概念がないから、これはできない
    - Q: リスト中のブロックという表現を見かけたら、どう変換するの？
        - インデント殺してゼロインデントで表現するしかないかー
    - [Markdownではリスト中のコードハイライト（とテーブル）を表現できない](Markdownではリスト中のコードハイライト_とテーブル_を表現できない.md)
        - 把握した

<br>

impl1

- sbq直した
    - <a href="https://gyazo.com/452a2ccd6cea13bf7f82171a167ae2d7" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/452a2ccd6cea13bf7f82171a167ae2d7/raw)</a>
    - 既にsbqでProjectやPageといったクラスがある
    - to markdownは、Page.to_markdown() みたいに実装してやればよい
- [/testdata-for-to-markdown/page](https://scrapbox.io/testdata-for-to-markdown/page)を正しく変換しきる
- 変換処理どうしようかな
    - 正規表現がベターなんだろうけど
    - 既にsbq parserが行指向になってしまっている……
    - ~~直感だけど、空行の有無による微調整必要そうだから、行指向で泥臭くしないといけない気がしないでもない~~ これはyes → [Markdownの「リストと段落の塊」の表現力が弱い件](Markdownの「リストと段落の塊」の表現力が弱い件.md)のカバーが必要
        - <a href="https://gyazo.com/777cf34172725fb255eaf37c28ed2752" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/777cf34172725fb255eaf37c28ed2752/raw)</a>
        - <a href="https://gyazo.com/c826bdb27383e5f11feae60d116cb1bc" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/c826bdb27383e5f11feae60d116cb1bc/raw)</a>
        - この違いを Markdown にどう反映させるか、とか
    - あと正規表現読みづらいから嫌い感ある
        - でも使っていかないと慣れないよなぁ
        - [strike-multiple-lines](strike-multiple-lines.md)のコードリーディングも投げてしまった（めっちゃ気合入れないと読めない）し……
        - プログラマ名乗りたいならサクサク読めなきゃいけない
        - 折衷案だな
            - コードリーディングはあとでちゃんとやって、勉強ノートもメモして正規表現鍛える
            - こっちでは行指向で実行しましょ
                - ただし行指向つらそうだったら正規表現も考える
- 先にページpageのexpect dataつくってみる
    - [そろそろペインでもタブでもない新しいUIが欲しい](そろそろペインでもタブでもない新しいUIが欲しい.md)の2ウィンドウ試してみる
        - 左にmarkdownエディタ、右にScrapbox
        - :sta:悪くないし、普通に便利ですね
    - [1](https___github.com_stakiran_scbjson2ghpages_blob_e5911daf1ccee649aa06ae4aa3a41b8f135ca3e9_expect_page.md)
    - [2](https___github.com_stakiran_scbjson2ghpages_blob_09e4a8824f3f486e697be53da7295511aa55c694_expect_page.md)
- 足りない
    - 空行をはさんだリスト-リスト
        - expect
            - <a href="https://gyazo.com/c047910247e279883a8173ae1ddf5998" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/c047910247e279883a8173ae1ddf5998/raw)</a>
        - actual
            - <a href="https://gyazo.com/6c8b24f984905e3fd756e7e7529c78ea" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/6c8b24f984905e3fd756e7e7529c78ea/raw)</a>
        - 連結されてしまう。。。
    - リスト-段落の空行ありなしの差がわからない
        - <a href="https://gyazo.com/5b3a5bf745af7ecb1f04ef1d6eac2669" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/5b3a5bf745af7ecb1f04ef1d6eac2669/raw)</a>
        - そもそもMarkdownは`<p>`で区切るゲー（段落ゲー）なので、Scrapboxみたいな`行<br>- リスト`みたいな表現を持っていない
    - ~~よくわからんバグ~~ done from 2
        - ~~[GitHubのMarkdownでネストしたリストが正しくレンダリングされない](GitHubのMarkdownでネストしたリストが正しくレンダリングされない.md)~~
        - ~~<a href="https://gyazo.com/b17b882daab1861caa9720960939fd00" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/b17b882daab1861caa9720960939fd00/raw)</a>~~
        - ~~ちゃんと書いてますけど~~
            - ~~<a href="https://gyazo.com/3aa0a2060d1bb83d1a5695ffc7d5062c" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/3aa0a2060d1bb83d1a5695ffc7d5062c/raw)</a>~~
    - [GitHubのMarkdownのリストのネストは10まで](GitHubのMarkdownのリストのネストは10まで.md)
        - これはいいか（10以上ネストするケースはScrapboxでもそうはない（合ったとしてもそれは切り出しなどするべきって話
    - ファイル名として使えない文字を含んだタイトルへのリンク
        - `+page+`とか（`+page+.md`なんてファイルはつくれない（Windowsでは`+`は使えない
    - [リンクの種類](リンクの種類.md)がわからない
        - [どこにもリンクされていない赤リンクなのか](どこにもリンクされていない赤リンクなのか.md) ← つまり[スケルトンリンク](スケルトンリンク.md)なのか
        - [test](test.md) ← 既に存在する青色リンクなのか
        - [google](https://www.google.co.jp/) or <https://www.google.co.jp/> ← underlineされる外部リンクなのか
        - ---
        - 絵文字で対処するか？
            - [リンクの種類を視覚的に区別する](リンクの種類を視覚的に区別する.md)でやる
- [Markdownの「リストと段落の塊」の表現力が弱い件](Markdownの「リストと段落の塊」の表現力が弱い件.md)
    - 最大の懸念だったここを潰せたのでokかな

<br>

## Links
- ← [Scrapbox to Markdown](Scrapbox_to_Markdown.md)
- ← [Scrapbox to Markdown コードブロック](Scrapbox_to_Markdown_コードブロック.md)

## 2hop Links
- → [リンクの種類](リンクの種類.md)
    - ← [Scrapboxの読み方](Scrapboxの読み方.md)
    - ← [リンクの種類を視覚的に区別する](リンクの種類を視覚的に区別する.md)
    - ← [✅画像にリンク貼ってる場合に表記がおかしい件の修正](✅画像にリンク貼ってる場合に表記がおかしい件の修正.md)
- → [tfl](tfl.md)
    - ← [Terraformソースからビューをつくりたい](Terraformソースからビューをつくりたい.md)
- → [そろそろペインでもタブでもない新しいUIが欲しい](そろそろペインでもタブでもない新しいUIが欲しい.md)
    - ← [開発中に使えるmarkdownメモツール](開発中に使えるmarkdownメモツール.md)
- → [strike-multiple-lines](strike-multiple-lines.md)
    - ← [複数行に一気に打ち消し線を引けるようにしたいです](複数行に一気に打ち消し線を引けるようにしたいです.md)
- → [未来の自分という他人](未来の自分という他人.md)
    - ← [実行するスクリプトは 0 xxx.bat、1 yyy.batのように番号順にするとわかりやすい](実行するスクリプトは_0_xxx.bat、1_yyy.batのように番号順にするとわかりやすい.md)
    - ← [知的生産の5つのフェーズ](知的生産の5つのフェーズ.md)
    - ← [Scrapbox四天王のうち誰になりたいか](Scrapbox四天王のうち誰になりたいか.md)
- → [Repl.it](Repl.it.md)
    - ← [Python入門](Python入門.md)
    - ← [PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現](PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現.md)
    - ← [Pythonでinline grammer replaceを正規表現で試すサンプル](Pythonでinline_grammer_replaceを正規表現で試すサンプル.md)
- → [リンクの種類を視覚的に区別する](リンクの種類を視覚的に区別する.md)
    - ← [Scrapbox to Markdown](Scrapbox_to_Markdown.md)
- → [スケルトンリンク](スケルトンリンク.md)
    - ← [空リンク](空リンク.md)
    - ← [読んだラノベ](読んだラノベ.md)
    - ← [いいかげんにつくる](いいかげんにつくる.md)
- → [PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現](PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現.md)
    - ← [Scrapbox to Markdown コードブロック](Scrapbox_to_Markdown_コードブロック.md)
    - ← [Scrapbox to Markdown 画像とicon記法の実装](Scrapbox_to_Markdown_画像とicon記法の実装.md)
- → [Markdownではリスト中のコードハイライト（とテーブル）を表現できない](Markdownではリスト中のコードハイライト_とテーブル_を表現できない.md)
    - ← [Scrapbox to Markdown リスト中のテーブルやらコードやらブロック](Scrapbox_to_Markdown_リスト中のテーブルやらコードやらブロック.md)
    - ← [Scrapbox to Markdown テーブル](Scrapbox_to_Markdown_テーブル.md)
    - ← [ダミーリスト](ダミーリスト.md)
