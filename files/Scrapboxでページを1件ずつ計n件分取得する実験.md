## Scrapboxでページを1件ずつ計n件分取得する実験
- 全ページの内容を全部parseする ← これたぶん無理
    - できるけど 3000page の fetch になるから実質無理
    - ちょっとコード書いて時間計測してみよう、案外一瞬かもしんねえ
    - n=30
        - <a href="https://gyazo.com/34833f44756bdc4cfd641a21388822f7" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/34833f44756bdc4cfd641a21388822f7/raw)</a>
        - 12秒くらいだった
        - 3000だと単純計算で1200秒
        - 論外
- [thk](thk.md) [/takker](https://scrapbox.io/takker)
    - [/villagepump/@sta#6012cb151280f0000057ddc2](https://scrapbox.io/villagepump/@sta#6012cb151280f0000057ddc2)
    - `Promise.all()`
    - ブラウザ激重くなりそうな気がしないでもない
    - 10, 1000, 1000, 3000 同時くらいで実験
        - [/takker/scrapboxの全てのpageを取得する](https://scrapbox.io/takker/scrapboxの全てのpageを取得する)
        - サーバーに負担かかる問題があるもよう

<br>

```js
// ページ内容全件取得
// fetch で一件ずつ取る案
// 遅すぎて論外

/*
const pages = scrapbox.Project.pages
const pageTitles = []
for(const page of pages){
 const doesNotExists = page.exists == false
 if(doesNotExists){
  continue
 }
 const title = page.title
 pageTitles.push(title)
}

const getter = (pageTitle) => {
    return fetch(`/api/pages/sta/${pageTitle}/text`).then((res) => {
     return res.text()
    }).then((text) => {
     const textByStr= text
     const textByLines = text.split(LB)
     return textByLines
    })
}

let c = 0
async function けいそくする(count){
  console.log(`けいそく すたーと with ${count}`)
    for(let i=0; i<count; i++){
     const pageTitle = pageTitles[i]
     c += 1
     await getter(pageTitle)
    }
    console.log('けいそく ＼(^o^)／')
} 
けいそくする(30)
*/
```

<br>

## Links
- ← [scrapbox-dailytasklist-impls](scrapbox-dailytasklist-impls.md)

## 2hop Links
- → [thk](thk.md)
    - ← [このScrapbox固有の表記](このScrapbox固有の表記.md)
    - ← [知的生産は個人的なものである、の考察残骸](知的生産は個人的なものである、の考察残骸.md)
    - ← [新奇開拓のジレンマ](新奇開拓のジレンマ.md)
