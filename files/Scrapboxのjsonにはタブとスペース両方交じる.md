## Scrapboxのjsonにはタブとスペース両方交じる
- そのまま挿入されてる
    - タブキーでインデントするとタブ
    - スペースキーでインデントするとスペース
- ある行から改行して自動インデントした場合、その行のが踏襲される

<br>

```json
{
  "name": "sta-export-test",
  "displayName": "sta-export-test",
  "exported": 1609646173,
  "pages": [
    {
      "title": "space-based indent",
      "created": 1609646137,
      "updated": 1609646164,
      "id": "5ff14037f71d51001c00f314",
      "lines": [
        "space-based indent",
        " この箇条書きは",
        " スペースキーでつくっています",
        " サブネスト",
        "  サブ",
        "   サブ",
        "   サブ",
        "   \tサブ", //★これはたぶんタブでつくっちまった
        ""
      ]
    },
    {
      "title": "tab-based indent",
      "created": 1609646109,
      "updated": 1609646132,
      "id": "5ff1401a106d63002251b708",
      "lines": [
        "tab-based indent",
        "\tこの箇条書きは",
        "\tタブキーでつくっています",
        "\tサブネスト",
        "\t\tサブ",
        "\t\t\tサブ",
        "\t\t\tサブ",
        "\t\t\t\tサブ",
        ""
      ]
    }
  ]
}
```

<br>

## Links
- ← [Scrapbox to Markdown コードブロック](Scrapbox_to_Markdown_コードブロック.md)
- ← [Scrapbox to Markdown テストコード設計](Scrapbox_to_Markdown_テストコード設計.md)
- ← [GitHubのMarkdownでネストしたリストが正しくレンダリングされない](GitHubのMarkdownでネストしたリストが正しくレンダリングされない.md)
- ← [別に切に欲しくないけどなんか面白そうだからつくる](別に切に欲しくないけどなんか面白そうだからつくる.md)
- ← [sbq](sbq.md)
- ← [Scrapboxをエクスポートしたときのjsonフォーマット](Scrapboxをエクスポートしたときのjsonフォーマット.md)

