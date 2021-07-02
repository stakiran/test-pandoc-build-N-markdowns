## scrapbox-dailytasklist-impls
- x [Scrapboxでページを1件ずつ計n件分取得する実験](Scrapboxでページを1件ずつ計n件分取得する実験.md)
- x [isTaskPageの残骸](isTaskPageの残骸.md)
- x [JavascriptでJSTの現在日や曜日を取得する](JavascriptでJSTの現在日や曜日を取得する.md)

<br>

console.logへの出力を貼り付けてみます

- リンクで汚したくないのでこっちでやる
    - [/sta-routinetask-sample/scrapbox-dailytasklistの動作確認エリア](https://scrapbox.io/sta-routinetask-sample/scrapbox-dailytasklistの動作確認エリア)
- 朝休 index.js:49:293048
    - index.js部分が邪魔すぎる……
    - 手元で置換した
        - <a href="https://gyazo.com/be570d046441fc9f88e7cc963bcc061a" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/be570d046441fc9f88e7cc963bcc061a/raw)</a>
- 連続してdoneするのがだるい
    - `[`つける
    - up or down
    - left
        - ここがだるい:sta:
    - `[`つける
- が、頭に描いてたのがようやく形になってテンションあがってる
    - ひゃっふー
- 後ろに`]`つけてdoneにするのは？
    - ダメです
    - `~~[task~~(task.md)` ← この時点で打ち消し線が入ってしまう

<br>

sectionによる並び替えはどう実装しようか？

- 二重ループで愚直に

<br>

importしてくる側から設定値を指定してもらうにはどうすればいい？

- ans: 普通にクラスとか関数とかexportすればいいです
- [ダックタイピング](ダックタイピング.md)しかない？
- つまり xxx という変数名に～～な値が入っているとみなす

<br>

<a href="https://gyazo.com/9b38a032c370b2b0ef8a29accf374e6e" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/9b38a032c370b2b0ef8a29accf374e6e/raw)</a>

- あと3つ
    - <a href="https://gyazo.com/04606af86dabf156bbf23ce1d5597f00" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/04606af86dabf156bbf23ce1d5597f00/raw)</a>
    - [Congratulation](Congratulation.md)!

<br>

<a href="https://gyazo.com/f3f2a61648678a73f20cc0933b93ced3" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/f3f2a61648678a73f20cc0933b93ced3/raw)</a>

- 0 なのに無限ループ出てくれない
- lengthをlenghtと書いていた……

<br>

<blockquote>Uncaught SyntaxError: missing ) after argument list</blockquote>

- もう10回は遭遇している
- thenの閉じ括弧

<br>

<blockquote>GEThttps://scrapbox.io/assets/img/logo-cut.svg 404</blockquote>

- 全部ダメ
    - <https://scrapbox.io/assets/img/logo-cut.svg>
    - /assets/img/logo-cut.svg
    - /assets/img/logo.svg

<br>

<blockquote>Uncaught ReferenceError: can't access lexical declaration 'getDailyTaskList' before initialization</blockquote>

参照するオブジェクトは事前に定義が必要

つまり script.js 並べるなら、先に定義を上から並べることになる

<br>

<a href="https://gyazo.com/d0841351105ea40231ae14037ae6e18d" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/d0841351105ea40231ae14037ae6e18d/raw)</a>

末尾のセミコロン抜け

<br>

## Links
- ← [scrapbox-dailytasklist](scrapbox-dailytasklist.md)

## 2hop Links
- → [Congratulation](Congratulation.md)
    - ← [英語のsとt、lとrを迷う問題](英語のsとt、lとrを迷う問題.md)
    - ← [tada](tada.md)
