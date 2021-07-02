# test-pandoc-build-N-markdowns
n個のmdファイルをn個のhtmlファイルに変換する実験 from [レンダリングエンジンをPandocに変える - stakiran研究所](https://scrapbox.io/sta/%E3%83%AC%E3%83%B3%E3%83%80%E3%83%AA%E3%83%B3%E3%82%B0%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%B3%E3%82%92Pandoc%E3%81%AB%E5%A4%89%E3%81%88%E3%82%8B)

## info
- files/
    - 250個くらい

```
$ pandoc --version
pandoc 2.13
Compiled with pandoc-types 1.22, texmath 0.12.2, skylighting 0.10.5,
citeproc 0.3.0.9, ipynb 0.1.0.1
```

## 1

```
@echo off

setlocal
set selfdir=%~dp0
set targetdir=%selfdir%files

pushd %targetdir%
for %%f in (*.md) do (
	pandoc -f markdown+emoji -t html4 %%f -o %%f.html
)
popd
```

- :x: 駄目なところ
    - 遅い？
        - ssd + windows10 で 15 秒くらいかかった
        - 2500ファイルだと150秒
        - 5000ファイルだと300秒
        - 5分
        - jekyll よりは早いか
    - リンクが `.md` のまま
    - `.md.html` じゃなくて `.html` にしたいんだが、バッチファイルどう書く？
        - `%%~nf.html`

## Q: Pandoc は multiple input files できないの？
無理そう。

- [Markdown and including multiple files - Stack Overflow https://stackoverflow.com/questions/4779582/markdown-and-including-multiple-files]
    - `*.md` を 1-html にはできるが、N-html はできない
- [Pandoc - Pandoc User’s Guide https://pandoc.org/MANUAL.html]
    - それらしきオプション見当たらん

ので、N-file あったら pandoc も N 回呼ぶことになる……

# pandoc じゃないけどついでに mkdocs も試す

```
 not found in the documentation files.
WARNING -  Documentation file 'scrapboxで創作.md' contains a link to '知的生産者間のコミュニケ
ーション.md' which is not found in the documentation files.
INFO    -  Documentation built in 3.51 seconds
```

え、早い、良い。
