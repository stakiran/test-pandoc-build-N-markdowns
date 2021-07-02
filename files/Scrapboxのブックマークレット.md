## Scrapboxのブックマークレット
- titleを取ってきて、promptで編集させる
- 入力した文字列をタイトルとみなし、ページ作成＆リンク貼る
    - リンクはちゃんと元のtitle使っている

<br>

おおよそ予想通りの実装

<br>

ソース見てみる

```javascript
javascript:(function(){var title=window.prompt('Scrap "Scrapbox" to sta.',document.title);if (!title) return;var lines=['','['+window.location.href+' '+document.title+']'];var quote=window.getSelection().toString();if (quote.trim()) lines=lines.concat(quote.split(/\n/g).map(function(line){return ' > '+line}));lines.push('');var body=encodeURIComponent(lines.join('\n'));window.open('https://scrapbox.io/sta/'+encodeURIComponent(title.trim())+'?body='+body)})();
```

<br>

- Scrapbox側にAPIもどきがあるからこそできること
    - URLにhoge書いてgetしたら、hogeが存在しない場合に新規ページしちゃうやつ
    - [スケルトンリンク](スケルトンリンク.md)

<br>

## 2hop Links
- → [スケルトンリンク](スケルトンリンク.md)
    - ← [Scrapbox to Markdown 文法変換の設計やら実装やら](Scrapbox_to_Markdown_文法変換の設計やら実装やら.md)
    - ← [空リンク](空リンク.md)
    - ← [読んだラノベ](読んだラノベ.md)
