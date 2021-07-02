## Scrapboxに画像をコピペするとYou are not logged in to Gyazoエラーが出る
<a href="https://gyazo.com/809b07eb2b66b2b5719a7c9461bd01c8" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/809b07eb2b66b2b5719a7c9461bd01c8/raw)</a>

You are not logged in to <https://gyazo.com>

↑ この一文が出る

<br>

コピペとは？

- snippingtoolで画面の一部をコピーして、scrapbox上でペーストする on Windows
- つまり画像のD&Dではなく「クリップボードにある画像データをペーストする」

<br>

考察

- どういうことだ？
- 可能性1
    - 元々「Gyazoログインしてないけどアップはできる状態」だった
    - 今回、新たにgyazoログインしてないぜメッセージを出すことにした？
        - gyazo宣伝するために？
- 可能性2
    - scrapboxとgyazoの連携まわりでバグが出ている
    - （本来はscrapboxからは自動でgyazoにログインできるようになっていた）

<br>

時系列

- 2021/03/31 20:27 そういう仕様になったとのこと
    - thk [/villagepump/You are not logged in to](https://gyazo.com#6062eae379d3a9000064f92f)(https://scrapbox.io/villagepump/You are not logged in to <https://gyazo.com#6062eae379d3a9000064f92f)>
    - なんでそうしたのかはまだピンと来てない
- 2021/03/30 17:50 起きた
    - ログインし直しても起きます
    - ブラウザのキャッシュとcookie消して再ログインしても起きます
    - とりあえずgyazoにアクセスしてログインしてみた
        - でなくなった
    - 調べてる
        - [Scrapboxのリリースノート](Scrapboxのリリースノート.md)は特になし
        - [ScrapboxのSystem Status](ScrapboxのSystem_Status.md)も問題なし
        - GyazoはリリースノートもSystem Statusもない
            - Twitterでも特に問題報告はなかった
- 2021/03/30 10:50 [コンビニ人間](コンビニ人間.md)書いててコピペしたときは起きてなかった
- with Firefox

<br>

## 2hop Links
- → [Scrapboxのリリースノート](Scrapboxのリリースノート.md)
    - ← [Scrapboxがおかしいときに見るページ](Scrapboxがおかしいときに見るページ.md)
    - ← [しれっと改善が入っているのが面白い](しれっと改善が入っているのが面白い.md)
    - ← [Scrapboxのブラケット入力時のページ補完の仕様が変わった？](Scrapboxのブラケット入力時のページ補完の仕様が変わった_.md)
- → [コンビニ人間](コンビニ人間.md)
    - ← [働きやすさのOPQRS](働きやすさのOPQRS.md)
    - ← [じぶんリリースノート 0.32.3](じぶんリリースノート_0.32.3.md)
    - ← [じぶんリリースノート 0.32.2](じぶんリリースノート_0.32.2.md)
- → [ScrapboxのSystem Status](ScrapboxのSystem_Status.md)
    - ← [Scrapboxがおかしいときに見るページ](Scrapboxがおかしいときに見るページ.md)
