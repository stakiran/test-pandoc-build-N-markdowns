## Scrapbox大人数同時編集の世界
- [/villagepump/Scrapboxの未解決問題](https://scrapbox.io/villagepump/Scrapboxの未解決問題)
    - <blockquote>たとえば1projectにアクティブユーザーが千人以上、万人以上が存在しているケース</blockquote>
    - projectに対して、ログイン中のユーザーが大人数
- [/forum-jp/大人数(だいたい10人以上？)で同時編集すると重くなる](https://scrapbox.io/forum-jp/大人数(だいたい10人以上？)で同時編集すると重くなる)
    - pageに対して、編集しているユーザーが大人数

<br>

<blockquote>プロジェクト単位ではなくページ単位でwebsocket通信しているので、プロジェクトの同時接続人数を減らしても効果はないです [/forum-jp/Scrapboxのトラブルシューティングを教えて欲しい#5dc1462befa18e0000dc0f27](https://scrapbox.io/forum-jp/Scrapboxのトラブルシューティングを教えて欲しい#5dc1462befa18e0000dc0f27)</blockquote>

- これは効果ないらしい
- ってことは前述の 1-project many logged-in user は問題なさそう
- いかにして page 内同時編集数を防ぐかゲー？

<br>

