## Scrapboxをエクスポートしたときのjsonフォーマット
- [#Scrapbox](Scrapbox.md) 
- もしものために備えておくのは当たり前
- やり方
    - Settings から手作業で
    - バックアップとエクスポートの違い
        - 中身は一緒
        - json でダウンロードさせるのも一緒
        - バックアップは daily で自動的につくってる
        - エクスポートはクリックしたときにつくる
        - エクスポートは include metadata もできる
    - include metadata したらどうなる？
        - jsonファイルサイズは倍以上にはなる感じ？
        - page.lines の中身が詳細になる
            - 各 line に created と updated がついてる
- インデントは？
    - [Scrapboxのjsonにはタブとスペース両方交じる](Scrapboxのjsonにはタブとスペース両方交じる.md)

<br>

**データ構造**

全体

```json
{
  "name": "sta",
  "displayName": "sta",
  "exported": 1587260187,
  "pages": [
   <page>,
   <page>,
   ...
  ]
}
```

<br>

page

```json
    {
      "title": "sta",
      "created": 1584184889,
      "updated": 1586576710,
      "lines": [
        "sta",
        "[https://gyazo.com/505861e8a5c21ae87eb972c4affd8841]",
        "",
        "Website: https://stakiran.github.io/stakiran/",
        "Twitter: https://twitter.com/stakiran2",
        "",
        "吉良野すた(stakiran / sta)の備忘録です。",
        "",
        " 生産",
        "  #つくった",
        "  #企画",
        "  #創作ネタ",
        "  #ビジネスネタ",
        "  #開発ネタ",
        " 生活",
        "  #日記",
        "  #趣味",
        " インプット",
        "  #読んだ",
        ""
      ]
    }
```

<br>

page(metadata)

```json
    {
      "title": "sta",
      "created": 1584184889,
      "updated": 1586576710,
      "lines": [
        {
          "text": "sta",
          "created": 1584184889,
          "updated": 1584184889
        },
        {
          "text": "[https://gyazo.com/505861e8a5c21ae87eb972c4affd8841]",
          "created": 1584184889,
          "updated": 1584184919
        },
        {
          "text": "",
          "created": 1584184919,
          "updated": 1584184919
        },
        {
          "text": "Website: https://stakiran.github.io/stakiran/",
          "created": 1584184937,
          "updated": 1584184939
        },
        {
          "text": "Twitter: https://twitter.com/stakiran2",
          "created": 1584184940,
          "updated": 1584184947
        },
        {
          "text": "",
          "created": 1585132616,
          "updated": 1585132616
        },
        {
          "text": "吉良野すた(stakiran / sta)の備忘録です。",
          "created": 1586301423,
          "updated": 1586301441
        },
        {
          "text": "",
          "created": 1584252963,
          "updated": 1586576676
        },
        {
          "text": " 生産",
          "created": 1586576644,
          "updated": 1586576662
        },
        ...
      ]
    },

```

<br>

## Links
- ← [sbq](sbq.md)

## 2hop Links
- → [Scrapboxのjsonにはタブとスペース両方交じる](Scrapboxのjsonにはタブとスペース両方交じる.md)
    - ← [Scrapbox to Markdown コードブロック](Scrapbox_to_Markdown_コードブロック.md)
    - ← [Scrapbox to Markdown テストコード設計](Scrapbox_to_Markdown_テストコード設計.md)
    - ← [GitHubのMarkdownでネストしたリストが正しくレンダリングされない](GitHubのMarkdownでネストしたリストが正しくレンダリングされない.md)
