# test-pandoc-build-N-markdowns
n個のmdファイルをn個のhtmlファイルに変換する実験

## files/
- 250個くらい

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
