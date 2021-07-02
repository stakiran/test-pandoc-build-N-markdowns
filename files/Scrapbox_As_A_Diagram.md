## Scrapbox As A Diagram
構成図として

<br>

- [AWSの構成図つくるのマジでしんどい](AWSの構成図つくるのマジでしんどい.md)
- Scrapbox、というかWikiでつくればいいんじゃね？
    - 構成図も階層構造とリンクと表現しきれるから、Wikiで表現しきれる
    - 別に図である必要性はないでしょ
- そう、図を描くのはしんどいから、構造を書くんだよ
    - Drawじゃねえんだよ
    - Writeするんだ
    - [描くな、書け](描くな、書け.md)
- 1リソース1ページ、@containsで子を列挙、@useで依存

```scb
vpc_main

@contains
 private_subnet_1
 private_subnet_2
 public_subnet_1
 public_subnet_2

@contains
 ig_1

@contains
 nat_gateway_1
 nat_gateway_2
```

- 気が向いたら書いてみるわ

<br>

書いてみた

- [/test-scbo-as-a-diagram](https://scrapbox.io/test-scbo-as-a-diagram)
- AWS限定だが
- 記法
    - `@contains`で「私は～～というAWSリソースを含んでます」をぶら下げる
        - `@contains_dynamically`は「動的に含まれたり含まれなかったりするもの」、インスタンス系やコンテナ系等
    - `@boundary-from`で「私は～～という ingress firewall を持っています」をぶら下げる
    - `config`で「私は～～という設定値を持っています」をぶら下げる
        - 端的に書く
        - Q: configと@containsの違いは？
            - @containsは**AWSリソースを**含むの意
    - `context`で「私の設定値の根拠や背景は～～です」をぶら下げる
        - 端的に書く
        - なぜそうなっているかはちゃんと書いておく
        - コードコメントと同じ
    - n個冗長化する場合は`(i)`をつける
        - `[i]`だとscrapboxではリンクになってしまう。。。
    - ページ名ではリソースの種類を先に持ってくる
        - x `nat-gateway-1`
        - x `natgateway-1`
        - o `gateway-nat-1`
        - これは俺の好みかもなー:sta:
    - `@contains`は種類ごとに分けて書く

```ダメな例
@contains
 [subnet-private(i)]
 [subnet-public(i)]
 [gateway-internet-1]
```

- ...
    - ...

```良い例
@contains
 [subnet-private(i)]
 [subnet-public(i)]

@contains
 [gateway-internet-1]
```

- ...
    - `@contains`はリンクしない
        - [でかすぎるリンク](でかすぎるリンク.md)になって意味を成さない
        - 一方で、`@boundary-from`は「ingress firewallを持つもの」を俯瞰できるし、でかすぎることもないので（`[@boundary-from](@boundary-from.md)`とリンクして）良い
- 感想
    - o
        - Scrapboxのリッチな機能でガシガシつくれるの快適
            - 補完が強いのでリンクですぐ繋げられる
        - 今見ているページ（リソース）とその直近の関係だけにフォーカスできるので、読みやすい
    - x
        - 一目で俯瞰できない
            - が、俯瞰は正直（構成図においても）諦めていいと思う
            - 俯瞰は脳内でつくればいい
            - あるいはビューとしてスクリプト等で変換してつくればいい
            - 少なくとも「常時メンテする必要のある設計図として」つくるのは違う気がする
                - メンテコスト高いんだよ
                - Q: それじゃ「IaCコード見ろ」にならない？
                    - ならない
                    - 優れたプログラマーならそれでいいんだけど
                    - コードだけだとさすがに理解に時間かかる
                    - かといって常時メンテ必要な俯瞰設計図はやりすぎ
                    - ちょうど良い塩梅が「俯瞰はできないけどWikiライクに書ける・見れる設計図」ではないかってことでこれを試しているのです:sta:
        - contains書くのに迷うことがある
            - ALBとか
            - 今回はsubnetの下にぶら下げた
                - [aws_lb - Resources - hashicorp/aws - Terraform Registry](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lb)にsubnetsというargumentがあったので
            - 人によってどこにぶら下げるか変わりそう。。。
- 総評
    - 少なくとも俺一人では有意義
    - 皆で設計したりレビューしたりするときもこれでいいんじゃねえかなって思えた
        - `@contains`など記法はつくりながら決めていけばいい
    - Q: 会社（OneNoteしか使えない）でやるとしたら？
        - 厳しいかなぁ
        - 理由1: 機能面UI面でScrapboxよりはるかにダメダメなので、スムーズにつくれない
        - 理由2: こういう「自分たちで新しいやり方やフォーマットつくってやっていく」スタイルに、他のチームメンバーがついてこれない
            - [ソフトウェアエンジニア](ソフトウェアエンジニア.md)やプログラマーじゃないとなかなか厳しい印象:sta:
            - （そもそも俺のこのやり方が有意義かどうかという問題もあるがそれはまた別の話）

<br>

## Links
- ← [My Wtta](My_Wtta.md)
- ← [AWSの構成図つくるのマジでしんどい](AWSの構成図つくるのマジでしんどい.md)
- ← [Scrapbox As A XXXX](Scrapbox_As_A_XXXX.md)

## 2hop Links
- → [描くな、書け](描くな、書け.md)
    - ← [書くな、描け](書くな、描け.md)
- → [でかすぎるリンク](でかすぎるリンク.md)
    - ← [Scrapboxにおけるリンクの意味](Scrapboxにおけるリンクの意味.md)
    - ← [毛玉問題](毛玉問題.md)
- → [AWSの構成図つくるのマジでしんどい](AWSの構成図つくるのマジでしんどい.md)
    - ← [負けず嫌いで仕事中にイライラする](負けず嫌いで仕事中にイライラする.md)
    - ← [図や絵は描き込めるよりも埋め込める方が良い](図や絵は描き込めるよりも埋め込める方が良い.md)
