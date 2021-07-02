## scrapbox-staのビルドでjekyllがタイムアウトする
1

- 7min経ってもビルド返ってこなくて不穏。。。
- <a href="https://gyazo.com/9e65979b25a1e4812c94122867d2dce4" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/9e65979b25a1e4812c94122867d2dce4/raw)</a>
- [GitHub Pagesのjekyllビルド時間はリンク数にも比例する](GitHub_Pagesのjekyllビルド時間はリンク数にも比例する.md)
- 10min over
- 死んだ
- んーーーーー:sta:
    - もし「この規模のファイル群はそもそもghpagesでは間に合いません」だったら詰む
- でもなー、別にquotaも引っかかってないぞ
    - [GitHub PagesのQuota制限](GitHub_PagesのQuota制限.md)
    - 10commit/h なんて超えてないし
        - <a href="https://gyazo.com/a63a75a8a801b4eaec0a72926169a57f" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/a63a75a8a801b4eaec0a72926169a57f/raw)</a>
    - ファイルサイズもたかが知れてる
        - <a href="https://gyazo.com/47b0f8d5e32969e45865e2e73487b59c" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/47b0f8d5e32969e45865e2e73487b59c/raw)</a>
- [The GitHub Pages build timed out. Please try again later.](The_GitHub_Pages_build_timed_out._Please_try_again_later..md)
    - 変換どこかでしくって死んでる可能性
- 見出し周りで悪さしてる？
    - <a href="https://gyazo.com/2eb3d2c94ba24b5451677b7ff688cece" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/2eb3d2c94ba24b5451677b7ff688cece/raw)</a>
    - `→`書いてるからとか？
    - いやいや
- rerunしてみる
    - これでダメだったらぐううう
    - 5.2min
    - ダメそう:sta:
    - ダメだ、なんか死んでるのかなぁ？
    - 1dayおいてrerunしたけどやっぱりダメなので、quotaではない

<br>

Q: リンクが多すぎる？

- [5000行のリンクからなるMarkdownをGitHub Pagesに置いてみる](5000行のリンクからなるMarkdownをGitHub_Pagesに置いてみる.md)いけたからそんなことはないはず

<br>

Q: 見出しがおかしい？

- とりあえず小さなrepoで`## → [ファイル名](ファイル名.md)` 試してみる
    - <https://github.com/stakiran/test-ghpages-error>
    - <https://stakiran.github.io/test-ghpages-error/>
    - 普通にいけるのでfalse

<br>

差分がやばすぎるから？

- 当該コミット
    - <a href="https://gyazo.com/1027ea53f9efe729e7f451f7ef77e546" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/1027ea53f9efe729e7f451f7ef77e546/raw)</a>
- linksだけ入れたときはこうだった
    - <a href="https://gyazo.com/af9ca8b11d18ce791c31456ac560a173" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/af9ca8b11d18ce791c31456ac560a173/raw)</a>
- 桁違うなｗ
    - これはjekyll内部でなにか起きててもおかしくない
        - でもsta.json入れた時は動いたよ
        - <a href="https://gyazo.com/f9a21585801d4d45683f658c03aeaca5" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/f9a21585801d4d45683f658c03aeaca5/raw)</a>
        - それでも12万か
    - どうすれば……
        - filter-branchで消さなあかん？いやいや。。。

<br>

[Troubleshooting Jekyll build errors for GitHub Pages sites - GitHub Docs](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites)

- [Troubleshooting Jekyll build errors for GitHub Pages sites - GitHub Docs](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites)
    - force `encoding: UTF-8`
        - 今試してる
        - だめ
    - [Markdown errors](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites#markdown-errors)
- ほかは無さそう

<br>

2hop-linksを上限2個にした

- 今のデータ感
    - <a href="https://gyazo.com/ffa0b6da61c41465e07fd757abe1d52d" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/ffa0b6da61c41465e07fd757abe1d52d/raw)</a>
- 対応
    - 削減行数は劇的
        - <a href="https://gyazo.com/a2d3f47a9a0abd4f4b5927cf8d314708" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/a2d3f47a9a0abd4f4b5927cf8d314708/raw)</a>
    - <a href="https://gyazo.com/9c770f6098cd82a4920ea41f1e576679" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/9c770f6098cd82a4920ea41f1e576679/raw)</a>
- まだ死ぬ
    - というか長い
    - <a href="https://gyazo.com/cd4cd75fd66165c4685e0d54f5a9c91f" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/cd4cd75fd66165c4685e0d54f5a9c91f/raw)</a>
    - <a href="https://gyazo.com/77feb0adc2e8ae704aee623f16aa2289" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/77feb0adc2e8ae704aee623f16aa2289/raw)</a>
        - 10minくらいでタイムアウトするイメージなのに
    - <a href="https://gyazo.com/b6a1c1299c8ee29248f089aae9a21067" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/b6a1c1299c8ee29248f089aae9a21067/raw)</a>
        - おおい、帰ってこーい
    - <a href="https://gyazo.com/a2052447fdf3e5b33d76541eb0e57b35" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/a2052447fdf3e5b33d76541eb0e57b35/raw)</a>
        - さまよってるな

<br>

見出し省いたら通ったが……

- <a href="https://gyazo.com/0d8a05b1539240a8062ca5e82aad3e88" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/0d8a05b1539240a8062ca5e82aad3e88/raw)</a>
- 嘘だろ、見出しあかんの？何が？
    - <a href="https://gyazo.com/4d55594b874d898e6a3f23b726161d1e" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/4d55594b874d898e6a3f23b726161d1e/raw)</a>

<br>

また通らなくなりそう

- と思ったらok
    - 8minくらいかかってる
- 少しページ数増やしたらtimed out

<br>

まとめ（推測ばりばりで正しさ怪しい。。。）

- 見出し省いたら通ったので、見出しはあまり入れない方が良い
- ビルド時間が10minくらい超えるとtimed out
    - なので10minくらい以内に収める必要がある
- jekyllのビルドは完全ブラックボックスなので原因下がるのがムズすぎる。。。
- 

<br>

## Links
- ← [✅Linksに相当するFooterをつける](✅Linksに相当するFooterをつける.md)

## 2hop Links
- → [The GitHub Pages build timed out. Please try again later.](The_GitHub_Pages_build_timed_out._Please_try_again_later..md)
    - ← [GitHub PagesのQuota制限](GitHub_PagesのQuota制限.md)
    - ← [❌レンダリングエンジンをHugoに変える](❌レンダリングエンジンをHugoに変える.md)
- → [5000行のリンクからなるMarkdownをGitHub Pagesに置いてみる](5000行のリンクからなるMarkdownをGitHub_Pagesに置いてみる.md)
    - ← [✅index.mdを自動生成する](✅index.mdを自動生成する.md)
- → [GitHub PagesのQuota制限](GitHub_PagesのQuota制限.md)
    - ← [The GitHub Pages build timed out. Please try again later.](The_GitHub_Pages_build_timed_out._Please_try_again_later..md)
