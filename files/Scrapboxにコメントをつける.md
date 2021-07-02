## Scrapboxにコメントをつける
- [/rashitamemo/アウトプット用のScrapboxとコメント用のScrapbox](https://scrapbox.io/rashitamemo/アウトプット用のScrapboxとコメント用のScrapbox)
    - コメント書く用のprojectを別途つくる案
- [/nishio/Scrapboxにコメント機能を付ける案](https://scrapbox.io/nishio/Scrapboxにコメント機能を付ける案)
    - [/comments](https://scrapbox.io/comments)project + ブックマークレットでページ追加していく案
    - <blockquote>ユーザは自分の書いたものが分散するのを好まず、自分のプロジェクトの中にある方を好むのではないか</blockquote>
        - 僕もこっち派
        - [井戸端](井戸端.md)でもそうだったけど、これ分かれてる
            - 自分でつくった情報を自分で持ちたい派（仮に「所有欲」と表現する）
            - 所有欲が薄い、ない派
    - [/nishio/Scrapbox擬似的多人数プロジェクト](https://scrapbox.io/nishio/Scrapbox擬似的多人数プロジェクト)
        - <blockquote>多分「共同のプロジェクトを作ってそこでやりましょう」には乗ってこない(これがなぜかの考察はまた今度)</blockquote>
            - これはたぶん[知的生産は個人的なものである](知的生産は個人的なものである.md)
            - [知的生産と議論は違う](知的生産と議論は違う.md)ってことなのかもしれない
- [/inteltank/Public scrapboxにコメントをつける#5f48fa1f84eb3a000096d9d4](https://scrapbox.io/inteltank/Public scrapboxにコメントをつける#5f48fa1f84eb3a000096d9d4)
    - <blockquote>[/wolframmemo/Scrapboxにコメントフォーム](https://scrapbox.io/wolframmemo/Scrapboxにコメントフォーム)</blockquote>
    - 元ページ見れないけど
    - たぶんブログみたいにコメント機能をつけるってことだと思う

<br>

:sta:

- [Nota, Inc.](Nota,_Inc..md)の協力は得られないものとして
    - scrapboxに新たな機能をつくってもらうことはできない
    - [/comments](https://scrapbox.io/comments)など運営がリードすると良さそうなprojectでも運営がリードすることはない
- 制約
    - 2者がやり取りをするためには、同じprojectに属する必要がある
    - 普段書いている一人projectに他人は入れたくない
    - 所有欲が強い人は、（他人のコメントであっても）自分のprojectに書きたい
- 制約にすべきか余地ありだがいったん制約とみなすもの
    - 特定ページへのコメントはscrapbox projectにて行う
        - project以外の手段でコメントしてもらってごにょごにょというアイデアもありそう
        - まあ[ScrapboxにはPOST APIがない](ScrapboxにはPOST_APIがない.md)けど
        - それでもjsonためて、あとでimport、ならできる

<br>

- [/comments](https://scrapbox.io/comments)
    - 1: 非公式に運営して、Scrapboxerなら誰もが知るレベルの有名projectにする
        - 口コミで広げられるだろう
    - 2: Scrapboxerでコメント欲しい人は以下をする
        - 自分のprojectで「コメントは[/comments](https://scrapbox.io/comments)で募集してます」的な記載
        - [/comments](https://scrapbox.io/comments)の "自分に関するページ投稿や更新" を購読（コメントされたことを知るために）
            - これどうやるんだろ
            - 検索結果をRSSで購読できるようにすれば、検索ワード工夫すればいけそうな気がす[るん](るん.md)
    - 3: コメントしたい人は以下をする
        - [/comments](https://scrapbox.io/comments)に参加
    - でも悪さをする人が怖いなー
        - 誰でも参加できる + 有名人も参加している + コメントし合う（反応する）場である
        - ↑ 悪さする人の格好の餌
        - Aさんのページaaaに対するBさんのコメントを、悪い人Cさんが改ざんするかもしれない
            - :sta:たとえば僕がこんなコメントを書いたとして
            - ↓
            - :sta:Aさんの太ももはエッチだと思います
            - こんなふうに改ざんされたとしたら……
        - みんな見てるからそういうのは大丈夫？
        - Scrapbox利用者ならリテラシーも高そうだし
    - x
        - 自分のprojectに書けない
            - かといって「自分のprojectに書いたページ」へのリンクを張る、は不親切？
            - コメント受けた側、リンク貼ってる箇条書きにぶら下げて返事する、はできる
            - さらにやりとり発生するなら、commentsのそのページ内で頑張る
            - つまり「最初のコメント」だけ所有する、という折衷案

<br>

- やり取り全部を所有するにはどうしたら？
    - ページ単位招待 ← こういうのないとダメそう
- そもそも全部所有したいか？
    - 現実的にはこうかなぁ
        - 最初のコメントは所有したい
        - <commentsのページ内でやり取りする>
        - <落ち着いた>
        - 自分のprojectで、引用などして見解をまとめる
    - 中抜きとでも言えばいいのか
        - table:中抜き

|  | 層 | 所有する？ | どこでやる？ | どうやる？ |
| - | - | - | - | - |
| 1 | 最初のコメント | y | 自分のproject | /commentsの該当ページに、コメント書いた自分のページURLを記載 |
| 2 | やりとりの開始から終了 | - | /comments | その記載リンクにぶら下げる形で会話 |
| 3 | 2を参考・引用したまとめ | y | 自分のproject |  |

<br>

- :sta:なんか新しい仕組みが一つくらい必要な気がする

<br>

## Links
- ← [Scrapbox日記](Scrapbox日記.md)

## 2hop Links
- → [るん](るん.md)
    - ← [Scrapboxでページの一部だけ公開するアイデア](Scrapboxでページの一部だけ公開するアイデア.md)
- → [ScrapboxにはPOST APIがない](ScrapboxにはPOST_APIがない.md)
    - ← [Scrapbox As A Storage](Scrapbox_As_A_Storage.md)
- → [井戸端](井戸端.md)
    - ← [最近の（？）若者って凄すぎない？](最近の___若者って凄すぎない_.md)
    - ← [takker](takker.md)
    - ← [Xについて書かれたAさんBさんの意見をかんたんに見る的な何か](Xについて書かれたAさんBさんの意見をかんたんに見る的な何か.md)
- → [知的生産は個人的なものである](知的生産は個人的なものである.md)
    - ← [ペアプロの心得](ペアプロの心得.md)
    - ← [Xについて書かれたAさんBさんの意見をかんたんに見る的な何か](Xについて書かれたAさんBさんの意見をかんたんに見る的な何か.md)
    - ← [セレンディピティ、マネジメントレス、何か、何か](セレンディピティ、マネジメントレス、何か、何か.md)
