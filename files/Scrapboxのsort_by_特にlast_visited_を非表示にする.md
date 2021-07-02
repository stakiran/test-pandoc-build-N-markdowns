## Scrapboxのsort by(特にlast visited)を非表示にする
<a href="https://gyazo.com/a798cc504bea75ae62559695c19b90e7" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/a798cc504bea75ae62559695c19b90e7/raw)</a>

<br>

- [last visited](last_visited.md)で[承認欲求](承認欲求.md)満たしてる感がある
    - [圧倒的な自己満足](圧倒的な自己満足.md)がしたいのに人の反応を気にしているのが良くない
        - ~~[マゾが使うScrapbox](マゾが使うScrapbox.md)のきらいもあるし……~~
    - :sta:消しちゃおうか
- ってことで消す

<br>

**日記**

- 2020/11/08 気にしなくなって編集に集中できる（というより気が散らない）のでよろしいです
- 2020/12/03 気になってちょっと覗いた
    - [sta](sta.md)が369view
    - most viewでも100viewいかないくらい
    - last visited見てもほとんどくられた形跡がない
        - たぶんSEOで稀に検索からやってきたくらい
    - [Open Secret](Open_Secret.md)じゃないが、良い感じに[圧倒的な自己満足](圧倒的な自己満足.md)できてるな
- 2020/12/30 人に読んでもらうこと前提で構築し直したので再開（消してたの再表示した）
    - [Scrapboxのピン留めページを再考する](Scrapboxのピン留めページを再考する.md)
    - staが417

<br>

**一番シンプルな実装**

- sort by をまるごと消す（他のソートも使えなくなるデメリット）
    - :sta:普段からろくに使ったことないし、これで試してみるか

```css
 /* hidden sort menu especially last visited */
 .page-sort-menu {
  display: none;
 }
```

<br>

**last visited項目だけ消すには？**

- イベントで menuitem 表示がトグルになってるのでだめっすね
- CSSで言えば以下のような感じになるが

```css
/* 同上, last visited item だけ消す */
.page-sort-menu > .dropdown > .dropdown-menu-right > li:nth-child(4) > a:nth-child(1) : {
  display: none;
}
```

<br>

## Links
- ← [rmaruon](rmaruon.md)
- ← [scrapbox-shuffler](scrapbox-shuffler.md)
- ← [Scrapbox日記](Scrapbox日記.md)

## 2hop Links
- → [Open Secret](Open_Secret.md)
    - ← [Spaces](Spaces.md)
    - ← [OO主義](OO主義.md)
    - ← [他人のScrapboxなんて誰も見ない](他人のScrapboxなんて誰も見ない.md)
- → [圧倒的な自己満足](圧倒的な自己満足.md)
    - ← [ランニングマン縛り](ランニングマン縛り.md)
    - ← [Scrapboxの哲学](Scrapboxの哲学.md)
    - ← [自分の作品でうっとりする](自分の作品でうっとりする.md)
- → [承認欲求](承認欲求.md)
    - ← [気持ち悪がられたいという性癖](気持ち悪がられたいという性癖.md)
    - ← [Scrapbox to Markdown](Scrapbox_to_Markdown.md)
    - ← [虚無](虚無.md)
- → [sta](sta.md)
    - ← [作業机](作業机.md)
    - ← [吉良野すた](吉良野すた.md)
    - ← [BBSとしてのScrapbox](BBSとしてのScrapbox.md)
- → [Scrapboxのピン留めページを再考する](Scrapboxのピン留めページを再考する.md)
    - ← [Scrapbox日記](Scrapbox日記.md)
    - ← [2020年末年始](2020年末年始.md)
- → [last visited](last_visited.md)
    - ← [Scrapboxと承認欲求を切り離す](Scrapboxと承認欲求を切り離す.md)
    - ← [Scrapboxをくる](Scrapboxをくる.md)
    - ← [Last visited as a Serendipity](Last_visited_as_a_Serendipity.md)
