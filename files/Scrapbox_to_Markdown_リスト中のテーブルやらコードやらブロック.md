## Scrapbox to Markdown リスト中のテーブルやらコードやらブロック
鬼門の[/testdata-for-to-markdown/nested block](https://scrapbox.io/testdata-for-to-markdown/nested block)

- とりあえずファイル名やりづらいのでシンプルに
    - before: [/testdata-for-to-markdown/markdownの語彙に含まれていない表現](https://scrapbox.io/testdata-for-to-markdown/markdownの語彙に含まれていない表現)
- page-to-scbが効かないと思ったら
    - <blockquote>python scbjson2ghpages.py -i test_lib_scblines2markdown.py --page-to-scb codeblock</blockquote>
    - なんでpyファイル与えてん
        - そしてこれに気付くのに数分かかるという[天然](天然.md)
        - 勘弁してー
        - 2回目なのでtodo入れとく
    - ` python scbjson2ghpages.py -i testdata-for-to-markdown.json --page-to-scb "nested block" > 1_input_nested_block.scb`
        - ok
- 期待値書いたけど、これ相当しんどそう
    - 特にテーブル前後の[ダミーリスト](ダミーリスト.md)がえぐい
    - <https://github.com/stakiran/scbjson2ghpages/blob/3128999cae2c6a03d540fb09fb59c20f78db536d/testdata/2_nested_block_expect.md>
    - そもそもわかりづらい
        - before
            - <a href="https://gyazo.com/9c63f22966e5faaf6cce5c6e7856e9a5" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/9c63f22966e5faaf6cce5c6e7856e9a5/raw)</a>
        - after
            - <a href="https://gyazo.com/e52fc7a97262cedcae2f01f425522e26" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/e52fc7a97262cedcae2f01f425522e26/raw)</a>
    - 慣れの問題だろうか？
    - ダミーリスト以外も考えた方がいい？
        - だがmarkdownがnested block対応してないので、blockはゼロインデントで書くってのはまず確定
        - そうなると、あとは前後の「ネストされてるリスト」をどう表現するかの問題
        - ちなみにmarkdownではいきなり「nネストのリスト」は書けない
        - 例
                    - こういうのはかけない
        - 例
            - markdownで書くには
                - こんな風に
                    - 一段ごとに順番に書いていかないといけない
        - だからこその[ダミーリスト](ダミーリスト.md)なわけだが
    - ダミーリスト、`...`が（インデント数nに対して）n-1行つづくのしんどみがある
    - 別案
        - コードは全部別ファイルに移してリンクさせる
            - x markdown側のSEOが乱れる（普段見かけない構成だろうからgoogleにランク落とされるかもしれん）
            - o 実装が少し楽になる
            - x ファイル数が増える増える
                - nested blockのコードやテーブルが仮に300あったとしたら、300ファイル増えるんだぜ？
        - コードやテーブルはファイルの下にまとめる（注釈みたいな）
            - 「ブロック注釈」とか名付けられそうｗ
            - x アンカーの考慮が必要
                - [intoc](intoc.md)で散々やったけど、できればアンカーの世界には携わりたくない……
            - x 実装もまあまあだるそう
                - 読み込んだブロックを保持しておいて、最後にまとめて配置みたいなことする必要
    - いや、直感を信じよう
        - 読み手側の慣れでしょ
    - ダミーリストの実装がダメだったら、別案しますわ
- ほいじゃー、やりましょう
- とりあえず実行してみたが、まあひどい
    - <a href="https://gyazo.com/1bc868623281376b929fe59011fcef06" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/1bc868623281376b929fe59011fcef06/raw)</a>
    - 終端が上手くつくられてない
    - ダミーリストがない
    - 開始行の前に空行が空いてない
- とりあえず前々からずっとスキップしてた★2の部分を見る
    - <a href="https://gyazo.com/fc3da11ee964a07e3b9b2d840243c01f" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/fc3da11ee964a07e3b9b2d840243c01f/raw)</a>
    - 呼び出し元はこう

```py
 # list or blockが終わった
 if p==0:
     extra_insertion = end_of_list_or_block(inblockstate_user)
     return extra_insertion
 
 # list or block が続いている(インデントは変わらず or 深くなった)
 # 先頭行のときもここに入る.
 is_more_deepen = c>=p
 if is_more_deepen:
     return IGNORE
 
 # list or block が続いている(インデントは変わらず or 深くなった or 浅くなった)
 # インデント 1 以上の深さで block が終わっているケース, もここに入る.
 extra_insertion = continuous_indent(c, inblockstate_user)
 return extra_insertion
```

- ...
    - ...
        - [Scrapbox to Markdown 文法変換の設計やら実装やら#607a160279d3a90000545b64](Scrapbox_to_Markdown_文法変換の設計やら実装やら#607a160279d3a90000545b64.md)
        - p>=1 and p>c
            - ~~p=1, c=0~~ end_of_list_or_block
            - ~~p=2, c=0~~ end_of_list_or_block
            - ~~p=2, c=1~~ ~~list or block が続いている(インデントは深くなった) ★これ嘘だろ（深くなってない） ~~ok
            - ~~p=3, c=0~~ end_of_list_or_block
            - ~~p=3, c=1~~ ~~list or block が続いている(インデントは深くなった) ★これ嘘だろ（深くなってない）~~ok
            - p=3, c=2
            - ~~p=3, c=0~~ end_of_list_or_block
        - p>=1 and c>1 and p>c
            - p=3, c=2
            - p=4, c=2
            - ...
            - p=4, c=3
            - p=5, c=3
            - ...
    - 嘘だろ部分、たぶん動いてないのでけしてみる
        - ok
    - うん、これで「nインデントに入っているときに、インデントが減った」ケースになった
    - ケース全部洗い出す
        - 1
            - リスト

```py
#comment
#comment
```

- ...
    - ...
        - ...
            - リスト
        - 2
            - リスト
            - table:table

| a | b |
| - | - |
| a | b |

- ...
    - ...
        - ...
            - リスト
        - 3
            - リスト

```py
#comment
#comment
```

- ...
    - ...
        - ...

```py
#comment
#comment
```

- ...
    - ...
        - 4
            - リスト
            - table:table

| a | b |
| - | - |
| a | b |

- ...
    - ...
        - ...
            - table:table

| a | b |
| - | - |
| a | b |

- ...
    - あと終わりがリストじゃなくて段落や空行になってるケースもある
        - いずれにせよ終端をちゃんとすれば次がどれであっても対応できる
        - ただしダミーリストはちゃんと入れておく必要がある
    - まとめると
        - 終端は空行入れてちゃんとする
            - tableの場合は空行だけでいい
            - codeの場合は`｀｀｀`と空行
        - インデントが続いている場合、ダミーリストの挿入も必要
- 終端
    - <a href="https://gyazo.com/e8ac1c1657cbfa184ac9c385b40d9048" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/e8ac1c1657cbfa184ac9c385b40d9048/raw)</a>
    - ok
- 始点
    - start_of_list_or_block?
        - いや、これは現在行が`code:xxx`や`table:xxx`のときの、次の行をどうするかって話
        - 今回欲しいのは現在行が「`code:xxx`や`table:xxx`の"前の"行」であるときの話
            - 先読みなんて実装してないんですけど……:sta:
    - 道は二つあるな
        - 1: 先読みを実装する≒先読み機能を持つcontextあたりを渡すようにする
        - 2: convert_step2()で「cur/prev式のパースで対応できなかった部分に対処する後処理」を入れる
            - こっちかな
    - 後処理とは？
        - 上記画像 1 の部分に空行を入れる
        - もっと言うと、以下のパターンが出た時に空行を差し込む
            - インデント1以上の行 → `｀｀｀xxx`
            - インデント1以上の行 → `| xxx | ...`
        - あ、待てよ、ダミーリストもここでやればええんちゃう？？:sta:
    - 決まり
    - で、スケルトン書いたけど
        - <a href="https://gyazo.com/f3d302ba920f6bf7ba3195d4a6daebed" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/f3d302ba920f6bf7ba3195d4a6daebed/raw)</a>
        - これ、もう一度 inblockstate 使って注意深く書かないとダメだわ
            - 「今はリストの中にいます」「今はコードの中にいます」 ← こういうの全部考慮しなきゃいけないから
        - 仮に愚直に「リストが来た後、`｀｀｀`が来たら挿入する」処理を書いたとすると
            - コードブロックの中でそういうパターンが来たらどうするねんって話になる
            - 無論、除外しないといけない
            - そのためには「今コードブロックに入っているかどうか」も知る必要がある
            - ……
            - と処理がややこい
            - このややこい部分は、inblockstate 周りのパースでつくっている（のでそれもう一度使うしかない）
    - `_step2_insert_extra_insertion()`かな
        - つまり cur/prev 式で入れていくのが append_extra_insertion
        - 今つくろうとしてる、append だけでは無理ゲーな分を改めて入れていく insert_extra_insertion
        - うん、いけそ:sta:
            - スマートではないが、そもそも表現語彙全然違うmarkdownへの変換なんだから、こういうもんでしょ
            - だからこそ今まで誰もつくってないんだろうし
                - 簡単な scb to markdown なら何個もあるけど
                - [Markdownではリスト中のコードハイライト（とテーブル）を表現できない](Markdownではリスト中のコードハイライト_とテーブル_を表現できない.md) ← たとえばこういうのをどう対処するかまで踏み込んだツールはまだない
    - パターンを実装風に言い換える
        - <blockquote>インデント1以上の行 → `｀｀｀xxx`</blockquote>
            - end of code blockであり、in listである
        - <blockquote>インデント1以上の行 → `| xxx | ...`</blockquote>
            - end of table blockであり、in listである
    - 脳内だと追いつかん

```scb
paragraph
 list1
  list2      --- A
```py    --- B
   #comment  --- C
   #comment
   if True:  --- D
       pass  --- F
   #comment  --- G
  list2      --- H
 list
paragraph    --- I
```py      --- J
 #comment
```

- ...
    - ...
        - a-b（preがaで、curがb）
            - 挿入するべきパターン
                - preがin listである
                - curがblockである
        - b-c
            - 挿入してはいけないパターン
            - a-bの条件だけだとこれも該当してしまう
            - 弾くには？
                - indentdepth_of_start？
                    - ダメ
                    - curがBになった時点で値が入ってしまう
                    - やっぱり「先読み」か~~「is_entered_just_now()」的なものが要る……~~is_next_the_enterring_timing()的なやつ
                        - つまりは先読みですね
                        - 実装が煩雑になるから先読み入れたくない……:sta:
    - done
        - prevのin block状態覚えるフラグ導入するだけでよかた
        - <https://github.com/stakiran/scbjson2ghpages/commit/100b37d94a83e25acb243e13a7953c6f03050e06>
- 終点

```step2
    print(os.environ)
```

   もちろん維持されます（深さ含めて） ---- ここが cur になったとき
```

- ...
    - prevはblankline
    - curはin listで、インデントが1よりも大きい
        - だったらインデント1から順に入れればいいだけか
    - Q: 他に被るパターンはない？条件それだけで大丈夫？
        - curがin blockではない、も必要だな
    - ああ、ダメ

```py
# (A)
if is_prev_in_list and not is_prev_in_block and is_cur_in_block:
    ADD_LINEFEED = ''
    outlines.append(ADD_LINEFEED)
    
# (B)
# - ただしここは tabletitle と tablecontents の間の空行を通る時にも入るので, 弾く
if not is_prev_in_list and not is_cur_in_block and cur_indentdepth>1:
    if lines_context.is_first_of_tablecontents():
        pass
    else:
        outlines.append('- ...')
```

- ...
    - ...
        - みたいな実装しようとしたけど、そもそも linescontextって、step2_conveter_lines 限定だったわ……
    - わかった
        - <a href="https://gyazo.com/c15a256d97b68b443e9aba905b0531f7" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/c15a256d97b68b443e9aba905b0531f7/raw)</a>
        - 二つ前を見る必要がある
            - curが11行目（でダミーリストの`- ...`決め打ちを入れる前）のときに、2つ前である9行目がtabletitleであるかどうか
            - いや、curが単に`\t`もってたら、にすれば？
                - table:こういう一列テーブルを捕捉できないが？

| a |
| - |
| b |
| c |

- ...
    - ...
        - ...
            - ...
                - 一列テーブルなんて使ってないから、いいかい？ｗ
        - おかしいな、これで弾けるはずだが

```py
# (B)
# - ただしここは tabletitle と tablecontents の間の空行を通る時にも入るので, 弾く
if not is_prev_in_list and not is_cur_in_block and cur_indentdepth>1:
    outlines.append('- ...')
```

- ...
    - ...
        - ...
            - not is_cur_in_block（ブロックの中ではない）、を既に判定している
            - これはテーブルブロックの中ではない、も判定できている（はず）
        - inblockstateのtable版、テストコード書いてねえな……
            - 書いたけど、異常ないです
        - なんで……
            - debugprint仕込んでみた結果、そもそも入ってないことがわかった
            - あとdebugprintがそもそも動かん
                - なぜ動かんかがわからん
                - ぐー
            - スペルミス
                - 20min悩むという……:sta:
                - [天然](天然.md)すぎる……
        - 結果

```terminal
$ python test_pagetest.py
..F.is_prev_in_list, cur_indent, is_cur_in_block = False, 2, False, L:  重要でな重要である
is_prev_in_list, cur_indent, is_cur_in_block = False, 2, False, L:  a   b       c
```

- ...
    - ...
        - ...
            - in table blockのはずなのに、blockではないと判定されている
            - なんでだっけ？
            - step2のappend時点でこうなるからだよな

```scb
table:matrix_空白セルあり
★ここをパースした時点で blank line と解釈する（ので in block 状態も解除される）
  重要でない	重要である
 緊急でない	第一領域	第二領域
 緊急である	第三領域	第四領域
```

- ...
    - ...
        - ...
            - ...
                - ああ、そうか、思い出した
                - これを防ぐために lines context 導入してるんだった
                    - かつ、lines contextへのセットはパース時に自分で行う必要があるんだった
                    - <a href="https://gyazo.com/7d64c909c1362a9fb9e5f21a65b6f95e" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/7d64c909c1362a9fb9e5f21a65b6f95e/raw)</a>
                    - これと同じよう、パースする側でenableする
                - 実装も思い出した
                    - enable しておけば、inblockstate user側で勝手に上記の解除無効をやってくれるんだ
                    - first_of_tablecontentsじゃなくてtable_top_blankだった
            - 長かったがdone
    - あとはダミーリストを正しく入れるだけだ……
    - 正しく動かん
        - <a href="https://gyazo.com/28a05cc7b4a9818d599014f29596fb1b" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/28a05cc7b4a9818d599014f29596fb1b/raw)</a>

```md
- ...
    - ...
        - もちろん
```

- ...
    - ...
        - こうなるはずなんだが
        - appendしなければ何も起こらない
            - <a href="https://gyazo.com/f727e94e101b99c9836cf6456c4048e2" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/f727e94e101b99c9836cf6456c4048e2/raw)</a>
        - `outlines.extend(dummylist)` の有無だけで、上記のような`- - ...` になるってどういうことだ
        - appendeeもおかしくはない

```terminal
$ python test_pagetest.py
..is_prev_in_list, cur_indent, is_cur_in_block = False, 3, False, L:   もちろん維持されます（
深さ含めて）
['- ...', '    - ...']
```

- ...
    - ...
        - `['- ...']('-_...'.md)`ハードコードで入れた場合
            - <a href="https://gyazo.com/f40b179d37a953b5952534d706324729" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/f40b179d37a953b5952534d706324729/raw)</a>
            - `- `という余分がついているのは何なんだ……？
            - いや、`[' - ...']('_-_...'.md)`という入力データミスしてた（先頭スペース要らない）
        - `['AAA']('AAA'.md)`の場合
            - <a href="https://gyazo.com/f973d9111354bffa8d3b9b4fe4ed233a" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/f973d9111354bffa8d3b9b4fe4ed233a/raw)</a>
            - `- `どこ行った？
            - なんだ、このC言語のメモリ一部上書きしちゃってますを彷彿とさせるこの挙動は……:sta:
        - うん、問題ない
        - ああ、そうかわかった！
            - この時点ではまだ scb 記法だから、挿入するの違う
                - bf `['- ...','    - ...']('-_...','____-_...'.md)`
                - af `[' ...','  ...']('_...','__...'.md)`
        - done
            - <a href="https://gyazo.com/5c8ce07d3fb2a3de8fbdf3768eebeb72" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/5c8ce07d3fb2a3de8fbdf3768eebeb72/raw)</a>
- コードブロックはok
- 次はテーブル
    - step3
        - <a href="https://gyazo.com/0f4f92e391081c3ac34bbdb684c995e9" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/0f4f92e391081c3ac34bbdb684c995e9/raw)</a>
    - tabletitleが上手く処理されてない
        - 一つ上のリストに紐付けちゃうのが自然か
            - が、今の実装的にエグそうなかほり……
    - step2
        - <a href="https://gyazo.com/3e0f7f3b6f6dc141e4946acd9cc01959" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/3e0f7f3b6f6dc141e4946acd9cc01959/raw)</a>
        - 何の因子が絡んでるのか、パット見わからねえな
    - in list において、3通りあるんだよな
        - [Scrapbox to Markdown#60849c1679d3a90000883fe5](Scrapbox_to_Markdown#60849c1679d3a90000883fe5.md)
            - table → list
            - table → table
            - table → code
        - いや、この辺掌握するのは修羅の道
        - ~~コードブロックと同じように処理するしかない~~してました
        - `(table|code) → (table|code)`の連チャンはまだ想定してないから、後にする
    - 要するにtabletitleという異端児をどう扱うか、に帰着される
        - 案1: リスト中で扱う
        - 案2: ゼロインデントにしてしまう
    - 案1が自然だが
        - 画像の1の空行除去が必要(step2)
        - tablecontentsとの間には空行が必要(step3)
    - 案2
        - 画像の2に空行追加が必要(step2)
        - tablecontentsとの間には空行が必要(step3)
    - どっちもエグいので自然な案1にする
    - ……わからん
        - なんでこの挙動になるのか（画像の1でなぜ空行が入ってるか）作者自身も俺でも追いつかないん……
    - デバッグログ仕込んだ
        - <a href="https://gyazo.com/d14b5bbfb1a260dbea6ad07f06f7fedb" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/d14b5bbfb1a260dbea6ad07f06f7fedb/raw)</a>
        - 結論、ここに入ってる
            - <a href="https://gyazo.com/6223b258a71a9b425797bde2fe7a0546" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/6223b258a71a9b425797bde2fe7a0546/raw)</a>
            - ignoreだから何も挿入されないはずだが
        - あ、こっちや
            - <a href="https://gyazo.com/f5be1f737f25f9fa6ff17d4c73f125db" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/f5be1f737f25f9fa6ff17d4c73f125db/raw)</a>
    - ダメ、わからん
    - step2の空行除去はできた
        - <a href="https://gyazo.com/8594575bfce2996bc98766081a1f38ad" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/8594575bfce2996bc98766081a1f38ad/raw)</a>
        - けど、てーぶるは空行空いててテーブルが空いてない理由がわからん
    - step3は問題が二つあって、
        - 1 リストになってない
        - 2 table separatorが入ってない（前述のテーブルで空いてないのと関係してる気がする）
        - `<a href="https://gyazo.com/0721669fefaf172521667b63862f4bac" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/0721669fefaf172521667b63862f4bac/raw)</a>`
    - 力尽きたので終わり
- とりあえずrevertしてもう一度

```py
# paragraph
#  list1
#   list2
# ★ここに空行を差し込む処理(A)
#   code:py
#    print('hello')
# ```
#
#  ... ★ここに左記のようなダミーリストを差し込む処理(B)
#   list2

# paragraph
#  list1
#   list2
#   table:xxx
# ★ここに空行を差し込む処理(C)
#    a b
#    c d
#   list2
……
elif is_prev_start_of_table and is_cur_in_tableblock:
    # (C)
    ADD_LINEFEED = ''
    outlines.append(ADD_LINEFEED)
```

- ...
    - これ入れると破綻する
    - step3
        - <a href="https://gyazo.com/d3b6965bd82a36fc0ec96e08050b471a" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/d3b6965bd82a36fc0ec96e08050b471a/raw)</a>
- とりあえずa b cてーぶるの方でseparator入ってない問題を
    - <a href="https://gyazo.com/2169de80bca5296b25f9d6af357f9cef" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/2169de80bca5296b25f9d6af357f9cef/raw)</a>
    - どっちもstep3で t f t t。状態は正しい
    - table separatorを返すのは、scb_to_markdown_in_line() で lines_context.is_first_of_tablecontents のとき
    - enable_first_of_tablecontents() されるのは、in table block のときかつModer.is_blankline(line)のとき
    - done
        - <https://github.com/stakiran/scbjson2ghpages/commit/5ef49b2ca3098ea04cb020fcd4bc873f08c060ec>
        - ややこしすぎて死ぬ
- あと二つ
    - <a href="https://gyazo.com/ebda52f934b52b7c9e9f988199257d29" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/ebda52f934b52b7c9e9f988199257d29/raw)</a>
    - 1 リスト記法にする
    - 2 空行を入れる
- リスト記法にする
    - done
    - <https://github.com/stakiran/scbjson2ghpages/commit/973df67f7f54a5bf2734f1023f7f8c994f79234f>
- 空行を入れる
    - がー、ややこしそう:sta:
        - これ以上step3でn行 returnをつくるわけにはいかない（table separatorだけで懲り懲り）
        - のでstep2しかないわけだが、そうすると状態が変わってまた泥沼になりそうなよかん。。。
    - ああ、だよな、これで上記の (C) 問題に帰ってきたわけだ
    - 前半done

```py
# (C)
if is_prev_in_list and is_prev_start_of_table and is_cur_in_tableblock:
```

- あと一つ！
    - step3
        - <a href="https://gyazo.com/6f7e2e3ebfe74a0445db6e703757bff2" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/6f7e2e3ebfe74a0445db6e703757bff2/raw)</a>
    - なんで入らない？
    - 一列目が空になってるせいで is_cur_in_tableblock 入らないとか？
    - デバッグログで状態可視化

```前半
[step2](pL, pB, pSoT), (cB, cCB, cTB, cSoT) = 
       (True, False, False), (True, False, True, True) L:  table:てーぶる ★1
[step2]enable table_top_blank about line:  table:てーぶる
[step2](pL, pB, pSoT), (cB, cCB, cTB, cSoT) =
       (True, True, True), (True, False, True, False) L:   a   b       c ★2
[step2](pL, pB, pSoT), (cB, cCB, cTB, cSoT) =
       (True, True, False), (True, False, True, False) L:   e  1       2
```

- ...

```後半
[step2](pL, pB, pSoT), (cB, cCB, cTB, cSoT) =
        (False, True, False), (False, False, False, True) L:  table:テーブル ★3
[step2](pL, pB, pSoT), (cB, cCB, cTB, cSoT) =
        (True, False, True), (False, False, False, False) L:    重要    重要でない ★4
[step2](pL, pB, pSoT), (cB, cCB, cTB, cSoT) =
        (True, False, False), (False, False, False, False) L:   緊急
```

- ...
    - ★1は正しい
        - in blockで、in tableblock で、 start of table
    - ★2も正しい
        - in block で、in tableblockだが、 start of table ではない
    - ★3はおかしいね
        - in block判定されてない
    - ★4もおかしいね
        - 3でブロック判定されてないのでここでもされてない
    - 3でブロック判定されないバグを調べよう:sta:
- step2で空行入ってないのがおかしいか？
    - step2をした結果
        - <a href="https://gyazo.com/e6d62fce1497d37b0bbb81e40f0981fc" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/e6d62fce1497d37b0bbb81e40f0981fc/raw)</a>
        - oの方みたいに空行が入れば、enable table_top_blank になってテーブルブロック判定されるはず
    - step1をした結果
        - <a href="https://gyazo.com/dd547c421b16c8b3c4b0df9ccd79da93" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/dd547c421b16c8b3c4b0df9ccd79da93/raw)</a>
        - 結果は正しいが、上記のxの部分が（続くstep2で）対処されない
            - これ、ブロックの直後にブロック続くケースだよな
            - たぶん end of block と start of block が被ってる、でもコードは被りを想定してない……みたいな実装の穴な気がする:sta:
    - step2がおかしい
    - (A)かなぁ……

```py
# (A)
# - ただしテーブルの場合は(tabletitleをリストの一行として扱うのが自然なので)差し込まない
if is_prev_in_list and not is_prev_in_block and is_cur_in_codeblock:
    ADD_LINEFEED = ''
    outlines.append(ADD_LINEFEED)
```

- ...
    - ...
        - うん、入らないね
        - デバッグログは？

```terminal
[step2](pL, pB, pSoT), (cB, cCB, cTB, cSoT)
       (True, True, False), (True, False, True, False)   L:   f  3       4
[step2](pL, pB, pSoT), (cB, cCB, cTB, cSoT)
       (True, True, False), (True, False, True, False)   L:
[step2](pL, pB, pSoT), (cB, cCB, cTB, cSoT)
       (False, True, False), (False, False, False, True) L:  table:テーブル
```

- ...
    - ...
        - ...

```summarized
   f	3	4     in-table-block
                  in-table-block ★ここやなぁ……
  table:テーブル   not in-block
```

- ...
    - ...
        - ...
            - ちょっとどこがおかしいかわからん
        - 合ってる方

```terminal
[step2](pL, pB, pSoT), (cB, cCB, cTB, cSoT)
       (False, False, False), (False, False, False, False) L: ネスト1
[step2](pL, pB, pSoT), (cB, cCB, cTB, cSoT)
       (True, False, False), (True, False, True, True)      L:  table:てーぶる
[step2]enable table_top_blank about line:  table:てーぶる
[step2](pL, pB, pSoT), (cB, cCB, cTB, cSoT)
       (True, True, True), (True, False, True, False)       L:   a   b       c
```

- ...
    - ...
        - ...

```summerized
 ネスト1          not in-block
  table:てーぶる  in-table-block and start-of-table

   a	b	c    in-table-block
```

- ...
    - ...
        - tableが終わった後の空行は all false にならないといけない
            - <a href="https://gyazo.com/808f9a7907df67ee1601bfc663e0f4e5" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/808f9a7907df67ee1601bfc663e0f4e5/raw)</a>
    - 見てて気になったところ
        - <a href="https://gyazo.com/f74714c41e2d8b74c94dbd8d8c339646" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/f74714c41e2d8b74c94dbd8d8c339646/raw)</a>
            - 終わってないやろ、むしろ始まってるやろ
        - 自分で脳内で状態遷移ぐるぐる回してて、これあかんわってなってる
            - <a href="https://gyazo.com/e4d11ea630be038a46d3f3693d4d5d8a" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/e4d11ea630be038a46d3f3693d4d5d8a/raw)</a>
            - 全パターン書こうとしてるけど、書けない……
        - ~~リーダブルに組み直すか……？~~
            - ~~たぶん diff 使うのが良い~~
                - ~~cとpのインデント数の差~~
            - と思ったが、普通に条件式圧縮できた
                - <https://github.com/stakiran/scbjson2ghpages/commit/066b83b4960e790e27ec5f5536d88bca7903ab65>
                - <https://github.com/stakiran/scbjson2ghpages/commit/5b183b335c3aa4ed885e799f8138e1a6fbd59ff9>
        - が、ここは関係なかった
    - どこだ？
        - InBlockStateUser?
        - <a href="https://gyazo.com/8449ad2f7945aa5fc2a1b76242e20fd4" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/8449ad2f7945aa5fc2a1b76242e20fd4/raw)</a>
        - allfalse になる＝ブロック状態から解除されるっつーことは、こっから下に来てないってことだよな
        - で、来るための条件は「現在行のインデント数」が「今のブロックのstart行のインデント数」以下であること
            - 満たしてるよな
    - うーん、これはわからんー
    - <a href="https://gyazo.com/0a9c880bdabd4cc3f2c0a36ff42cd9b2" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/0a9c880bdabd4cc3f2c0a36ff42cd9b2/raw)</a>
        - 空行なのになんでブロックが続いてんだ……？
    - だよな、やっぱりtable_top_blank問題が誤って発動してるとしか思えない
        - で、デバッグ仕込んでみたら、all false になった
            - is_table_top_blank() は内部でクリアしているので、デバッグログ側で呼び出してFalseになってるってことは、すでにenableが走ってたことを意味する
        - ここしかないんやが
            - <a href="https://gyazo.com/d5b68ff7d234ca5338985b82c57152ad" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/d5b68ff7d234ca5338985b82c57152ad/raw)</a>
            - でもここ入ったらデバッグログにも enable表示でるはずやが
            - 矛盾起きてるんだが
        - だめだわかんねぇ……
    - また明日……
    - ---
    - (B)をコメントアウトしても入らなかったので、ダミーリスト処理部分は関係ない
    - あ、こうするか？
        - `[step2](pL, pB, pSoT), (cB, cCB, cTB, cSoT) 2 = (False, True, False), (False, False, False, True) L:  table:テーブル`
        - start of tableなのに cTB(in-table-block)じゃない、というおかしな状態になってる
        - ので、in-table-block に無理やりしちゃう……とか
    - とりあえず、ここが肝やな
        - cTBじゃないからtable top blankに入らないんだ
            - `if state.is_in_table_block() and is_cur_start_of_table:`
    - cTB判定は`is_cur_in_tableblock = state.is_in_table_block()`
    - 突き止めた
        - <a href="https://gyazo.com/edc00c69705efb2c628db84f9c29c1f5" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/edc00c69705efb2c628db84f9c29c1f5/raw)</a>
        - enableした後、俺は「次行でtable top blank判定している」つもりでいたが、そうじゃない
        - だいぶ離れて、今空行が入らない部分でなぜか判定が入っている……
        - 普通はこうならなきゃいけない
            - <a href="https://gyazo.com/a84172a98ef8572eda287f1a5ffb4615" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/a84172a98ef8572eda287f1a5ffb4615/raw)</a>
    - できた
        - <a href="https://gyazo.com/fa645aea8e1aafb97fa73030c6b0a440" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/fa645aea8e1aafb97fa73030c6b0a440/raw)</a>
- ダミーリスト足りてないが……
    - `if not is_prev_in_list and not is_cur_in_block and cur_indentdepth>1:`
    - start of table は既に in-table-blockなので、二番目を満たしてないな
    - `if not is_prev_in_list and cur_indentdepth>1:`？
        - いや、これだとブロック中が全部ヒットしてしまう？
        - いや、いいのでは？
            - in-listはin-blockでもある
                - （紛らわしいけど in list とはインデント持ってるって意味）
            - not in-listってことは、少なくともブロックには入ってないってことだ
    - ok
- が、今度はテーブル側で変な行できてる……
    - <a href="https://gyazo.com/7524f20dee932e4af3eacf79640c5117" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/7524f20dee932e4af3eacf79640c5117/raw)</a>
    - これは弾かないといけない
    - 最初だけダミーが入ってないのも気になる
- 条件追加で対処した
    - <https://github.com/stakiran/scbjson2ghpages/commit/4f229fa4219cfe53b4834c70f683f0114dfea214>

<br>

たぶん code → code と table → code のパターン足りてないかもー。。。

<br>

## Links
- ← [Scrapbox to Markdown](Scrapbox_to_Markdown.md)

## 2hop Links
- → [天然](天然.md)
    - ← [✅Linksに相当するFooterをつける](✅Linksに相当するFooterをつける.md)
    - ← [なぜ自動テストの導入は失敗するのか？](なぜ自動テストの導入は失敗するのか_.md)
    - ← [House1の火災保険を解約する](House1の火災保険を解約する.md)
- → [ダミーリスト](ダミーリスト.md)
    - ← [真の意味でものづくりがしたいんだよ](真の意味でものづくりがしたいんだよ.md)
    - ← [Markdownではリスト中のコードハイライト（とテーブル）を表現できない](Markdownではリスト中のコードハイライト_とテーブル_を表現できない.md)
- → [Markdownではリスト中のコードハイライト（とテーブル）を表現できない](Markdownではリスト中のコードハイライト_とテーブル_を表現できない.md)
    - ← [Scrapbox to Markdown 文法変換の設計やら実装やら](Scrapbox_to_Markdown_文法変換の設計やら実装やら.md)
    - ← [Scrapbox to Markdown テーブル](Scrapbox_to_Markdown_テーブル.md)
    - ← [ダミーリスト](ダミーリスト.md)
- → [intoc](intoc.md)
    - ← [GFM](GFM.md)
