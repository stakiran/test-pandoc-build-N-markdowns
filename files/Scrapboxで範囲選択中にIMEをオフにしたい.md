## Scrapboxで範囲選択中にIMEをオフにしたい
<br>

まとめ

- `「`が消えないとあまりシームレスじゃないので、使うのやめる
- どうやったら消せるんだろうなぁこれ

<br>

**元の入力は要らないので切り捨てたい**

- known issueだった
- だめ
    - preventDefault や stopPropagation の組み合わせを変える
    - 処理入った直後に実行してみる
- [モダンブラウザにおけるキー入力のキャンセル - Qiita](https://qiita.com/pochman/items/b99c835bf598810d3c18)
    - Firefoxの場合、keydownの後にcompositionupdateが発生するらしい
    - リスナー2つくって、クロージャかなんかで状態変数でやりとりすればいいかもしれない
    - ああ、ダメだ、IMEオンのときはkeydownに来ないんだ

```js
//残骸。動かん
export function brackettingAlways() {
  document.addEventListener('keydown', e => {
   const eData = e.data
   console.log(e)
   
    const buttons = document.getElementsByClassName('popup-menu')
      ?.[0]?.getElementsByClassName('button')
    if (!buttons) return; // そもそもpopup menuがなかったら何もしない
    if (eData.length === 0) return;
    switch(eData.split('').pop()) {
      case '「':
        document.getElementsByClassName('button link-button')?.[0]?.click();
        break;
      default:
        break;
    }
  });
  
  document.addEventListener('compositionupdate', e => {
   const eData = e.data
   console.log(e)
   
    const buttons = document.getElementsByClassName('popup-menu')
      ?.[0]?.getElementsByClassName('button')
    if (!buttons) return; // そもそもpopup menuがなかったら何もしない
    if (eData.length === 0) return;
    switch(eData.split('').pop()) {
      case '「':
        document.getElementsByClassName('button link-button')?.[0]?.click();
        break;
      default:
        break;
    }
  });
}
```

<br>

**[thk**(thk.md) [/takker/IME onの時、キー入力をScrapboxに渡すUserScript](https://scrapbox.io/takker/IME onの時、キー入力をScrapboxに渡すUserScript)]

- 範囲選択しているかどうかは「popup menu出てるか」で判定する
- 出てたら0番目のbuttonをclick
    - <a href="https://gyazo.com/c8698086e75e00dff4f9f2deb5ced683" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/c8698086e75e00dff4f9f2deb5ced683/raw)</a>

```js
export function execute() {
  document.addEventListener('compositionupdate', e => {
    const buttons = document.getElementsByClassName('popup-menu')
      ?.[0]?.getElementsByClassName('button')
    if (!buttons) return; // そもそもpopup menuがなかったら何もしない
    if (e.data.length === 0) return;
    switch(e.data.split('').pop()) {
      case '「':
        e.preventDefault();
        e.stopPropagation();
        document.getElementsByClassName('button link-button')?.[0]?.click();
        break;
      default:
        break;
    }
  });
} 
```

<br>

**やりたいこと**

- 範囲選択中はほぼリンクをつける
- IMEオンだとつかない → オフにして → つける、とかしてて面倒くさい
- [UserScript](UserScript.md)でできないかしら
    - IME制御が無理ゲーな気がする
    - たぶんブラウザがセキュリティ的に許されてない

<br>

## 2hop Links
- → [UserScript](UserScript.md)
    - ← [Scrapboxへの要望](Scrapboxへの要望.md)
    - ← [ScrapCalc](ScrapCalc.md)
    - ← [Scrapbox As A Brarea](Scrapbox_As_A_Brarea.md)
