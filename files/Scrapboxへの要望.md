## Scrapboxへの要望
[/forum-jp](https://scrapbox.io/forum-jp)

<br>

**出した**

- [/forum-jp/現存する全てのpublic projectを横断検索したい](https://scrapbox.io/forum-jp/現存する全てのpublic projectを横断検索したい)
    - [Scrapboxに存在するすべてのpublic projectから検索したい](Scrapboxに存在するすべてのpublic_projectから検索したい.md)
    - 出しちまった
    - [takker](takker.md)さんあざっす
    - <blockquote>Googleで`site:scrapbox.io 検索ワード`で検索すればだいたい同じようなことがもうできると思います</blockquote>
        - Googleに見つかってない分も漏れなく調べたいって欲求があった
        - けど、承認欲求成分満載なのでたしかにダメ
- [/forum-jp/最後に編集した位置にジャンプするショートカットが欲しい](https://scrapbox.io/forum-jp/最後に編集した位置にジャンプするショートカットが欲しい)
    - shogoさんからリプ来た、あざっす、だけどちょっと違う
    - 「カーソル位置」ではなく「最後に編集した位置」に飛びたい
        - `カーソル位置≠最後に編集した位置`
        - 最後に編集した位置をi行とする
        - カーソル位置がi行以外でも、この操作をすると（新たに編集してなければ）i行にジャンプする
    - :sta:が、[UserScript](UserScript.md)でできそうな気はするな
    - [/forum-jp/現存する全てのpublic projectを横断検索したい#605456dd97c2910000223216](https://scrapbox.io/forum-jp/現存する全てのpublic projectを横断検索したい#605456dd97c2910000223216)
        - <blockquote>現存じゃないけど、お気に入り登録したprojectとかは検索したくなる事はありますね:shokai:</blockquote>
        - たぶんもうできてるよな
            - [Scrapboxで他のprojectも検索できるようになったのでUgly wordで検索してみる](Scrapboxで他のprojectも検索できるようになったのでUgly_wordで検索してみる.md)

<br>

**出してない**

- [画像に境界線が欲しい](画像に境界線が欲しい.md)
- [ページ名変更したあとの「変更しました」ってalert、必要だろうか？](ページ名変更したあとの「変更しました」ってalert、必要だろうか_.md)
- [テロメアの時刻を（行をコピペした後でも）line.createdに固定する](テロメアの時刻を_行をコピペした後でも_line.createdに固定する.md)
- ~~[複数行に一気に打ち消し線を引けるようにしたいです](複数行に一気に打ち消し線を引けるようにしたいです.md)~~ userscriptでok
- [画像エイリアス文法](画像エイリアス文法.md)
- バージョン管理したい
    - エクスポート先を固定urlにしてほしい or urlをレスポンドしてくれるAPI
        - バージョン管理したいので
        - [/sta-taskmanagement](https://scrapbox.io/sta-taskmanagement)とかで、「このへんの定義ごっそり変えたい」「でも後で戻れるようにしたい」なんてことがしたい
        - jsonをエクスポートして、ダメだったらimportし直す……をすればやりやすくなる
            - まあimportする前にいったんproject削除しないといけないけど……
                - [/forum-jp/全ページを削除するボタンが欲しい](https://scrapbox.io/forum-jp/全ページを削除するボタンが欲しい)
                - これは無反応
                - APIでこれできる手段が必要なんだよなぁ
        - 問題はjsonファイルのバージョン管理
            - エクスポートを機械的にできるようにすればいい
    - :sta:が、明らかに煩雑なので違うだろうなとは思う
- 他のScrapboxプロジェクトの参照エイリアス
    - [/sta-taskmanagement/実行後属性](https://scrapbox.io/sta-taskmanagement/実行後属性)
    - これだとちょっと長い
    - こうしたい
        - `tm/実行後属性` ← これだけで済むようにする
        - 事前に `tm=sta-taskmanagement` みたいな設定を持たせておく
- [LiveFiltering](LiveFiltering.md)

<br>

## Links
- ← [テロメアじゃなくて作成時刻を上手い感じで埋め込む技術](テロメアじゃなくて作成時刻を上手い感じで埋め込む技術.md)
- ← [複数行に一気に打ち消し線を引けるようにしたいです](複数行に一気に打ち消し線を引けるようにしたいです.md)
- ← [Scrapbox日記](Scrapbox日記.md)
- ← [Scrapboxのギャラリーモード](Scrapboxのギャラリーモード.md)
- ← [LiveFiltering](LiveFiltering.md)

## 2hop Links
- → [takker](takker.md)
    - ← [強い人は喋れる？](強い人は喋れる_.md)
    - ← [Xについて書かれたAさんBさんの意見をかんたんに見る的な何か](Xについて書かれたAさんBさんの意見をかんたんに見る的な何か.md)
    - ← [日々、とんは語る。](日々、とんは語る。.md)
- → [UserScript](UserScript.md)
    - ← [ScrapCalc](ScrapCalc.md)
    - ← [Scrapbox As A Brarea](Scrapbox_As_A_Brarea.md)
    - ← [takker](takker.md)
- → [画像エイリアス文法](画像エイリアス文法.md)
    - ← [Scrapboxで絵文字](Scrapboxで絵文字.md)
