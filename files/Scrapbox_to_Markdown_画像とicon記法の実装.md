## Scrapbox to Markdown 画像とicon記法の実装
impl6

- 画像いきます
- [Gyazoのリンクから画像の直リンクを得る](Gyazoのリンクから画像の直リンクを得る.md)には？
    - [Gyazo API](Gyazo_API.md)使うしかなさそう
    - 12500requests/日
        - [/sta](https://scrapbox.io/sta)が4500page、仮に5pageに1pageで画像1枚使ってるとすると、900枚
        - まあ問題なさそうか
    - pagesize 1～100
        - 100回をn回ぶん回すことになるね
- 実装は？
    - ステップ分けた方がいい
    - json to markdownする前に「画像リンクするのに必要な情報を集めてくるフェーズ」を設ける
        - コマンド一発で行えるようにする
        - トークンはたぶん用意してもらう必要があるな
- つまり
    - `.png`決め打ちでいいので変換をつくりきる
    - Gyazo API使って正しいurlをゲットする処理（というかコマンド）
    - ↑ この二つがある
- 変換済ませたいから、前者からいきまふ
    - [PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現](PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現.md)
    - 帰還
    - 追加で以下が必要です
        - [Gyazo API](Gyazo_API.md)を使って画像のURLと縦横比を手に入れる（手に入れておく）
        - icon記法をパースして`<img>`タグに置換し、（その中身を）手に入れてた情報を使って仕上げる
    - が、これは`scb_to_markdown_in_line()`より上のレイヤーの仕事なので、ここではしません
- [Scrapboxのicon記法表示時の縦横比](Scrapboxのicon記法表示時の縦横比.md) 調べる
    - 行に収まるように配置している
    - imgタグのheight/widthではどう指定すればいい？
        - ScrapboxはCSSで処理してるっぽいけど、Markdownに載せる場合はimgタグの表現力しか使えない
        - だが[HTMLのimgタグのheightやwidthで%は使っちゃダメ](HTMLのimgタグのheightやwidthで%は使っちゃダメ.md)
- imgタグ置換処理
    - `:sta:`
    - `:sta:` 丸々カットして
    - replace `:XXX:` to `<img src='ページXXXに載ってる画像のURL' width="同左縦横比に基づいたX" height="同左縦横比に基づいたY" />`
    - markdown layerではCSSもjsも使えないから、結論として
        - pixel値だけで頑張る必要がある
        - 行の高さはわからない（ので適当に決め打ちするしかない）
- 実装
    - repl.it用

```py
import re

s = '''画像 noindent

![](https://i.gyazo.com/e4aae2345d1927c777db267138d1e419.jpg)

<br>

画像 indent

- ![](https://i.gyazo.com/639242beda8d44936421325524cd99f3.jpg)
    - ![](https://i.gyazo.com/777cfb7cd2528ebf90db1617ed659a40.jpg)

<br>

- ユーザーアイコンはどうしましょうか:sta:
    - わかるー（x3 してます）:sta:
    - わかるー:sta::sta::sta:

<br>
'''
lines = s.split('\n')

RE_ICON_TO_REMOVE_NONGREEDY = re.compile(r'\(.+?\.icon(\*[0-9]+){0,1}\.md\)')

RE_ICON_TO_REPLACE_TO_IMG = re.compile(r'\[(.+?)\.icon\]')

for i,line in enumerate(lines):
  newline = line
  newline = re.sub(RE_ICON_TO_REMOVE_NONGREEDY, '', newline)
  if line==newline:
    continue

  newline = re.sub(RE_ICON_TO_REPLACE_TO_IMG, '<img src="\\1" height="32" />', newline)
  print('{}: {}'.format(i, newline))
```

- ...
    - 丸々カット
        - `RE_ICON_TO_REMOVE = re.compile(r'\(.+\.icon(\*[0-9](0-9.md)+){0,1}\.md\)')`
            - これだと非貪欲にならん
        - `RE_ICON_TO_REMOVE_NONGREEDY = re.compile(r'\((.+\.icon(\*[0-9](0-9.md)+){0,1}\.md)?\)')`
            - これも結果変わらず
            - というか「非貪欲の`?`」は`?`か`*`か`+`につけるものか
        - `RE_ICON_TO_REMOVE_NONGREEDY = re.compile(r'\(.+?\.icon(\*[0-9](0-9.md)+){0,1}\.md\)')`
            - year!
    - imgタグ化
        - `RE_ICON_TO_REPLACE_TO_IMG = re.compile(r'\[(.+?)\.icon(\*[0-9]((.+?)\.icon(\*[0-9.md)+){0,1}\]')`
        - <a href="https://gyazo.com/3ce91d9512e81b8c1b45e4af5df96176" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/3ce91d9512e81b8c1b45e4af5df96176/raw)</a>
        - `icon*3` ← このn-repeatの対処が難しい。。。

<br>

## Links
- ← [Scrapbox to Markdown](Scrapbox_to_Markdown.md)
- ← [アイコン記法を画像として埋め込む](アイコン記法を画像として埋め込む.md)

## 2hop Links
- → [HTMLのimgタグのheightやwidthで%は使っちゃダメ](HTMLのimgタグのheightやwidthで%は使っちゃダメ.md)
    - ← [アイコン記法を画像として埋め込む](アイコン記法を画像として埋め込む.md)
- → [Scrapboxのicon記法表示時の縦横比](Scrapboxのicon記法表示時の縦横比.md)
    - ← [アイコン記法を画像として埋め込む](アイコン記法を画像として埋め込む.md)
- → [Gyazoのリンクから画像の直リンクを得る](Gyazoのリンクから画像の直リンクを得る.md)
    - ← [✅Gyazo埋め込みの画像を表示する](✅Gyazo埋め込みの画像を表示する.md)
    - ← [Gyazo API](Gyazo_API.md)
- → [PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現](PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現.md)
    - ← [Scrapbox to Markdown 文法変換の設計やら実装やら](Scrapbox_to_Markdown_文法変換の設計やら実装やら.md)
    - ← [Scrapbox to Markdown コードブロック](Scrapbox_to_Markdown_コードブロック.md)
- → [Gyazo API](Gyazo_API.md)
    - ← [✅Gyazo埋め込みの画像を表示する](✅Gyazo埋め込みの画像を表示する.md)
    - ← [PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現](PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現.md)
    - ← [Gyazoのリンクから画像の直リンクを得る](Gyazoのリンクから画像の直リンクを得る.md)
