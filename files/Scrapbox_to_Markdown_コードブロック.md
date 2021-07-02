## Scrapbox to Markdown コードブロック
- コードブロック
- 全然動かんｗ
    - コードの始めも終わりも動いてない
        - 始めはそもそも実装入ってない
        - 終わりは実装入れてるけど「今週前半の俺、これ何がしたいん？」状態
    - step2で終端を入れて、step3で各行（つまり`code:xxx` to `｀｀｀xxx`）をする
- step2で終端入れる
    - [Scrapbox to Markdown 文法変換の設計やら実装やら](Scrapbox_to_Markdown_文法変換の設計やら実装やら.md)の★1
    - ★1
        - リストやテーブルの場合、add \n で良い
        - コードブロックの場合、add `｀｀｀`
    - リストorテーブルかコードブロックかを判別する手段がない
    - state userにフラグがもう一つ要るなぁ
    - is_left_just_now() が「たった今ブロックから抜けました」を調べるやつ
        - ここに「たった今 "コード" ブロックから抜けました」も追加すればいい
    - フラグ更新戦略
        - if in block
            - 更新しない
        - if not in block
            - code blockに入ったら更新する
            - code blockから出たら更新する
            - それ以外は更新しない
    - code blockに入ってるかどうかはstateが持っている
    - おお、すげえ:sta:
        - <a href="https://gyazo.com/36d393ef6185474108c353a8eaceebb0" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/36d393ef6185474108c353a8eaceebb0/raw)</a>
        - [ひょいと実装](https://github.com/stakiran/scbjson2ghpages/commit/9336aef22a3edcfbf8a8d04ee6aa68e30c727ee9)したらredだったテストコードが一気にgreen
        - 普通はn回、ウン十回[TAE](TAE.md)るのに
    - ok、入った
        - <a href="https://gyazo.com/ee5424bccb112c9f221946fe1603e968" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/ee5424bccb112c9f221946fe1603e968/raw)</a>
- step3で開始入れる
    - これは[PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現](PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現.md)でよろ
    - ok
- まだ遠いのー
    - <a href="https://gyazo.com/5108dee76183e5707c91efb510ffaf39" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/5108dee76183e5707c91efb510ffaf39/raw)</a>
    - 1 なんか空行が空いちまうし中身もリストとして処理されてしまっている件
    - ~~2 空行が入らない~~こっちは★1のextra insersionを`｀｀｀\n`にすればok
- なんで？
    - ここか
        - <a href="https://gyazo.com/dc14940df063dd689889c1935a11126f" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/dc14940df063dd689889c1935a11126f/raw)</a>
    - is in listであっても、in code blockのときは変換しちゃいけない
    - あれ？is in blockとis in listの関係ってどうだっけ？
        - is in block
            - codeのときもtableのときも両方当てはまる
        - is in list
            - インデントの数で決めてる
            - 0より大きければis in list=true

```py
    def _update_case_of_not_in_block(self, line, cur_indentdepth):
     ……
        raise RuntimeError('Invalid start of block.') # ★これ入れてみたら普通に入りやがった
```

- ...
    - ...
        - いや、入るか
            - blockじゃないときに専用記法があったらcodeblockやtableblockにするぞって話なだけで
        - おかしいな
            - codeblock中の行が全部 is **not** in blockと判定されている
            - なんで
            - テストコードではちゃんと動いてるんですけど
                - i==15とかi=17とか
    - コードブロック開始後に（なぜか入ってる）空行のせいでモードが戻されてる？
        - <a href="https://gyazo.com/0e99cdd4150da5e381b6c6c9f187b5ff" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/0e99cdd4150da5e381b6c6c9f187b5ff/raw)</a>
        - bingo
            - step2の中間生成物見てみたらこうなってた
                - <a href="https://gyazo.com/d9111daab1e67561d35c4b7b4b0039a9" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/d9111daab1e67561d35c4b7b4b0039a9/raw)</a>
            - step1では無事
                - <a href="https://gyazo.com/dcc00c27310b7738c7c1a7abda41b260" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/dcc00c27310b7738c7c1a7abda41b260/raw)</a>
        - つまり`judge_extra_insertion()`の問題
    - [Scrapbox to Markdown 文法変換の設計やら実装やら](Scrapbox_to_Markdown_文法変換の設計やら実装やら.md)の話
        - table:patterns

| curlineのインデント数 | prevlineのインデント数 | どう解釈すべき？ | 備考 |
| - | - | - | - |
| …… |  |  |  |
| 1 | 0 | add \n | リスト or ブロックがはじまた |

- ...
    - ...
        - 始まりの前に空行入れてるけど
        - **コードブロックの場合は入れちゃいけないんだ**
    - done
        - <https://github.com/stakiran/scbjson2ghpages/commit/c8a68d07b42675d5deec30e79ba03e80dfa820a8>
- あと少し
    - <a href="https://gyazo.com/20aab3fafec33e0c73bbfa9ff99d979c" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/20aab3fafec33e0c73bbfa9ff99d979c/raw)</a>
    - 要するに「本来nインデントであるはずの行」からインデントを外す処理をどこでやるか
    - step1とstep2は違うから、step3かそのメタしかない
    - step3はutilなのでlineしか受け付けないはず（自分がコードブロックの中にいるとかどうとかは関知しない）
    - よってメタで処理するしかない
        - あ、でもstep3ではinblockstate使ってメタな処理してるｗ
        - :train:設計軽いとこういうほころびがでてくるよねー。。。
            - ほころびがでないような設計するってのは中々に難しい
            - 中学からのプログラミング経験で言えば、ここは才能が絡む部分だと思う
                - 圧倒的な[地頭](地頭.md)でクソースでも御するタイプと
                    - 世の中には変数名をa,a1,x,x1みたいにつけるプログラマーもいる（って話聞いたことある）
                - 何らかの才能で芸術的にシンプルでほころびのない設計をやってしまうタイプ
            - 俺は凡人なので愚直に対応していくしかない
                - せめてテストコードでホワイトボックス的に品質担保するくらいよ

```py
    # コードブロックの中身
    if is_in_block and state.is_in_code_block():
        # ただし code:xxx の開始行も in code block 判定なので
        # 置換処理もここでやるしかない.
        #
        # パフォーマンスがダメそうなら, 開始行を in code block 判定にしない等の追加処理が必要か.
        newline = re.sub(RE_CODE_BLOCK_START, '```\\2', newline)
        #
        # ★ここでインデントを解除する処理を書く
        return newline
```

- ...
    - あああああ、これ厄介だな
        - 機械的にインデント殺しちゃダメ
        - コードブロックの始まりが持つインデント数nを使って、nだけ除外してやらねばならない

```scb
たとえば
 list1
  list2
```py
   for _ in range(4):
       print('4回繰り返すじぇー')
  コード終わり
```

- ...
    - ...
        - これを変換するとこうなる

```markdown
たとえば

- list1
    - list2

```python
for _ in range(4):
    print('4回繰り返すじぇー') # ここのインデントまで殺しちゃいけない
```

- ...★このダミーリスト部分はまだ実装できてないが。。。
    - コード終わり
```

- ...
    - 正規表現だとどうなる？
        - cur_indentdepth回のスペースをキャプチャして殺したいんですけど
        - `r'( ){3}'` これで3回
        - ここにcur_indentdepthを差し込む
        - `r'( ){{}}'.format(cur_indentdepth)`？
            - でもformat使うと`{}`自体が特別な意味もっちゃって、正規表現のn回指定が使えない
    - ……愚直に文字列処理するか
    - ああ、待って、だめ
        - cur_indentdepthじゃなくて、コードブロック開始時のインデント深さが必要
            - this_codeblock_indentdepthみたいなの
            - indentdepth_of_startプロパティある
        - done
            - <https://github.com/stakiran/scbjson2ghpages/commit/f9b184e2d8e9d5cf580d29bd2fe6e0c8d096602b>
            - <https://github.com/stakiran/scbjson2ghpages/commit/a32c39a8e7bb545d1d43ef3d64dae975d1e78e4a>
- あと少し（意外と長い）
    - 言語名の統一と
        - <a href="https://gyazo.com/64ebb1c07d3669412b29bc6ca07665d7" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/64ebb1c07d3669412b29bc6ca07665d7/raw)</a>
    - ahkの[HotString](HotString.md)のとき（たぶん`:`ついててコードブロック判定になってしまってる）の謎のインデント
        - <a href="https://gyazo.com/f5fe7d508f8fcce1512f9ed6acd750e3" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/f5fe7d508f8fcce1512f9ed6acd750e3/raw)</a>
- 言語名統一
    - `        newline = re.sub(RE_CODE_BLOCK_START, '｀｀｀\\2', newline)`
    - これの延長線やな
    - `｀｀｀`でsplitして1番目の要素取り出して、あとは愚直に条件分岐するしかないか
    - パターン
        - js
        - javascript
        - JavaScriptやJSなど大文字小文字
        - hoge.jsなど拡張子
    - 全部対応するのは明らかにしんどいので、どっかから流用するべき
    - markdown、というより[GFM](GFM.md)がどうしているかも見るべき
        - 拡張子をそのまま書いて処理はできるので、少なくとも xxxx.ext は ext をそのまま使えばいい
    - あとは言語名だけ書かれてるパターン
    - いくつか例出してみるか
    - js
        - `code:ここの仕様` 以前どこかで見た気がする
        - なにかのライブラリ使ってるんだよな、たしか
        - [Scrapboxのコードハイライトはhighlight.jsを使っている](Scrapboxのコードハイライトはhighlight.jsを使っている.md)
    - と思ったけど、よく考えたらGitHub側も多分同じようなの使ってるよな
    - つまり、scrapboxが対応している言語名指定の語彙≒GitHubの語彙とみなせるのでは？
    - そやな
    - 自力実装なんてしたくないし、そうしよう
    - まとめ
        - `code:xxx`は`｀｀｀xxx`にする
        - `code:xxx.ext`は`｀｀｀ext`にする
    - 正規表現だけでは無理くない？
    - できた！
        - <https://github.com/stakiran/scbjson2ghpages/commit/8e394897608bb32977abfbf181139d02c543b4b7>
- ahkの[HotString](HotString.md)のとき（たぶん`:`ついててコードブロック判定になってしまってる？）の謎のインデント
    - あああああああああああああわかった
    - json parserでnormalize scbしてるせいだ
        - [Scrapboxのjsonにはタブとスペース両方交じる](Scrapboxのjsonにはタブとスペース両方交じる.md)ので全部スペースにしている
        - が、これだとコードブロック内のタブインデントも全部スペースになってしまう
    - どうすっかな
    - 案は2つ
        - スペースのままで通す
            - 僕はスペース派なので！
            - が、これだとタブ派の人達が使えなくなっちゃうね。。。
        - json parse時、コードブロックについてはnormalizeしない
            - というかscrapboxで通常ほ本文もタブとスペースが混ざってるの、なんか理由がある気がしてきた
            - shokaiさん達のエンジニアがあえてタブとスペースを混在させるやりづらさを放置するとは思えない
            - 何か理由があるんだ？
    - 今はプロトで早く形にしたいので、スペースのまま押し通しますん:sta:

<br>

## Links
- ← [Scrapbox to Markdown](Scrapbox_to_Markdown.md)

## 2hop Links
- → [TAE](TAE.md)
    - ← [脳内シミュレーターがしょぼい](脳内シミュレーターがしょぼい.md)
    - ← [TAE Context](TAE_Context.md)
    - ← [知的生産の5つのフェーズ](知的生産の5つのフェーズ.md)
- → [GFM](GFM.md)
    - ← [Scrapbox to Markdown テーブル](Scrapbox_to_Markdown_テーブル.md)
    - ← [Markdownは段落の次に空行を入れなくてもテーブルを認識できるか](Markdownは段落の次に空行を入れなくてもテーブルを認識できるか.md)
- → [HotString](HotString.md)
    - ← [ランダムな文字列をタイトルにしてページを新規作成する](ランダムな文字列をタイトルにしてページを新規作成する.md)
    - ← [トピック指向](トピック指向.md)
    - ← [AutoHotkeyのHotStringでブックマークエイリアス](AutoHotkeyのHotStringでブックマークエイリアス.md)
- → [Scrapboxのjsonにはタブとスペース両方交じる](Scrapboxのjsonにはタブとスペース両方交じる.md)
    - ← [Scrapbox to Markdown テストコード設計](Scrapbox_to_Markdown_テストコード設計.md)
    - ← [GitHubのMarkdownでネストしたリストが正しくレンダリングされない](GitHubのMarkdownでネストしたリストが正しくレンダリングされない.md)
    - ← [別に切に欲しくないけどなんか面白そうだからつくる](別に切に欲しくないけどなんか面白そうだからつくる.md)
- → [Scrapbox to Markdown 文法変換の設計やら実装やら](Scrapbox_to_Markdown_文法変換の設計やら実装やら.md)
    - ← [Scrapbox to Markdown](Scrapbox_to_Markdown.md)
- → [地頭](地頭.md)
    - ← [今日整理したこと](今日整理したこと.md)
    - ← [強い人は喋れる？](強い人は喋れる_.md)
    - ← [脳内シミュレーターがしょぼい](脳内シミュレーターがしょぼい.md)
- → [PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現](PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現.md)
    - ← [Scrapbox to Markdown 文法変換の設計やら実装やら](Scrapbox_to_Markdown_文法変換の設計やら実装やら.md)
    - ← [Scrapbox to Markdown 画像とicon記法の実装](Scrapbox_to_Markdown_画像とicon記法の実装.md)
