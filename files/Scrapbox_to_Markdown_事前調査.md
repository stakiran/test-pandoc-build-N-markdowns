## Scrapbox to Markdown 事前調査
- ブックマークレットで単体ページ行うのは[/daiiz](https://scrapbox.io/daiiz)さんのがある
    - [daiiz/sb2md: Scrapbox contents -> Markdown](https://github.com/daiiz/sb2md)
    - 主にScrapboxで書いたものを、公開用にMarkdownにしたい場合に重宝
    - これも
        - <https://hashrock.github.io/md2sb-online/>
- :sta:僕が欲しいの
    - エクスポートしたjsonから、たとえばgithub wikiで公開できるmarkdownのファイル郡に変換する
    - jsonから変換するやつ
        - <https://github.com/kondoumh/sb2md>
            - <https://github.com/mamezou-tech/sbgraph>

<br>

- 手段
    - GitHubで公開することを念頭に
    - GitHub Actionsで自動ビルド試したりもしたい

```file
wiki/
b.bat
data.json
convert.py
```

<br>

- エクスポートしたjson使ってつくってみるか
    - 例

```json
    {
      "title": "workspace",
      "created": 1588146516,
      "updated": 1593231788,
      "id": "5ea93151287376001e3ef378",
      "lines": [
        "workspace",
        " [- 各概念の用語をページ化していくかどうか] いったん無し。仮説含めてまとめきる",
        "  [- マニャーナ]",
        "  [- GTD]",
        " [- 文献の強化？] いったんここまでで。",
        " [仮説]を潰していく",
        " [タスク管理概論]ページを拡充して「これなら本書けそう」レベルまで",
        " 電子書籍執筆開始",
        ""
      ]
    },
```

- ...
    - ...

```md
workspace

- ~~各概念の用語をページ化していくかどうか~~ いったん無し。仮説含めてまとめきる
    - ~~マナーニャ~~
    - ~~GTD~~
- ~~文献の強化~~ いったんここまでで
- [仮説](仮説)を潰していく
- [タスク管理概論](タスク管理概論)ページを拡充して……
- 電子書籍執筆開始

```

- ...
    - github wiki を想定しているのでリンクは `[ページ名](ページ名)`
        - .md はなし
    - 段落の間には空行を
    - **\tとスペースの違いがわからん**
        - <a href="https://gyazo.com/72755ae324d326f0a9f9ed9e6c2af565" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/72755ae324d326f0a9f9ed9e6c2af565/raw)</a>
        - <a href="https://gyazo.com/62c4d95e8e6fd26398d6a7a775fce4d7" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/62c4d95e8e6fd26398d6a7a775fce4d7/raw)</a>
        - どっちもただのリストなんですが
        - tableの区切りは`\t`なんだが
        - 行頭はスペースも\tも両方許す、感じが良いのかしら？
    - tableやcodeの終端は？
        - インデントが一段戻ったとき
    - 画像
        - gyazo.com含むものを`![]()`でいけるはず
        - <https://github.com/stakiran/test_githubwiki/wiki/gyazoのリンクでも画像表示できる？>
            - ~~ダメです。会員登録後、一括でメタデータ公開的な操作が必要~~ いや普通に `i.` と `.png` つけていけるね
                - `.jpg` の場合もあります
                    - 判定が必要というわけか……
                    - 二つ並べれば確実ｗ
                - まあurl分かれば見えるんだから当然か
        - [gyazo](gyazo.md)

<br>

## Links
- ← [Scrapbox to Markdown](Scrapbox_to_Markdown.md)

## 2hop Links
- → [仮説](仮説.md)
    - ← [オッカムの剃刀](オッカムの剃刀.md)
    - ← [企業や製品の例](企業や製品の例.md)
    - ← [価値仮説](価値仮説.md)
