## ScrapboxをしているとFirefoxが重くなることがある
- ここまでのまとめ
    - 以下が重なると発生しやすい
        - [UserCSS](UserCSS.md)などで重くなっている
        - 重たい画像（でかい画像や高画質な画像）がたくさん使われている
    - たぶん僕のPCがポンコツなせい
    - たぶん僕のFirefoxが長年使っててプロファイル（のDB？）がおかしくなってる可能性

<br>

- 2021/01/24
    - <a href="https://gyazo.com/0d41b1c81719d1f0be54e5d4ed819e15" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/0d41b1c81719d1f0be54e5d4ed819e15/raw)</a>
    - [/sta](https://scrapbox.io/sta)こもってても発生した
- 2021/01/19
    - [about:performance](about_performance.md)で調べてみた
    - Scrapboxのページ一覧読み込むとき、こんなん
        - <a href="https://gyazo.com/f8dade1b77dbfb4172fda5cb457468cb" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/f8dade1b77dbfb4172fda5cb457468cb/raw)</a>

<br>

- ...
    - ガリガリ言い出すの、Scrapbox使ってるときだから、なんか契機があると思うんだよなぁ
    - 出にくいポケモンみたいな感じで全然掴めん
- 2021/01/13
    - <a href="https://gyazo.com/257f3f30738cc2cf1c594476c31c5f7f" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/257f3f30738cc2cf1c594476c31c5f7f/raw)</a>
    - [/RutileWIXOSS](https://scrapbox.io/RutileWIXOSS)見たら発生した
    - I/Oが遅いってことかなぁ
    - 通信の後に発生している
    - 通信の速さじゃないな、I/Oだわ
    - ちなみに[エコモード](エコモード.md)は関係なさそう（既にハイパフォ）
- 2021/01/09
    - [/icons](https://scrapbox.io/icons)眺めてても発生
    - 一つわかった、Firefoxが画像をキャッシュ化（保存）するときのI/Oだ
        - そして今のうちのPCはオンボロHDDだからI/Oは辛い
- 21/01/08
    - <a href="https://gyazo.com/e7f2791455a0fde597fe39eea6008831" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/e7f2791455a0fde597fe39eea6008831/raw)</a>
    - 再発
    - どうも[UserCSS](UserCSS.md)が重たいprojectだとなるっぽい
        - [井戸端](井戸端.md)もちょっと重たい
        - [/shiology](https://scrapbox.io/shiology)はだいぶ重たい
    - :sta:でも帯がずっと続くのっておかしない？
        - そんなに巨大なデータ？
        - たとえば画像が全部高品質なやつで合計すると何百MBレベルになるとか？
        - だとしたら早い回線じゃないとエグいね
            - [自宅の回線速度が遅い](自宅の回線速度が遅い.md)
    - このPCがポンコツ（Windows, HDD）なだけだろうが
        - [MBA](MBA.md)では起きないしね
    - あとブラウザのキャッシュだかなんだかもある気がするんだよなぁ
- 21/01/07
    - <a href="https://gyazo.com/d2c95419a4a45d38547bf8b7915a2059" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/d2c95419a4a45d38547bf8b7915a2059/raw)</a>
    - Scrapboxってか[井戸端](井戸端.md)見ていたとき？
        - だが収まっている
    - わからんなぁ
    - [Firefoxがあまりに重いので履歴を全部消した](Firefoxがあまりに重いので履歴を全部消した.md)とも関係ある？
        - 今は[週次レビュー](週次レビュー.md)時に履歴全部消してるけどなぁ
        - cookieやサイトデータも500MBもないし
    - PCが古くてHDDまわりがゴミなのかもしれない

```md
| 2017/4/8 | 750 | 昼食 | ラーメンチャーハンセット |  |
| 2017/4/8 | 130467 | PC関連 | ASUS ノートパソコン |  |
| 2017/4/8 | 486 | 朝食 | ベーカリー |  |
```

- ...
    - ...
        - まだ4年だが

<br>

## Links
- ← [PC2 ASUS Gaming Windows](PC2_ASUS_Gaming_Windows.md)
- ← [Scrapbox日記](Scrapbox日記.md)
- ← [Scrapboxは貧弱なPCに優しくない](Scrapboxは貧弱なPCに優しくない.md)
- ← [Firefox](Firefox.md)

## 2hop Links
- → [UserCSS](UserCSS.md)
    - ← [ScrapCalc](ScrapCalc.md)
    - ← [sta](sta.md)
    - ← [Scrapbook](Scrapbook.md)
- → [MBA](MBA.md)
    - ← [リズムラダーなるものを検討する](リズムラダーなるものを検討する.md)
    - ← [ひとりビジネスホテル 2020/11/14](ひとりビジネスホテル_2020_11_14.md)
    - ← [指がヒリヒリする](指がヒリヒリする.md)
- → [井戸端](井戸端.md)
    - ← [最近の（？）若者って凄すぎない？](最近の___若者って凄すぎない_.md)
    - ← [takker](takker.md)
    - ← [Xについて書かれたAさんBさんの意見をかんたんに見る的な何か](Xについて書かれたAさんBさんの意見をかんたんに見る的な何か.md)
- → [Firefoxがあまりに重いので履歴を全部消した](Firefoxがあまりに重いので履歴を全部消した.md)
    - ← [Firefox](Firefox.md)
    - ← [じぶんリリースノート 0.32.11](じぶんリリースノート_0.32.11.md)
- → [自宅の回線速度が遅い](自宅の回線速度が遅い.md)
    - ← [House1の問題](House1の問題.md)
    - ← [WiMAX2+](WiMAX2+.md)
