## scrapbox project被リンク数ヒストグラムのpythonスクリ
<a href="https://gyazo.com/6ecaeca7aa367172599a66d3a688b545" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/6ecaeca7aa367172599a66d3a688b545/raw)</a>

<br>

- 学び
    - Python requestsでAPI使えば、ローカルとPython libsの力でゴリゴリし放題
    - matplotlib 使えばかんたんにグラフ描けそう
        - でも色々概念あるのでちゃんと学ばないとつまづきそう

<br>

- :sta:処理すぐに終わったのがマジで意味わからん
    - 3000pageあるのに
    - 並列化？
    - ソース読んでみたい
        - GET `https://scrapbox.io/api/pages/{project}/search/titles`
        - `response.headers.get('X-Following-Id')` これがポイントみたいだ
    - 単純だった
        - [/scrapboxlab/api/pages/:projectname/search/titles](https://scrapbox.io/scrapboxlab/api/pages/:projectname/search/titles)
        - 1000件単位でゲットできる
        - 'X-Following-Idはただのpagination
        - **responseにページ内リンクの入ったlinksがある**
    - [collections.Counter()](collections.Counter().md)
    - ヒストグラムつくってるところはよーわからん
        - [matplotlib.pyplot.hist — Matplotlib 3.3.3 documentation](https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.hist.html)
    - グラフ描画使ったことないけど、思っているよりかんたんに描けるんだな
        - [matplotlibの階層構造を知ると幸せになれる(かもしれない) - Qiita](https://qiita.com/ceptree/items/5fb5e9e6f29d214153c9)
        - [早く知っておきたかったmatplotlibの基礎知識、あるいは見た目の調整が捗るArtistの話 - Qiita](https://qiita.com/skotaro/items/08dc0b8c5704c94eafb9)
        - 用語いっぱいあるのでちゃんと勉強した方がよさげ
            - [Terraform](Terraform.md)読んだときみたいに、[DeepL翻訳](DeepL翻訳.md)さんとか
    - （こういうの全然知らんところ）[大学の卒業研究時代はほぼ遊んでた](大学の卒業研究時代はほぼ遊んでた.md)のが効いてる気がしないでもない

<br>

- [/villagepump/各projectの被リンク数histogram](https://scrapbox.io/villagepump/各projectの被リンク数histogram)
- use
    - コピペしてインデント整えて

```terminal
$ pip install requests
$ pip install matplotlib
$ python main.py sta
```

- 文字化けしてるな
    - たぶんcicaフォントがpcにない

<br>

## Links
- ← [LinksとPagesの比](LinksとPagesの比.md)

## 2hop Links
- → [Terraform](Terraform.md)
    - ← [真の意味でものづくりがしたいんだよ](真の意味でものづくりがしたいんだよ.md)
    - ← [じぶんリリースノート 0.32.5](じぶんリリースノート_0.32.5.md)
    - ← [抽象化されて提供されているものの中身を把握する](抽象化されて提供されているものの中身を把握する.md)
- → [DeepL翻訳](DeepL翻訳.md)
    - ← [Obsidian](Obsidian.md)
    - ← [このScrapbox固有の表記](このScrapbox固有の表記.md)
    - ← [DeepLさんに頼りたい](DeepLさんに頼りたい.md)
