## scrapbox-dailytasklist
<a href="https://gyazo.com/f2f088e82a7a289de13337936f904e42" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/f2f088e82a7a289de13337936f904e42/raw)</a>

<br>

- [scrapbox-dailytasklist-specs](scrapbox-dailytasklist-specs.md)
- [scrapbox-dailytasklist-impls](scrapbox-dailytasklist-impls.md)
- [scrapbox-dailytasklist-sandbox](scrapbox-dailytasklist-sandbox.md)
- [scrapbox-dailytasklist-readme](scrapbox-dailytasklist-readme.md)
- todo
    - ~~[/sta](https://scrapbox.io/sta)で試す(3000page超で現実的なパフォーマンスになるか）~~5-7秒待つが許容範囲
    - 2021/02/08 19:03:12 特に強い必要性もないので停滞中...:sta:
    - [UserScriptでメッセージを表示したい](UserScriptでメッセージを表示したい.md)
        - 表示する部分を組み込む
            - エラー出すだけだしalertでよくない？
            - :sta:たぶんtrue（明日の僕さん、どうですかね
        - fitやsecの文法ミス
        - page fetch時のprogress
    - 呼び出し元からパラメーター渡すようにする
    - 配布方法を考える
        - スクリは1ページ内に収める etc
        - UserScriptやJS知らない人でもコピペ+αで使えるようにしたい

<br>

```js
export const VERSION = 'scrapbox dailytasklist v0.0.1'

//後で外に出す
//const __projectName__ = 'sta-routinetask-sample'
const __projectName__ = 'sta'
const __sections__ = ['朝休','朝','昼休','昼','夕休','夕','夜休','夜']

const LB = '\n'
const DELIM_ATTRIBUTE = ':'
// @todo どうせなら fit で使ってる , と / も定数化しませんか？
const ATTRHEAD = {
 'FIT' : 'fit:',
 'SECTION' : 'sec:',
}

```

<br>

for debug

```js
const c = (obj) => {
 console.log(obj)
}
```

<br>

util Datetime

```js
class Datetime {
 constructor(){
  this._init()
 }
 
 _init(){
        const msecJST = Date.now()
        const dateJST = new Date(msecJST)
        console.log(`Datetimeクラス上の現在日時は ${dateJST}`)
        this._dateJST = dateJST
 }
 
 get day(){
  const day = this._dateJST.getDate()
  return day
 }
 
 get dowJP(){
        const downum = this._dateJST.getDay()
        const dowTable = ['日', '月', '火', '水', '木', '金', '土']
        const dow = dowTable[downum]
        return dow
 }  
} 
```

<br>

lib from [/programming-notes/テキストを挿入するUserScript](https://scrapbox.io/programming-notes/テキストを挿入するUserScript) 微修正

```js
function insertText(text) {
  const cursor = document.getElementById('text-input');
  cursor.focus();
  cursor.value = text;
  const uiEvent = document.createEvent('UIEvent');
  uiEvent.initEvent('input', true, false);
  cursor.dispatchEvent(uiEvent);
}
```

<br>

全ページ取得

APIの仕様で先頭5行まで

```js
// @return [] 範囲外に対して取得しに行ったとき
const getSpecificRange = (start, count) => {
    return fetch(`https://scrapbox.io/api/pages/${__projectName__}?skip=${start}&limit=${count}`).then((res) => {
     return res.json()
    }).then((json) => {
     return json.pages
    })
}

const getAllPages = async () => {
 let start = 0
 const fetchWindow = 1000
 const allPages = []
 
 while(true){
     const pages = await getSpecificRange(start, fetchWindow)
     const isReachedEnd = pages.length == 0
     if(isReachedEnd){
      break
     }
     // Python でいう extend がないので, 仕方なく愚直に辿って入れる...
     for(const page of pages){
      allPages.push(page)
     }
     start += fetchWindow
    }
 
 return allPages
}
```

<br>

全ページのうちタスクページだけを抽出

```js
const isTaskPage = (page) => {
 const lines = page.descriptions
 const tooShort = lines.length <= 1
 if(tooShort){
  return false
 }
 // タスクページかどうかを判定する
 // - 速度優先のため単純な文字列比較で判定したい
 // - fit: fit: でも満たしちゃうけど気にしない
 let foundCount = 0
 const REQUIRED_COUNT = 2
 for(const line of lines){
  const foundFitAttr = line.startsWith(ATTRHEAD.FIT)
  const foundSectionAttr = line.startsWith(ATTRHEAD.SECTION)
  if(foundFitAttr){
   foundCount++
  }
  if(foundSectionAttr){
   foundCount++
  }
  if(foundCount == REQUIRED_COUNT){
   break
  }
 }
 const notFoundAllRequiredAttr = foundCount != REQUIRED_COUNT
 if(notFoundAllRequiredAttr){
  return false
 }
 return true 	
}

const pagesToTaskPages = (pages) =>{
 let taskPages = []
 for(const page of pages){
  const isNotTaskPage = !isTaskPage(page)
  if(isNotTaskPage){
   continue
  }
  taskPages.push(page)
 }
 return taskPages
}
```

<br>

task

```js
class Task{
 constructor(page){
  this._title = page.title
  this._lines = page.descriptions
  
  this._fit = null
  this._section = null
  
  this._parseLines(this._lines)
 }
 
 _parseLines(lines){
  for(const line of lines){
   this._parseLine(line)
  }
 }
 
 _parseLine(line){
  // 毎回全パターンを parse することになるが
  // ルーチンタスク数は高々数百なので性能なんて気にしなくていい.
  this._parseAsFitAttr(line)
  this._parseAsSectionAttr(line)
 }
 
 _parseAsFitAttr(line){
   const vOrNull = this._parseAsXXXAttr_and_get(line, ATTRHEAD.FIT)
  if(vOrNull == null){
   return
  }
  this._fit = vOrNull
 }
 
  _parseAsSectionAttr(line){
   const vOrNull = this._parseAsXXXAttr_and_get(line, ATTRHEAD.SECTION)
  if(vOrNull == null){
   return
  }
  this._section = vOrNull
  }
  
 _parseAsXXXAttr_and_get(line, headOfAttr){
  const foundAttr = line.startsWith(headOfAttr)
  if(!foundAttr){
   return null
  }
  const v = line.substr(headOfAttr.length)
  return v
 }
 
 isFit(day, dowJP){
  let ret = false
  ret = ret || this._isFitAsEveryDay()
  ret = ret || this._isFitAsDow(dowJP)
  ret = ret || this._isFitAsSingleDay(day)
  ret = ret || this._isFitAsEnumedDay(day)
  ret = ret || this._isFitAsPerNDay(day)
  return ret
 }
 
 _isFitAsDow(dowJP){
  const myfit = this._fit
  const found = myfit.indexOf(dowJP) != -1
  if(found){
   return true
  }
  return false
 }
 
 _isFitAsEveryDay(){
  return this._fit == 'every'
 }
 
 _isFitAsSingleDay(day){
  const myday = this._stringDayToNumberDay(this._fit)
  if(myday == -1){
   return false
  }
  const isEqual = myday == day
  if(isEqual){
   return true
  }
  return false
 }
 
 _isFitAsEnumedDay(day){
  const myfit = this._fit
  const fitdays = myfit.split(',')
  const isNotEnumedDayFormat = fitdays.length == 0
  if(isNotEnumedDayFormat){
   return false
  }
  for(const fitdayByString of fitdays){
   const fitday = this._stringDayToNumberDay(fitdayByString)
       if(fitday == -1){
        continue
       }
       const isNotEqual = fitday != day
       if(isNotEqual){
        continue
       }
       return true
  }
  return false
 }
 
 _isFitAsPerNDay(day){
   const myfit = this._fit
   const maybeExpression = myfit.split('/')
   const isNotExpression = maybeExpression.length != 2
   if(isNotExpression){
    return false
   }
   
    const radix = 10  	 	
   const [a, b] = maybeExpression
   const routineIntervalDay = parseInt(a, radix)
   const hitPoint = parseInt(b, radix) // RPG における HP ではない
   // @todo ユーザーに書式正しくない旨伝えた方が易しいと思う
   if(Number.isNaN(routineIntervalDay)){
    return false
   }
   if(Number.isNaN(hitPoint)){
    return false
   }
   
   const mod = day % routineIntervalDay
   const isMatched = mod == hitPoint
   if(isMatched){
    return true
   }
   return false
 }
 
 // @return -1 日としておかしい値だった
 _stringDayToNumberDay(stringDay){
  // '25'  -> 25
  // '25a' -> 25
  // '2a5' -> 2
  // 'a25' -> NaN
  const radix = 10
  const numberOrNaN = parseInt(stringDay, radix)
  if(Number.isNaN(numberOrNaN)){
   return -1
  }
  const day = numberOrNaN
  return day
 }
 
 toLine(){
  const title = this._title
  const indentForScrapboxList = ' '
  const linkedTitle = `[${title}]`
  const line = `${indentForScrapboxList}- ${linkedTitle}]`
  return line
 }
 
 get section(){
  return this._section
 }
}
```

<br>

task enumer

```js
class TaskEnumer{
 constructor(tasks, sections){
  this._tasks = tasks
  this._sections = sections
 }
 
 // @return [line, line, ...]
 enum(){
  const indentForScrapboxList = ' ' 	
  const outLines = []
  // @todo ネスト深くて不吉な臭い
  for(const section of this._sections){
   outLines.push(`${indentForScrapboxList}${section}`)
      for(const task of this._tasks){
    const sectionOfTheTask = task.section
    const isNotMatched = section != sectionOfTheTask
    if(isNotMatched){
     continue
    }
    outLines.push(`${task.toLine()}`)
      }	
  }
  return outLines
 }
}
```

<br>

entrypoint

```js 
function getDailyTaskList(){
    const dt =  new Datetime()
    const nowday = dt.day
    const nowdow = dt.dowJP
    
    getAllPages().then((allPages) => {
     console.log(`page count is ${allPages.length}`)
     
     const taskPages = pagesToTaskPages(allPages)
     
     const tasks = []
     for(const taskPage of taskPages){
      const task = new Task(taskPage)
      tasks.push(task)
     }
     
     const fittedTasks = []
     for(const task of tasks){
      const isNotFit = !(task.isFit(nowday, nowdow))
      if(isNotFit){
       continue
      }
      fittedTasks.push(task)
     }
     
     const enumer = new TaskEnumer(fittedTasks, __sections__)
     const dailyTaskList = enumer.enum()
     
     const dailyTaskListByStr = dailyTaskList.join('\n')
     insertText(dailyTaskListByStr)
    })
}
```

<br>

UI

```js
const MENUNAME = 'DailyTaskList'
const SCRAPBOX_FAVICON_PATH = 'https://scrapbox.io/assets/img/favicon/favicon.ico'

scrapbox.PageMenu.addMenu({
 title: MENUNAME,
 image: SCRAPBOX_FAVICON_PATH, // 良いアイコン案ないのでテキトーに favicon で
});

const menu = scrapbox.PageMenu(MENUNAME)
menu.addItem({
 title: 'Create daily tasklist',
 onClick: getDailyTaskList,
});
```

<br>

## Links
- ← [UserScriptとの付き合い方を再考する](UserScriptとの付き合い方を再考する.md)
- ← [Scrapbox As A TaskManagement](Scrapbox_As_A_TaskManagement.md)
- ← [プログラミングフットワーク](プログラミングフットワーク.md)
- ← [Most viewedのページをたまにメンテナンスする](Most_viewedのページをたまにメンテナンスする.md)
- ← [Scrapboxでタスク管理](Scrapboxでタスク管理.md)
- ← [指定タグを含むページ名の一覧をつくるUserScript](指定タグを含むページ名の一覧をつくるUserScript.md)
- ← [Gyampっぽいの自作したい](Gyampっぽいの自作したい.md)
- ← [ScrapboxでGTD](ScrapboxでGTD.md)
- ← [じぶんリリースノート 0.32.1](じぶんリリースノート_0.32.1.md)
- ← [Scrapbox As A Configuration](Scrapbox_As_A_Configuration.md)
- ← [scrapbox-dailytasklist-readme](scrapbox-dailytasklist-readme.md)
- ← [TeamsチームXXXを覗く](TeamsチームXXXを覗く.md)
- ← [scrapbox-dailytasklist-specs](scrapbox-dailytasklist-specs.md)
- ← [UserScriptでメッセージを表示したい](UserScriptでメッセージを表示したい.md)
- ← [scrapbox-routinearea](scrapbox-routinearea.md)
- ← [Scrapbox上でルーチンタスク管理したい](Scrapbox上でルーチンタスク管理したい.md)

## 2hop Links
- → [scrapbox-dailytasklist-sandbox](scrapbox-dailytasklist-sandbox.md)
    - ← [scrapbox-dailytasklist-readme](scrapbox-dailytasklist-readme.md)
