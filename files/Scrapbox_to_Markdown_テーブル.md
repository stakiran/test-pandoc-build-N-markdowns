## Scrapbox to Markdown テーブル
テーブル

- スペース含む文字はどうなる？
    - table:table

| a | a_b | a a |
| - | - | - |
|  | ←スペース含んでます | a | a |

- ...
    - ああ、そうか、start of tableのインデント数から計算できるのか
- とりあえずtable終端がコード終端とみなされてる

```py
        # コードブロックの時は特別な終端を入れる必要がある.
        def end_of_list_or_block(inblockstate_user):
            if inblockstate_user.is_left_from_codeblock_just_now():
                return END_OF_CODE
            return ADD_LINEFEED
```

- ...
    - 見てるけどわからねえなこれ……

```py
        if state.is_in_code_block: #メソッド呼び出ししてねぇ……
            self._is_left_from_codeblock_just_now = True
```

- ...
    - 直ったけど、今までのテストコードが通ってたのが不思議
        - ああ、そうか
        - function obecetがreturnされてたから、常にtrueだったのか
        - で、_is_left_from_codeblock_just_nowフラグは_is_left_just_nowと一緒に更新してるロジックになってて、かつ_is_left_just_nowはちゃんと実装してるから、（その処理に便乗して初期化されてる）just nowも初期化（False）部分はちゃんと動いてた、と
        - 今回、tableの終端というパターンを加えたことで、この偶然の動作に入らなくなって露呈した
- そもそも一度も入ってない問題
    - <a href="https://gyazo.com/1aba5e468308d576f86ab7bc3d1679e6" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/1aba5e468308d576f86ab7bc3d1679e6/raw)</a>
    - いや、こうか
        - <a href="https://gyazo.com/d9a40f93894642e5d2580e2acb18b182" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/d9a40f93894642e5d2580e2acb18b182/raw)</a>
        - テーブルタイトル部分で入ってるけど、そのあと空行入れてるのでinblock状態が死んでinlist状態になってしまっている
    - ややこいな。契機3つあるぞ
        - start of table
            - 装飾しない or テーブルタイトルを示す書き方にする
        - start of tableの次行
            - 空行は入れない（厳密に言えば空行時のモードにしない）
        - tableの中身
            - タブ区切りになってるからよしなに整える
- start of table は ok
- 次行
    - これが難しい……
    - inblockstate_userいじるしかないよな
        - 「現在行は空行だけど、前行がテーブルタイトルだったのでそのままin-table-block状態にしまーす」
    - ぐー、inblockstateクラスがmediator並に煩雑になっていく……:sta:
    - 空行に入ったときは

```py
    for scbline in lines:
        cur_indentdepth = count_indentdepth(scbline) # ここでindent=0になる
        inblockstate_user.update(scbline, cur_indentdepth)
```

- ...
    - ...
        - まだinblockだから、こっち

```py
    def _update_case_of_in_block(self, line, cur_indentdepth):
        state = self.state

        is_current_more_deep = cur_indentdepth > state.indentdepth_of_start
        if is_current_more_deep:
            return
  # ★cur_indentdepth=0になっちゃってるからこっち来ちゃうね
        if state.is_in_code_block():
            self._is_left_from_codeblock_just_now = True
        state.leave()
        self._is_left_just_now = True
```

- ...
    - ...
        - こっち来ちゃいけない
        - だからといって愚直に「テーブルのときは」みたいな特化処理を入れると汚い
        - 汎化すると？
            - 要するに「indent=0になったときでもモードを維持しなきゃいけないシチュ」ってのがある
            - 今のところ table だけだけど
            - たぶんtableしかないけど
        - うーん、だったら空行なしでいい？
            - codeblockは既に「次行はいきなりはじまるから空行要らない」にしてる
                - まあこうだからね

```例
```py            ```py  
 print('hello')    print('hello')
```

- ...
    - ...
        - ...
            - ...
                - テーブルの場合、今はこうしてる

```例
table:tableXYZ     table:XYZ
 a b c             
                   | a | b | c |
```

- ...
    - ...
        - ...
            - ...
                - これだとあかんから、↓ こうするとどうか？（codeblockと同じになるので実装は楽になる）

```例
table:tableXYZ     table:XYZ
 a b c             | a | b | c |
```

- ...
    - ...
        - ...
            - [GFM](GFM.md)が空行なしでもパースできるかよな
            - [Markdownは段落の次に空行を入れなくてもテーブルを認識できるか](Markdownは段落の次に空行を入れなくてもテーブルを認識できるか.md)
                - うーん、GFMだけお強くて対応してるって感じ
                - GFM issuesは対応してても、ghpagesでは対応してない可能性が微レ存
        - やめます
    - 「indent=0になったときでもモードを維持しなきゃいけないシチュ」を組み込む
        - いや、特化が汚い言うても、普通に差し込むしかないか

```py
is_in_between_tabletitle_and_tablecontents = cur_indentdepth==0 and state.is_in_table_block()
if is_in_between_tabletitle_and_tablecontents:
 # ★あとでわかるためにここになんかわかりやすいメモを
    return
```

- ...
    - done
        - <a href="https://gyazo.com/fcce228aedc4764a3c2101740d131f63" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/fcce228aedc4764a3c2101740d131f63/raw)</a>
        - <https://github.com/stakiran/scbjson2ghpages/commit/799243b7d2ecdfa195d5558d244d6725b09563e6>
- あとは中身
    - `| - | - | - |` ← これも必要ですね
    - ちょっと乱暴だが別案もある
        - [Markdownでテーブルタイトルをテーブルに埋め込む](Markdownでテーブルタイトルをテーブルに埋め込む.md)
        - が、どっちにしても汚いし、安直だしでいったんやめ
        - （そもそもテーブル記法使ってマトリックス書いてるのがおかしいやんね:sta:）
            - そもそもテーブルはヘッダとデータを持つ概念
            - 言い換えると列ごとにデータを並べる記法
    - これもlineだけだと先頭行かどうかがわからんのでメタか状態が要る。。。
        - いまさらすぎるけど、行指向でアプローチするの失敗だったかもしれん
    - メタでやるとしたら

```py
    for scbline in lines:
        cur_indentdepth = count_indentdepth(scbline)
        inblockstate_user.update(scbline, cur_indentdepth)
  # ★ここで「次に渡す line は table contents の一行目だよ」を表す情報を渡す
        markdown_line = scb_to_markdown_in_line(scbline, cur_indentdepth, inblockstate_user)
        markdown_line_without_icon_grammer = _icon_grammer_to_img_tag(markdown_line)

        outlines.append(markdown_line_without_icon_grammer)
```

- ...
    - ...
        - scb_to_markdown_in_lineは汎用的にしておきたいんですけど
        - が、inblockstate 使ってる時点でいまさらか
        - 本当に汎用化したいならこの1と2（前後の行を考慮しなくても line 与えられたら一意に変換できる系）を切り出すしかないです
            - <a href="https://gyazo.com/f5742bffee7487a419bf02d6e570ff78" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/f5742bffee7487a419bf02d6e570ff78/raw)</a>
            - が、scb to markdownするためには前後行の考慮は必須（むしろ肝）なので、汎用化に力入れるのは違う
    - ああ、つかinblockstateもメタか
    - つまりメタとしてどうするかが違うだけ
        - 新しく何かつくるか
        - inblockstateの中につくるか
    - Q: 「次に渡す line は table contents の一行目だよ」はどこでわかる？
        - <a href="https://gyazo.com/3332398b57e71eaadefe0c4ebce4054a" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/3332398b57e71eaadefe0c4ebce4054a/raw)</a>
    - Q: ここで処理できないの？
        - できないです
        - この関数内はline（今見てる一行分）のみ処理するもの
    - つまり、ここで「次に渡す line は table contents の一行目だよ」を誰かに渡すしかない
    - inblockstateは違うよな
        - いや、tableもin blockだから、inblock stateの一種だとみなすこともできる……
    - ~~安直に名付けるなら~~ちょっと浮かばん
    - 逆に汎用的に名付けるなら
        - 「次行に任意の行を差し込むマン」とか
        - 「特殊記法のコンテンツ（ここではtable contents）の開始に開始用文法を差し込むマン」とか
    - あー、だめかも:sta:
        - 差し込みたい`| - | - | - |` の列数は、二行目も見ないとわからない
        - やっぱり行指向限界あるってｗｗ
            - x 行指向（行のリスト）
            - o 要素のリスト
                - 要素として「テーブル」という塊をもたせる
                - たぶん普通はこの実装ですよね……
        - ……形にするの優先なので、突っ走りまふ
        - nextlineみたいな引数追加するしかないよな
            - あるいは前後コンテキストみたいな名前にしてprevlineとnextlineを入れる
            - というか他にも入れられる構造にしておく

```py
markdown_line = scb_to_markdown_in_line(scbline, cur_indentdepth, inblockstate_user, context)
```

- ...
    - ...
        - ...
            - contextだと名前広すぎる
            - 前後コンテキスト、周辺コンテキスト、prevnext、
            - いや、contextでいいか
                - context.nextline ← これは確定
                - context.prevline ← この辺は必要なら追加すればいい（できる）
        - 決まりだな
        - まとめ
            - contextを追加する
                - context.nextline
                - context.is_first_of_tablecontent()
        - いや、……

```py
for scbline in lines:
    # この中で scbline の次の行って見れます？
```

- ...
    - ...
        - ...

```py
for linenumber,scbline in enumerate(lines):
    # lines[linenumber+1]とか見ます？（汚い）
```

- ...
    - ...
        - ...
            - が、他に見る方法ないのでこれしかないぞ
            - indexerror防ぐために len(lines) とかも必要になるしなー
        - contextは何かクラスつくってラップする
    - context使って実装する
        - あー、contextにlines与えといて、update(linenumber)だけ実行して自動で更新させる手もある
            - が、ロジックが二重になるのでなしか
            - 呼び出し元から更新関数呼び出させることにする
        - ok
            - <https://github.com/stakiran/scbjson2ghpages/commit/a55155b64ad81a97a90d8046b60e8a1c9483970b>
    - あとはcontextを使うようにすればいけるはず
    - 組み込んだけど、また遠い……
- あと二つ
    - <a href="https://gyazo.com/7ecb2783257cedbd3586878cc1e0e2b8" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/7ecb2783257cedbd3586878cc1e0e2b8/raw)</a>
    - `| - |` は2行分の挿入になるが、n行挿入を今の実装は許さない
    - `['', '<br>', '']('',_'_br_',_''.md)`の空行区切り地帯がなぜかin table blockとみなされている
- in table block誤認識
    - <a href="https://gyazo.com/ce53c3b5581c75d618fc79ba5ce64f7b" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/ce53c3b5581c75d618fc79ba5ce64f7b/raw)</a>
    - 1は正しい
    - 2は正しい（空行だが、tabletitleとtablecontentsの間であり、in table block とみなさないとテーブル処理できない）
        - これを「table top blank」と呼ぶことにする
    - 3が正しくない（テーブルが終わってるので Block:False じゃないといけないし、Table:Falseじゃないといけない）
        - これを「table bottom blank」と呼ぶことにする
    - コードブロック時はちゃんとできてる
        - <a href="https://gyazo.com/bef77532f6292647127a4fe99e567783" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/bef77532f6292647127a4fe99e567783/raw)</a>
        - 1の部分はblockもcodeblockもfalse
    - step2の結果を比較すると

```table
table:3x3

 a	b	c
 1	2	3
 foo	bar	buz
★ここがend of tableだが、判定できてる？？
<br>
```

- ...
    - ...

```code
```python
 import os
 print('environment variables')
 print(os.environ)
``` ★ここでend of code判定してる
```

- ...
    - ...
        - step2処理時、今はこう
            - <a href="https://gyazo.com/5b9492426a5720ae41acfcd8da19e8ad" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/5b9492426a5720ae41acfcd8da19e8ad/raw)</a>
            - tableのときは空行入れてる
        - inblock判定してるのはinblockstate
            - `lib_scblines2markdown.py::scb_to_markdown_in_line(line, cur_indentdepth, inblockstate_user, lines_context):()::678`
            - _update_case_of_in_block()
        - ああ、わかった

```py
def _update_case_of_in_block(self, line, cur_indentdepth):
    state = self.state
    
    is_current_more_deep = cur_indentdepth > state.indentdepth_of_start
    if is_current_more_deep:
        return
    # ★ここで上述の「2は正しい」を入れてるが、この書き方だと3のケースも入ってしまう。。。
    is_in_between_tabletitle_and_tablecontents = cur_indentdepth==0 and state.is_in_table_block()
    if is_in_between_tabletitle_and_tablecontents:
        return
```

- ...
    - ...
        - is_in_between_tabletitle_and_tablecontentsを構成する変数が一つ足りない
            - テーブルごとに最初に一回だけ ← こういうのが要る
            - lineとcur_indentdepthだけでは無理です
            - context渡さないとダメ？
            - :sta:めっちゃ煩雑な実装になってくんですけど……
                - いわゆるクラス図とか書いとかないと新規メンバーが死ぬレベル
                - 本質的に煩雑な実装になっている感

```py
for linenumber,scbline in enumerate(lines):
    cur_indentdepth = count_indentdepth(scbline)
    inblockstate_user.update(scbline, cur_indentdepth, ★ここでcontext渡す？？)
    context.update(linenumber) #これ前に持ってこなきゃだけど
```

- ...
    - ...
        - ...
            - :train:凹むなぁ……
                - こうして後から後からクラスや状態導入しなきゃいけないのって俺の設計がゴミだからなんだよな
                - もっというと設計時点で網羅する俯瞰能力というか視野というか発想力というか、がない
        - contextとして何を置いておけばいい？
            - before: `cur_indentdepth==0 and state.is_in_table_block()`
                - これ違うんだよな
                - [Markdownではリスト中のコードハイライト（とテーブル）を表現できない](Markdownではリスト中のコードハイライト_とテーブル_を表現できない.md)なので、cur_indentdepth==0とは限らない
            - after: `??`
            - contextとして持った何か一つを使う感じにしたい
            - 用語つくった
        - 整理する
            - table top blank
                - step2の処理により、空行が保証される
                - 普通に処理すると in table block 状態が解除されてしまうので、解除させない処理をする
            - table bottom blank
                - blankと名付けてあるが、空行であるとは限らない
                    - [Markdownではリスト中のコードハイライト（とテーブル）を表現できない](Markdownではリスト中のコードハイライト_とテーブル_を表現できない.md)なので、cur_indentdepth==0とは限らない
                - tableの終わりを示すので、in table block 状態は解除しなければならない
                    - よって table top blank と同じ処理で済ますことはできない（今はここで苦戦している）
        - 実装どうするか
            - `_update_case_of_in_block(self, line, cur_indentdepth)`関数内の話
            - 基本的に` cur_indentdepth <= state.indentdepth_of_start`になった = ブロックを出た、である
                - table bottom blank のときはこれでよい
                - table top blank のときはこれじゃダメ
            - 今は、table top blank のときに除外する処理を書いたつもりだが、判定が甘くてbottomのときも引っかかってる
            - どう直すべきか
            - table top blank の判定を強くする
            - contextに任せる
        - context

```py
def __init__(self, lines):
    self._lines = lines
    
    self._nextline = None
    self._is_first_of_tablecontents = False
    self._is_table_top_blank = False #★これかな
```

- ...
    - done!
        - <a href="https://gyazo.com/4154024d63c621ebebc1498002cb59e5" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/4154024d63c621ebebc1498002cb59e5/raw)</a>
    - よし、だいぶ近づいてきたぞ。。。
- `| - |` は2行分の挿入になるが、n行挿入を今の実装は許さない件
    - これなー……
        - lineとして `(lineの内容)★`みたいな形で目印つけておいてから、メタで★部分を置換するくらいしか思いつかない
        - アルゴリズムが for line in lines という行指向で動いてるので、途中で lines の行数を変えることができない
        - for i,line in enumerate(lines) からの i 直接操作、みたいなことはしたくない……
            - が、するしかなさそうか……？
    - いや、できるわ

```py
for linenumber,scbline in enumerate(lines):
    cur_indentdepth = count_indentdepth(scbline)
    context.update(linenumber)
    inblockstate_user.update(scbline, cur_indentdepth, context)
    
    # markdown_line を str じゃなくて [str,] にする
    markdown_line = scb_to_markdown_in_line(scbline, ……)
    markdown_line_without_icon_grammer = _icon_grammer_to_img_tag(markdown_line)
    
    # そしたらここは outlines.extend() でマージすることになる
    # 処理遅そうだが……
    outlines.append(markdown_line_without_icon_grammer)
```

- ...
    - ...
        - 処理遅そうなのが心配
            - [/sta](https://scrapbox.io/sta)は5000page近くあるわけだからね……
            - できれば数秒以内で終わってほしさある
                - 直感的に「明らかに処理非効率的なところ」を何個も迂回しないと達成できない気がする
                - まあ[推測するな、計測せよ](推測するな、計測せよ.md)だから現時点では行動はしないけど
        - :train:こういうしょうもない解も一昨日夜はひらめかなかったんだから不思議なものだ
        - golangみたいに戻り値二つにする？
            - `markdown_line1, markdownline2 = scb_to_markdown_in_line(scbline, ……)`
            - line2は普段は使わない
            - 空チェックだけして、もしあればそれもappendする
            - line2は table の `| - | - | - |`など特殊行だろうから、_icon_grammer_to_img_tag()は要らないはず
                - そういう意味では line2 よりも「特殊行」的なネーミングにしたいな
        - pythonで return either `str` or `[str, str](str,_str.md)`みたいなことできたっけ？
            - `scb_to_markdown_in_line()`関数内でreturnの箇所がたくさんあるから、全部で`return [str,str](str,str.md)`書きたくない
            - 呼び出し元次第か

```py
either_str_or_list = scb_to_markdown_in_line(scbline, ……)
if either_str_or_listがstr:
    line1を使おう
elif either_str_or_listがlist:
    line1とline2を使おう
```

- ...
    - ...
        - ...
            - みたいな
        - 寝かせるzzz....
        - 見てる
        - eitherで分けるの煩雑なので、もう`[str](str.md)`と`[str,str](str,str.md)`にしますか
            - パフォーマンスやばそうならその時また考えればいい（たとえばeitherで実装し直せばいい）
            - <a href="https://gyazo.com/9277dc4f8c6ed1e324b155b45119b6cd" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/9277dc4f8c6ed1e324b155b45119b6cd/raw)</a>
            - （これは書いてる途中やが）
            - と思ったけど、やっぱり仰々しいな
            - ほぼ1lineが返ってくるのに for enumerate してるのが気持ち悪すぎる
        - のでeither案でやる
        - できた
            - <a href="https://gyazo.com/fd88dfe70f9603baf98c1f2c4f076a27" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/fd88dfe70f9603baf98c1f2c4f076a27/raw)</a>
        - コードの見た目
            - <a href="https://gyazo.com/b69470e917f28268a25d7a1d27c13118" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/b69470e917f28268a25d7a1d27c13118/raw)</a>
            - 汚いことに代わりはないが、for enumrate よりはまし
- 課題は解決した
- あとは実際の出力に寄せていくだけ
    - table:table

| a | b | c |  |
| - | - | - | - |
| a | b | c |  |
|  | a | b | c |
| a | b | c | d |

- ...

```上記をscb記法で書くと？(タブは\tで書くことにする)
table:table
  a\tb\tc\t
  a\tb\tc\t
  \ta\tb\tc
  a\tb\tc\td
```

- ...
    - 要するにtab区切り

```md
| a | b | c |  |
```

- ...
    - tab個数+2
        - 先頭と末尾を囲む
    - 1セルは2space空けよう
        - `| |` ← こういう1spaceだとmarkdownパーサによっては解釈されない
    - tab_delimitor_string_to_markdown_table_line()
    - アルゴリズムどうする？
        - append-in-loop式
            - `|` つけて、
            - loop
                - 要素置いて、
                - `|`つける
        - `a` → `| a |`
        - `a\tb` → `| a | b |`
        - `a\t\tb` → `| a |  | b |`
        - いけそうだな
    - いけそう
        - <a href="https://gyazo.com/b27cecffd9f46294ce9a116a0aa2f349" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/b27cecffd9f46294ce9a116a0aa2f349/raw)</a>
    - 新たな問題浮上
        - <a href="https://gyazo.com/f24b3835a7d30d4c1a3d177c9fc50466" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/f24b3835a7d30d4c1a3d177c9fc50466/raw)</a>
        - scb table lineはtab delimitorだが、先頭に限っては normalize してるせいで space delimitor になってる
        - table:たとえば

|  |  | a | a |
| - | - | - | - |
| a | a | a | a |

- ...
    - ...
        - ↑ これの1行目は `\t\ta\tb`ではなく`  a\tb`になってる
    - できた
        - <a href="https://gyazo.com/5dd713a1ab78c360562853d2a2e88aa3" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/5dd713a1ab78c360562853d2a2e88aa3/raw)</a>
        - tab delimitorをリストアする、という初見では意味不明な概念が出てきたｗ
        - <https://github.com/stakiran/scbjson2ghpages/commit/5e2fe474354684ca3756ceeab87b54b75958f5b5>
- あとは`| - |` 、つまりは table separator の個数をちゃんと反映するだけです
    - これでようやくテーブルが終わるはず……
    - `| - |` 生成アルゴリズム
        - 1 `| - |`
        - 2 `| - | - |`
        - 3 `| - | - | - |`
        - だから、
            - `| `
            - loop
                - ` - |`
        - これでいけるね
    - 個数は
        - <a href="https://gyazo.com/9daebfa87a671b42cc66b3db545a514e" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/9daebfa87a671b42cc66b3db545a514e/raw)</a>
        - そうか、context.nextline必要だと思って準備したけど
        - newlineあるからそれ使えばええやん
        - newlineのタブ数
            - table:1

| a |
| - |

- ...
    - ...
        - ...
            - table:2

| a | a |
| - | - |

- ...
    - ...
        - ...
            - table:3

| a | a | a |
| - | - | - |

- ...
    - ...
        - ...
            - それぞれタブ数は0, 1, 2
            - ~~タブ数+1回繰り返せばいい~~違います
        - もう markdown table line なので、`|`の個数

```md
| a |
```

- ...
    - ...
        - ...

```md
| a | a |
```

- ...
    - ...
        - ...

```md
| a | a | a |
```

- ...
    - ...
        - ...
            - それぞれパイプ数は 2, 3, 4
            - パイプ数-1回繰り返せばいい
                - 合わないけど
                - -2？
                - いや、上記見る限りでは-1でしょ……

```py
pipecount = len(newline.split('|'))
cellcount = pipecount - 1
table_separator = '|' + ' - |'*cellcount
return [newline, table_separator]
```

- ...
    - ...
        - ...
            - ...
                - どこがおかしい？
                - ああ、pipecountおかしいわ
                    - `len('| a |'.split('|'))`は3だ
    - あとは名前
        - `| - | - | - |`
        - これなんて呼べばいい？
        - <a href="https://gyazo.com/416b2c0205594cabe1ce6e1b460e6856" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/416b2c0205594cabe1ce6e1b460e6856/raw)</a>
        - 1はtabletitle
        - 2はtablecontents
        - 3は？
            - table separatorだった（by一昨日の俺）
            - 別にtableを分けてるわけじゃないからこのネーミングはおかしいのだが
            - いったんオレオレツールで俺には馴染んでるから許してくれ
    - done
        - <https://github.com/stakiran/scbjson2ghpages/commit/944e742c90f6ea4924bb699bd75aca7db5c62cf0>
- 末尾問題……
    - <a href="https://gyazo.com/9e0d8d2f47da49977aca8add82fe4840" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/9e0d8d2f47da49977aca8add82fe4840/raw)</a>
    - expectでは末尾スペースなしにしてる
    - どうしようかなこれ
        - [Scrapbox to Markdown#6081f6f479d3a90000cd1855](Scrapbox_to_Markdown#6081f6f479d3a90000cd1855.md)
        - 今はappend-in-loopアルゴリズムの仕様
    - しかしテストコードでは末尾スペースアリで書いてるｗ
    - ok
- table中のリンクは？
    - 今の実装的にエグそうなので、いったんパス……
- これでようやくtableワンパス通った！cong！	

<br>

## Links
- ← [Scrapbox to Markdown](Scrapbox_to_Markdown.md)

## 2hop Links
- → [GFM](GFM.md)
    - ← [Markdownは段落の次に空行を入れなくてもテーブルを認識できるか](Markdownは段落の次に空行を入れなくてもテーブルを認識できるか.md)
    - ← [Scrapbox to Markdown コードブロック](Scrapbox_to_Markdown_コードブロック.md)
- → [推測するな、計測せよ](推測するな、計測せよ.md)
    - ← [✅Linksに相当するFooterをつける](✅Linksに相当するFooterをつける.md)
    - ← [富豪的プログラミング](富豪的プログラミング.md)
    - ← [Tritask-scrapbox](Tritask-scrapbox.md)
- → [Markdownではリスト中のコードハイライト（とテーブル）を表現できない](Markdownではリスト中のコードハイライト_とテーブル_を表現できない.md)
    - ← [Scrapbox to Markdown 文法変換の設計やら実装やら](Scrapbox_to_Markdown_文法変換の設計やら実装やら.md)
    - ← [Scrapbox to Markdown リスト中のテーブルやらコードやらブロック](Scrapbox_to_Markdown_リスト中のテーブルやらコードやらブロック.md)
    - ← [ダミーリスト](ダミーリスト.md)
