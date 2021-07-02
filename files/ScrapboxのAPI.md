## ScrapboxのAPI
- [/help-jp/API](https://scrapbox.io/help-jp/API)
    - 触りだけ
- [/scrapboxlab/APIの書式](https://scrapbox.io/scrapboxlab/APIの書式)
    - こっちが詳しい

<br>

**GETする**

- [fetch](fetch.md)を使う
- json()ではなくtext()を使う

```js
const LB = '\n'

fetch('/api/pages/sta/task/text').then((res) => {
 return res.text()
}).then((text) => {
 const textByStr= text
 const textByLines = text.split(LB)
 console.log(textByLines)
})
## Links
- ← [✅Linksに相当するFooterをつける](✅Linksに相当するFooterをつける.md)
- ← [Scrapboxでimport from jsonするAPI](Scrapboxでimport_from_jsonするAPI.md)
- ← [Tritask-scrapbox](Tritask-scrapbox.md)
- ← [Scrapbox上でルーチンタスク管理したい](Scrapbox上でルーチンタスク管理したい.md)
- ← [console.log(scrapbox)](console.log_scrapbox_.md)
- ← [Scrapbox Lint](Scrapbox_Lint.md)

## 2hop Links
