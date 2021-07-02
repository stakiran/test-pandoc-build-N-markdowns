## Scrapbox to Markdown
背景

- [承認欲求](承認欲求.md)満たしたい
- ScrapboxだとSEOが弱いし、そもそも承認成分を持ち込みたくない
- どうするか
    - 静的サイトに変換すればいい
    - 1ページを1ファイルに変換する
- [GitHub Pages](GitHub_Pages.md)が楽そうでいいかな
    - [tit](tit.md)や[monolithic](monolithic.md)みたいなテイストをイメージしている
    - つまり[Markdown](Markdown.md)に変換する

<br>

サンプル

- [scrapbox-sta](scrapbox-sta.md)

<br>

resources

- repo
    - <https://github.com/stakiran/scbjson2ghpages/>
- testdata
    - [/testdata-for-to-markdown](https://scrapbox.io/testdata-for-to-markdown)

<br>

progress

- 2021/05/06 一通り落ち着いたしGW終わるのでいったんここまで
    - <https://github.com/stakiran/scbjson2ghpages/releases/tag/v0.1.0>

<br>

:hr:

以下作業メモ

<br>

todo

- [ビルドにCPUパワーとI/Oを酷使するので何とかする](ビルドにCPUパワーとI_Oを酷使するので何とかする.md)
- [パイプ直書きでpipe trapが発動するのを防ぐ](パイプ直書きでpipe_trapが発動するのを防ぐ.md)
- [デバッグプリント用フラグを実行時コマンドラインオプションで与える](デバッグプリント用フラグを実行時コマンドラインオプションで与える.md)
- [DrawingなどScrapboxのストレージを使っている画像を表示する](DrawingなどScrapboxのストレージを使っている画像を表示する.md)
- [各ページに「view on scrapbox」リンクをつける](各ページに「view_on_scrapbox」リンクをつける.md)
- [リンクの種類を視覚的に区別する](リンクの種類を視覚的に区別する.md)
- 解析的にむずかしい
    - [引用中のリンクを反映させる](引用中のリンクを反映させる.md)
    - [アスタリスクを2つ以上重ねた太字表記内のリンクも正しく変換する](アスタリスクを2つ以上重ねた太字表記内のリンクも正しく変換する.md)
- [cssで(icon記法からつくった)絵文字を強調する](cssで(icon記法からつくった)絵文字を強調する.md)
- [アイコン記法を画像として埋め込む](アイコン記法を画像として埋め込む.md)
- [レンダリングエンジンを模索する](レンダリングエンジンを模索する.md)
    - [レンダリングエンジンをMkDocsに変える](レンダリングエンジンをMkDocsに変える.md)
    - [❌レンダリングエンジンをHugoに変える](❌レンダリングエンジンをHugoに変える.md)
- [でかすぎるリンクとその接続先を表示するページ](でかすぎるリンクとその接続先を表示するページ.md)
    - タグ名指定出来たほうがいいかも
- [index.mdに書く「projectごとに固有の部分」を自由にいじれるようにする](index.mdに書く「projectごとに固有の部分」を自由にいじれるようにする.md)
- [Linksの表示順序を上手い感じに並び替える](Linksの表示順序を上手い感じに並び替える.md)
- [✅Linksに載せるリンク数はオプションで指定できるようにする](✅Linksに載せるリンク数はオプションで指定できるようにする.md)
- [✅Linksに相当するFooterをつける](✅Linksに相当するFooterをつける.md)
    - 16-8-4 cutはもうちょっとなんとかしたい
    - [F,T,H limitを微調整してちょうどよい塩梅を探す](F,T,H_limitを微調整してちょうどよい塩梅を探す.md)
- [✅リスト中のブロックを含んだページの変換に穴があるのを修正する](✅リスト中のブロックを含んだページの変換に穴があるのを修正する.md)
- [✅全ページリンク集をつくる](✅全ページリンク集をつくる.md)
- [✅各ページに大見出しを入れる](✅各ページに大見出しを入れる.md)
- [✅各ページにタイトルを入れる](✅各ページにタイトルを入れる.md)
- [✅結果的に_から始まるファイル名にアクセスできないので何とかする](✅結果的に_から始まるファイル名にアクセスできないので何とかする.md)
- [✅jekyllで日本語ファイル名が正しくリンクされない問題を修正する](✅jekyllで日本語ファイル名が正しくリンクされない問題を修正する.md)
- [✅GitHub Pagesでsourceをルートにしている場合に、ルートにアクセスしてもindex.htmlに転送されない](✅GitHub_Pagesでsourceをルートにしている場合に、ルートにアクセスしてもindex.htmlに転送されない.md)
- [✅Gyazo埋め込みの画像を表示する](✅Gyazo埋め込みの画像を表示する.md)
- [✅index.mdを自動生成する](✅index.mdを自動生成する.md)
- testpageでテストしたいやつ
    - [✅画像にリンク貼ってる場合に表記がおかしい件の修正](✅画像にリンク貼ってる場合に表記がおかしい件の修正.md)
    - [✅アイコン記法の後に文字を書くと解釈がおかしくなるのを修正する](✅アイコン記法の後に文字を書くと解釈がおかしくなるのを修正する.md)
    - [✅リンクの後にアイコン記法が続く場合に変換がおかしくなるのを修正する](✅リンクの後にアイコン記法が続く場合に変換がおかしくなるのを修正する.md)
    - [✅URL直書きをリンクにする](✅URL直書きをリンクにする.md)
    - [✅リンク中に-(パイプ)が含まれるとテーブルとして解釈されてしまう問題](✅リンク中に-(パイプ)が含まれるとテーブルとして解釈されてしまう問題.md)

<br>

サンプルつくるまでの作業ログ

- [種々のタスクをScrapbox上でどうまとめるかを検討する](種々のタスクをScrapbox上でどうまとめるかを検討する.md)
- [sta.json加えてghpagesリリースします](sta.json加えてghpagesリリースします.md)
- [Scrapbox to Markdown sta.jsonを食わせて全部通るまで帰れま１０](Scrapbox_to_Markdown_sta.jsonを食わせて全部通るまで帰れま10.md)
- [Scrapbox to Markdown リスト中のテーブルやらコードやらブロック](Scrapbox_to_Markdown_リスト中のテーブルやらコードやらブロック.md)
- [Scrapbox to Markdown テーブル](Scrapbox_to_Markdown_テーブル.md)
- [ファイル内容が一致していてもリストとリストをassertEqualしていればFalseになることがある](ファイル内容が一致していてもリストとリストをassertEqualしていればFalseになることがある.md)
- [Scrapbox to Markdown コードブロック](Scrapbox_to_Markdown_コードブロック.md)
- [Scrapbox to Markdown 画像の実装はいったん捨てる](Scrapbox_to_Markdown_画像の実装はいったん捨てる.md)
- [Scrapbox to Markdown 画像とicon記法の実装](Scrapbox_to_Markdown_画像とicon記法の実装.md)
- [Scrapbox to Markdown テストコード設計](Scrapbox_to_Markdown_テストコード設計.md)
- [Scrapbox to Markdown 文法変換の設計やら実装やら](Scrapbox_to_Markdown_文法変換の設計やら実装やら.md)
- 2021/04/07 [Scrapbox to Markdown 基本方針](Scrapbox_to_Markdown_基本方針.md)
    - :sta:時期結構離れてる
        - 突然モチベーション湧いたんだよなぁ
        - あとちょうど[House2](House2.md)検討始めて他のタスク（≒[いせむげ](いせむげ.md)）を手放したからってのもある
- 2020/06/27 [Scrapbox to Markdown 事前調査](Scrapbox_to_Markdown_事前調査.md)

<br>

[#開発ネタ](開発ネタ.md)
## Links
- ← [真の意味でものづくりがしたいんだよ](真の意味でものづくりがしたいんだよ.md)
- ← [じぶんリリースノート 0.32.5](じぶんリリースノート_0.32.5.md)
- ← [いせむげを再開する](いせむげを再開する.md)
- ← [計画をつくるのが苦手](計画をつくるのが苦手.md)
- ← [Scrapbox As A Brarea](Scrapbox_As_A_Brarea.md)
- ← [飼われるためには](飼われるためには.md)
- ← [tilをScrapboxに統合したい](tilをScrapboxに統合したい.md)
- ← [やりたいことがない](やりたいことがない.md)
- ← [noteネタ](noteネタ.md)
- ← [ドッグフーディング](ドッグフーディング.md)
- ← [Scrapbox四天王のうち誰になりたいか](Scrapbox四天王のうち誰になりたいか.md)
- ← [タスク管理の体系化をGitHub Pagesに置いてみた](タスク管理の体系化をGitHub_Pagesに置いてみた.md)
- ← [✅Linksに相当するFooterをつける](✅Linksに相当するFooterをつける.md)
- ← [各ページに「view on scrapbox」リンクをつける](各ページに「view_on_scrapbox」リンクをつける.md)
- ← [scrapbox-sta](scrapbox-sta.md)
- ← [✅index.mdを自動生成する](✅index.mdを自動生成する.md)
- ← [種々のタスクをScrapbox上でどうまとめるかを検討する](種々のタスクをScrapbox上でどうまとめるかを検討する.md)
- ← [ひとりScrapbox開発](ひとりScrapbox開発.md)
- ← [Markdown記法で書かれた「Markdownファイルへのリンク」部分をWindowsで保存できる名前に変換する](Markdown記法で書かれた「Markdownファイルへのリンク」部分をWindowsで保存できる名前に変換する.md)
- ← [知的生産で食べていきたい](知的生産で食べていきたい.md)
- ← [Markdownでテーブルタイトルをテーブルに埋め込む](Markdownでテーブルタイトルをテーブルに埋め込む.md)
- ← [Markdownは段落の次に空行を入れなくてもテーブルを認識できるか](Markdownは段落の次に空行を入れなくてもテーブルを認識できるか.md)
- ← [ファイル内容が一致していてもリストとリストをassertEqualしていればFalseになることがある](ファイル内容が一致していてもリストとリストをassertEqualしていればFalseになることがある.md)
- ← [PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現](PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現.md)
- ← [Scrapboxで実装を考える世界](Scrapboxで実装を考える世界.md)
- ← [Gyazo API](Gyazo_API.md)
- ← [そろそろペインでもタブでもない新しいUIが欲しい](そろそろペインでもタブでもない新しいUIが欲しい.md)
- ← [Markdownの挙動調べてると1日30commitすぐに超える](Markdownの挙動調べてると1日30commitすぐに超える.md)
- ← [全部入りScrapboxで開発進めると楽しい](全部入りScrapboxで開発進めると楽しい.md)
- ← [Markdownの「リストと段落の塊」の表現力が弱い件](Markdownの「リストと段落の塊」の表現力が弱い件.md)

## 2hop Links
- → [tit](tit.md)
    - ← [自分の過程を収集](自分の過程を収集.md)
- → [✅jekyllで日本語ファイル名が正しくリンクされない問題を修正する](✅jekyllで日本語ファイル名が正しくリンクされない問題を修正する.md)
    - ← [✅結果的に_から始まるファイル名にアクセスできないので何とかする](✅結果的に_から始まるファイル名にアクセスできないので何とかする.md)
    - ← [Jekyllのincludeに_と.から始まる文字列を追加する](Jekyllのincludeに_と.から始まる文字列を追加する.md)
    - ← [半角英数字の全角化](半角英数字の全角化.md)
- → [✅画像にリンク貼ってる場合に表記がおかしい件の修正](✅画像にリンク貼ってる場合に表記がおかしい件の修正.md)
    - ← [✅Gyazo埋め込みの画像を表示する](✅Gyazo埋め込みの画像を表示する.md)
- → [Scrapbox to Markdown 文法変換の設計やら実装やら](Scrapbox_to_Markdown_文法変換の設計やら実装やら.md)
    - ← [Scrapbox to Markdown コードブロック](Scrapbox_to_Markdown_コードブロック.md)
- → [✅全ページリンク集をつくる](✅全ページリンク集をつくる.md)
    - ← [✅index.mdを自動生成する](✅index.mdを自動生成する.md)
- → [scrapbox-sta](scrapbox-sta.md)
    - ← [じぶんリリースノート 0.32.5](じぶんリリースノート_0.32.5.md)
    - ← [飼われるためには](飼われるためには.md)
    - ← [tilをScrapboxに統合したい](tilをScrapboxに統合したい.md)
