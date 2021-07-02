## Scrapbox to Markdown テストコード設計
impl5

- ~~テストコードの戦略考える~~page testを整える
- bra
    - layer
        - json
        - raw scb
        - normalized scb([Scrapboxのjsonにはタブとスペース両方交じる](Scrapboxのjsonにはタブとスペース両方交じる.md)をスペースだけにするとか)
        - markdown
    - json使ってテストする
        - [/testdata-for-to-markdown](https://scrapbox.io/testdata-for-to-markdown)いじることでテストデータいじる
        - exportして手元に持ってくる
        - scbjson2ghpages.pyに食わせる
            - これだけだと全部読み込みで使いづらい
            - 指定ページのnormalized scbを返すようにする？
    - normalized scbで書かれた指定ファイルを使ってテストする
        - ファイルは適当に用意して
        - ~~scbjson2ghpages.pyに食わせることができるようにする？~~
            - ~~でも製品にテスト用機能搭載するって違くない？~~
            - 普通にtest_lib_scblines2markdown.pyからreadすればいいのでは
    - json何回もexportし直してなおしてってのはだるいからやめたい
    - テストのレイヤー
        - unittest
            - lib_*.pyの各変換機能とか
            - unittestライブラリでできる
            - ここはファイル I/Oせずにテストデータをハードコードすればいい
        - function test
            - jsonの特定ページがexpectと完全一致するかをたしかめる
            - ここは全体を一気通貫で見たいからI/Oも必要
            - 今は手作業で[WinMerge](WinMerge.md)で見てる
            - テストコードで処理したいときってどうすればいいんだ？
                - linuxのdiffコマンド？
                - 自力で「ファイル読んで内容比較するコード」つくる？
        - deploy test
            - 実際にghpagesにデプロイする
            - これは手作業で見てみて「うん、できてるな」するしかなくない？
            - [/sta](https://scrapbox.io/sta)で全部見るのはえぐい（4500page+）ので、追々直すスタイルになるだろう
            - [/testdata-for-to-markdown](https://scrapbox.io/testdata-for-to-markdown)はフルサポートしたいな
                - これは一つのghpagesとして公開しちゃう
    - diffコマンド例

```terminal
$ diff 2_page_expect.md 3_page_actual_step3.md
131a132,134
>
> <br>
>
```

- ...
    - ...
        - leftのファイルに131行目に対して add をすると、rightのファイルの132～134行目の内容になります

```見方
(before)
---
(after)
```

- ...
    - ...
        - ...

```before省略時
(after)
```

- ...
    - ...
        - だから、step3の方が三行ほど余分やで、と言っている
        - 完全一致すればstdoutはゼロ（同じファイルを二つ食わせるとわかる）
    - 直近ではcodeやtableをかんたんにテストする手段がほしい
    - これはバージョン管理する？
        - 1_page_input.scb
        - 2_page_expect.md
    - これはしない
        - 3_page_actual_step1.md
        - 3_page_actual_step2.md
        - 3_page_actual_step3.md
    - 一般化すると
        - table:一般化

| 1_(pagename)_input.scb | normalized scbを記したファイル |
| - | - |
| 2_(pagename)_expect.md | 1を変換するとこうなるはずだ、という期待値 |
| 3_(pagename)_actual_step1.md | 1を変換したらこうなった、という実際の値(step1部分) |
| 3_(pagename)_actual_step2.md | 同上、step1後のstep2 |
| 3_(pagename)_actual_step3.md | 同上、step2後のstep3であり完成形（これがexpectと一致すればよい） |

- ...
    - ...
        - step1,2は最悪要らないが、あればデバッグ時に役立つので置いとく（gitignoreしてるのであってもかまわん）
    - pagenameバリエーション
        - [/testdata-for-to-markdown](https://scrapbox.io/testdata-for-to-markdown)
        - table:variation

| page | 今使ってる「リストの塊」と「基本的な文法」を網羅したもの |
| - | - |
| ? | コード記法 |
| ? | テーブル記法 |
| ? | 画像系 |

- ...
    - unittest……はもうできてる
        - 必要なら適当にCRUDできる
    - deploy test……は、まだまだ後
    - function test……が、UI整備されてない
        - pagenameに当たる部分をつくる
        - 自由に切り替えられるようにする
        - jsonとは切り離した方がいいか？
            - こうかな
            - 1: [/testdata-for-to-markdown](https://scrapbox.io/testdata-for-to-markdown)でテストデータつくる
            - 2: export to json
            - 3: ローカルに持ってきて、本体に加えて、to raw オプションで .scb ファイルに吐く
            - このscbファイルを 1_input.scb にする
- テストのレイヤー分け直します
    - unit test
        - 一般的なunittest
        - 部品がちゃんと動くかのテスト
        - unittestライブラリで完結させる
    - page test
        - page1つの変換がexpectと完全一致するかを試すテスト
        - テストデータはファイルとして準備しておくが、テストコードで動作完結できる
        - wrong時の確認は手作業 with [WinMerge](WinMerge.md)etc
    - project test
        - projectの変換がちゃんとできてるかを試すテスト
            - ページ数 = ファイル数くらいはテストコードで調べてもいいかもしれん
        - jsonを加えて、ちゃんと全部markdownで吐かれてるかを見る
            - 主にWindows側のfile writeに絡む問題がここで浮上するはずだ:sta:
            - [Windowsでファイル名に使えない文字](Windowsでファイル名に使えない文字.md)とか
        - 全部見るのはえぐいので程々に（[/sta](https://scrapbox.io/sta)は4500ページ超えてるから！）
        - index.mdが意図通りになってるかはちゃんと見るべき
            - そもそも何をどの順番でどう表示するかは全然設計できてないけど:sta:
    - deploy test
        - [GitHub Pages](GitHub_Pages.md)に実際にデプロイしてみるテストフェーズ
- page testの手段設計
    - test_pagetest.py？
        - ~~functionって単語微妙だな（関数を想起する）~~page test
        - test_page.pyだと「ページをテストする」でわかりづらいので「page testをテストする」ってことでこれでよい
    - テストデータはディレクトリ分けよう
        - testdata/ でいいか
        - テストコード自体はいったん直下に置いてしまう
    - ./
        - scbjson2ghpages.py
        - test_pagetest.py
        - testdata/
            - 1_codeblock_input.scb
            - 1_page_input.scb
            - 2_codeblock_expect.md
            - 2_page_expect.md
            - ....
    - expect actual の比較方法は？
        - 手作業やwinmergeでも見たいから、ファイルには出したい
        - 3_*.mdを出すよな
        - でもテスト自体はコード実行するだけで完結させたい
        - diffコマンドをos.systemで実行（行儀悪い）
        - 完全一致 or notであれば、コードで書ける
            - listとlistの比較をすればいい
            - たしかpythonだと簡単にできたはず
            - で、「完全一致じゃない」だったら、手作業でwinmergeとかで見る
                - さすがに「どこがどう違うか」の表示を車輪の再発明するのはエグい
            - これだな:sta:
- いけそうやな
- んでは整備・実装していきましょー
- [Pythonで2つのファイルが完全一致するかどうかを調べる](Pythonで2つのファイルが完全一致するかどうかを調べる.md)
- ok
    - <https://github.com/stakiran/scbjson2ghpages/tree/43348f1c22751bbee76318b8b9c51fa8e7308a6f>

<br>

## Links
- ← [Scrapbox to Markdown](Scrapbox_to_Markdown.md)

## 2hop Links
- → [Scrapboxのjsonにはタブとスペース両方交じる](Scrapboxのjsonにはタブとスペース両方交じる.md)
    - ← [Scrapbox to Markdown コードブロック](Scrapbox_to_Markdown_コードブロック.md)
    - ← [GitHubのMarkdownでネストしたリストが正しくレンダリングされない](GitHubのMarkdownでネストしたリストが正しくレンダリングされない.md)
    - ← [別に切に欲しくないけどなんか面白そうだからつくる](別に切に欲しくないけどなんか面白そうだからつくる.md)
- → [Windowsでファイル名に使えない文字](Windowsでファイル名に使えない文字.md)
    - ← [✅jekyllで日本語ファイル名が正しくリンクされない問題を修正する](✅jekyllで日本語ファイル名が正しくリンクされない問題を修正する.md)
    - ← [PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現](PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現.md)
