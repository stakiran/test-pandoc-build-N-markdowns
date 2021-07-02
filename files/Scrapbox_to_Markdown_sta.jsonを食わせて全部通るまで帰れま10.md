## Scrapbox to Markdown sta.jsonを食わせて全部通るまで帰れま１０
sta.jsonを食わせて全部通るまで帰れま１０

- dryrun取って保存させてみまーす
- ok
    - <a href="https://gyazo.com/7a0462d00664e42120c1b36e840a4f4f" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/7a0462d00664e42120c1b36e840a4f4f/raw)</a>
    - 1分かからん
        - [PC2 ASUS Gaming Windows](PC2_ASUS_Gaming_Windows.md)で[SSD](SSD.md)だからだろうけど

<br>

~~sta.jsonを食わせて全部通るまで帰れま１０~~ dryrunレベルではok

- <a href="https://gyazo.com/5cb1ed88b0f327177c5ad244adbc1ea8" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/5cb1ed88b0f327177c5ad244adbc1ea8/raw)</a>
    - 早速死んだ
    - [/sta/Scrapbox to Markdown テーブル](https://scrapbox.io/sta/Scrapbox to Markdown テーブル)
    - こいつで死んでる模様
    - たぶん

```_
```
```

- ...
    - ...
        - これを3bqと名付けることにする
    - scb内にこの文字がそのまま出現しているパターンだな

```py
prefix, langname_part = newline.split('```')
```

- ...
    - ...
        - 今こうなので、要素3以上になったら死ぬ
        - 言い換えると3bqが同一行に2回以上現れたら死ぬ
        - そんなことある？
            - ここくらい？
                - <a href="https://gyazo.com/a30e56de63cd8cab1964757070f53754" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/a30e56de63cd8cab1964757070f53754/raw)</a>
            - が、これは既にcodeの中なのでcode:py部分が3bqになる、はないはずだが
    - いや、今のコードだと入るわ
        - <a href="https://gyazo.com/40c01d4983d6c0fcba332d1c35f0d2fb" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/40c01d4983d6c0fcba332d1c35f0d2fb/raw)</a>
        - <a href="https://gyazo.com/63888bf5e3a376961f7e112a7cc68ed6" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/63888bf5e3a376961f7e112a7cc68ed6/raw)</a>
            - コードブロックの開始(code:xxx)のときだけ line_to_start_of...を実行すべき
            - だが、今は2行目以降に code:xxx が出現したときもヒットしてるっぽいな
    - どうしようか
        - 案1: scb_to_markdown の方で「1行目だけヒットさせる」条件分岐つくる
            - o 役割分担適切
            - x 実装難しい
        - 案2: line_to_start... の方で要素3以上のケースを無視する
            - o 実装かんたん
            - x lineのくせにコンテキスト考えてて役割分担崩壊してる
    - 案1じゃないとダメだな

```py
```py
 aaa
 aaa
```

- ...
    - ...
        - ↑ こういうときに死ぬ
        - 「今はコードの中身だから code:xxx という記述があっても解釈しないよ」としなければならない
    - そのためには……うーん、state.is_entered_block_just_now() みたいなのが要る？
    - ~~pagetestでこのケースつくってためしましょー~~
        - と思ったけど、少し路線変えた
        - そもそも 3bqが2回以上続くケースがありえないので、想定しないとみなしてみた
        - <https://github.com/stakiran/scbjson2ghpages/commit/bd5c2c75b7e7930caa412c6b8ad0f86139bc570b>
    - ~~あと display-pagename は要らない（save_one_file()内で dryrun 立ってるなら pagename も出してしまえばいい）~~ok
- とりあえず全部変換は通った
    - <a href="https://gyazo.com/64b39412e87888b460a0a5c1346418ee" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/64b39412e87888b460a0a5c1346418ee/raw)</a>
    - 5秒くらいかかる with [PC2 ASUS Gaming Windows](PC2_ASUS_Gaming_Windows.md)
- [Markdown記法で書かれた「Markdownファイルへのリンク」部分をWindowsで保存できる名前に変換する](Markdown記法で書かれた「Markdownファイルへのリンク」部分をWindowsで保存できる名前に変換する.md)

<br>

いよいよscbjson2ghpages.py側の実装に入る

- コマンドラインオプション
    - 1ページだけ変換する
        - --page-to-scb
    - 全ページを変換する
        - デフォルトはこっちでいい
        - 保存先は？
            - -d でディレクトリ指定する？
            - ghpages決め打ちだから、その仕様に合わせればいい
            - docs/ と / があるんだったっけ？
                - yes
                - [GitHub Pagesのsource directoryの選択肢](GitHub_Pagesのsource_directoryの選択肢.md)
            - ならオプションで決めてしまえばいい
                - --use-docs-dir
                    - これ入れたら /docs になる
                    - デフォは / 
                    - とか
                - が、scbjsonは何千ページになるわけで、それを / に展開するのは辛いから /docs 一択でいいよね
                - いいです:sta:
        - /docs の存在を前提にします
            - 存在チェックしてなければエラーだそう
    - あとはどんなオプション？
        - これは追々でいい
- 変換処理、もう実装しちゃう
    - <a href="https://gyazo.com/50c279ae689cbd473e8741bb0e48ffaf" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/50c279ae689cbd473e8741bb0e48ffaf/raw)</a>
    - ok
    - <a href="https://gyazo.com/a0e860c7a511a5b27ea59ad68fc54924" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/a0e860c7a511a5b27ea59ad68fc54924/raw)</a>
- ここまではいい
    - 問題は[/sta](https://scrapbox.io/sta)を食わせたときやで……

<br>

## Links
- ← [Scrapbox to Markdown](Scrapbox_to_Markdown.md)

## 2hop Links
- → [PC2 ASUS Gaming Windows](PC2_ASUS_Gaming_Windows.md)
    - ← [環境改善オタク](環境改善オタク.md)
    - ← [名詞ナンバリング](名詞ナンバリング.md)
    - ← [ビルドにCPUパワーとI/Oを酷使するので何とかする](ビルドにCPUパワーとI_Oを酷使するので何とかする.md)
