## Scrapbox As A Matching
はじめに

- 半ば妄想に近い[ビジネスネタ](ビジネスネタ.md)
- そもそもScrapboxは規約で出会いを禁止している
    - [Scrapboxの利用規約](Scrapboxの利用規約.md)

<br>

Scrapbox As A Matchingとは？

- Scrapboxでマッチングしたらどうなるかなぁと
- [Scrapbox婚活](Scrapbox婚活.md)にも使えるのでは？
- 今思いついてる手段
    - マッチングで使うデータを[Scrapbox As A Database](Scrapbox_As_A_Database.md)か[Scrapbox As A Configuration](Scrapbox_As_A_Configuration.md)でつくっておく
        - たとえばAさんの[/project-A-for-matching](https://scrapbox.io/project-A-for-matching)と、Bさんの[/project-B-for-matching](https://scrapbox.io/project-B-for-matching)がある
        - AさんとBさんのマッチング = [/project-A-for-matching](https://scrapbox.io/project-A-for-matching)と[/project-B-for-matching](https://scrapbox.io/project-B-for-matching)を照合してマッチングを判定
        - つまり「これこれのフォーマットに準拠したprojectつくっておいたら、相性判断ができるよ」
        - これこれのフォーマット、はまだ練れてない
            - が、[二択マッチング](二択マッチング.md)がつくりやすいのではと思ってる

<br>

3

- aさんのprojectAと、bさんのprojectB
- AとBをマッチングすることで、aとbの相性を出す
- 素のprojectだと表現自由度高すぎて厳しい気がする
    - そもそも僕みたいに[全部入りScrapbox](全部入りScrapbox.md)つくってる人は少数派
    - public project持ってる人でも用途が限定されてて、回答情報は入れたくないケースが多そう
    - とすると、後述する「マッチング用のprojectを新たに作る」はほぼtrueにある
        - :sta:いやでも
            - Scrapboxユーザーが欲しいのって「こんな私と相性が良い人知りたい」でしょ
                - つまり「既にバリバリoutputしていて」「そんな自分に合った人と出会いたい」
            - 二択マッチングである必要はない
                - 性格じゃなくて思考や嗜好が似ている人と繋がりたい、かもしれない
                - だとしたら性格が反映された情報は要らない
- 「マッチングさせるためにこれこれこういうページつくってね」？
    - それはどういうページ？
    - [二択マッチング](二択マッチング.md)の回答載せるとか？
        - [Q:毎日定時退社したいですか？](Q_毎日定時退社したいですか_.md)
        - [Q:喫煙しますか？](Q_喫煙しますか_.md)
        - フォーマット定めるのしんどそー
            - 一行目を回答にして、幅を持たせる？
            - `y|Y|yes|YES|Yes|はい`
        - 質問一覧をjsonにしておけばエクスポートできる
            - 個人public projectに突っ込んでもいいし、マッチング用に新たにpublic projectつくってもいい
- 必要なもの
    - マッチングアルゴリズム
    - 質問の具体例や粒度
- :train:「嗜好が似た者同士で集まることの是非」に関する情報が欲しい
- :sta:んー、これ単に「マッチングを[Scrapbox As A Database](Scrapbox_As_A_Database.md)か[Scrapbox As A Configuration](Scrapbox_As_A_Configuration.md)で実装する」ってだけの話がしてきた

<br>

2

- もうちょっと具体的に広げませんか
- 2つあるね
    - 1: AさんのprojectとBさんのprojectをマッチングする
        - プロジェクト間マッチング
    - ~~2: 1つのproject内で、AさんとBさんをマッチングする~~
        - ~~プロジェクト内マッチング~~
    - いったん1:だけで考える

<br>

1

- どんなイメージ？
    - 利用者は自分のユーザーページをメンテする
    - 他の人が書き込んでもいい
    - リンクでつなげて？

<br>

## Links
- ← [My Wtta](My_Wtta.md)
- ← [Q:喫煙しますか？](Q_喫煙しますか_.md)
- ← [Q:毎日定時退社したいですか？](Q_毎日定時退社したいですか_.md)
- ← [Scrapboxでマッチングを実現する](Scrapboxでマッチングを実現する.md)

## 2hop Links
- → [全部入りScrapbox](全部入りScrapbox.md)
    - ← [ScrapboxのPage数を増やすコツ](ScrapboxのPage数を増やすコツ.md)
    - ← [Scrapbox As A Brarea](Scrapbox_As_A_Brarea.md)
    - ← [全部入りScrapboxでもAs A Reflectionしたい](全部入りScrapboxでもAs_A_Reflectionしたい.md)
- → [Scrapbox As A Database](Scrapbox_As_A_Database.md)
    - ← [Scrapbox As A XXXX](Scrapbox_As_A_XXXX.md)
    - ← [自分で設計する"受動的な情報収集源"](自分で設計する_受動的な情報収集源_.md)
    - ← [Gyampっぽいの自作したい](Gyampっぽいの自作したい.md)
- → [Scrapboxの利用規約](Scrapboxの利用規約.md)
    - ← [Scrapbox婚活](Scrapbox婚活.md)
    - ← [やっぱり妹ものが最強だなあ](やっぱり妹ものが最強だなあ.md)
    - ← [Scrapboxで複数人下ネタproject](Scrapboxで複数人下ネタproject.md)
- → [Scrapbox As A Configuration](Scrapbox_As_A_Configuration.md)
    - ← [Scrapbox As A XXXX](Scrapbox_As_A_XXXX.md)
    - ← [詰めマイン](詰めマイン.md)
    - ← [scrapbox-reminder](scrapbox-reminder.md)
- → [二択マッチング](二択マッチング.md)
    - ← [２択総研](2択総研.md)
