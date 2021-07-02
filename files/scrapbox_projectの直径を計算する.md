## scrapbox projectの直径を計算する
[/villagepump/井戸端の直径](https://scrapbox.io/villagepump/井戸端の直径)

- コードリーディングしたい

<br>

- links

```js
links = {
    "title1": links1,
    "title2": links2,
}
```

- ...
    - たぶんこうなってる
        - fromEntriesは `[key,value](key,value.md)` を `{ key:value}` に変換している
        - [JavaScriptでObject.entries/fromEntriesでreduceの利用頻度を減らす](https://zenn.dev/terrierscript/articles/2021-04-02-java-script-object-entities)
    - links？
        - [/scrapboxlab/api/pages/:projectname/search/titles](https://scrapbox.io/scrapboxlab/api/pages/:projectname/search/titles)
        - ページ内のリンク（たぶんリンク先ページ名）
    - つまり links_per_title 
- `for (const p in links) `
    - for in ってなんだっけ
        - p に key が入る
        - つまり`for (const title in links_per_title) `
- `links[p].forEach(l => {` の部分
    - `links[p]` は、`links = links_per_title[title](p]`_は、`links_=_links_per_title[title.md)` のことだな
    - `l` には、今見てる title の links の各値（つまりページtitleのリンク先ページ名）が来る
    - `links[l]`
        - これは `links_per_title[l]`
- うー、コード書き換えながら見ていくべきだな

<br>

2021/05/15 時点の元コードから[机上リファクタリング](机上リファクタリング.md)している

```js
self.addEventListener('message', async ({data: project}) => {
 let diameter = 0;
 let diameterList;

    const links_per_titles = await getLinkInfo(project);
    for (const title in links_per_titles) {
  // p: 距離を測る元ページのタイトル
  let visited = new Set();
  let distList = [[[], title]];  // 辿ったページリストと現在のページのペア（=経路）のリスト
  let depth = 0;

  while (true) {
   const nextList = [];  // titleから1歩進んだ経路のリスト
   distList.forEach(([pred, title]) => {
    links_per_titles[title].forEach(linkto_title_of_this => {
     // pのリンク先の各ページを見る
     const this_linkto_exists = (links_per_titles[linkto_title_of_this] === undefined
     if (not this_linkto_exists) {
      return;
     }
     
     already_visited = visited.has(linkto_title_of_this)
     if(already_visited){
      continue; // forEachの中でcontinueってできるんだっけ？（できるとみなす）
     }
     // 未訪問なら1歩進んだ経路を追加する
     visited.add(linkto_title_of_this);
     // ★predって何の略？
     // ...ってなんだっけ？ → pythonでいう *args や
     // とりあえず pred は最初は [] だから、newpred も [] やな
     const newPred = [...pred]; // copy
     newPred.push(title);
     nextList.push([newPred, linkto_title_of_this]);
     
     // ★次読むなら、この二周目以降から
    });
   });
   if (nextList.length == 0) {
    // 行き止まり
    break;
   }
   // 現在の経路リストを更新して繰り返す
   distList = nextList;
   depth++;
  }

  // 今までで最長の経路なら、経路長と経路の中身の記録を更新
  const newDist = depth - 1;
  if (newDist > diameter) {
   diameter = newDist;
   diameterList = [...distList[0][0], distList[0][1]];
  }
 }
    self.postMessage(diameterList);
});

// 全ページのリンク情報を取得
async function getLinkInfo(project = scrapbox.Project.name) {
   const rawPages = [];
   let followingId = null;
   do {
    const param = followingId === null ? '' : `?followingId=${followingId}`;
    const res = await fetch(
     `https://scrapbox.io/api/pages/${project}/search/titles${param}`
    );
    followingId = res.headers.get('X-Following-Id');
    rawPages.push(...(await res.json()));
   } while (followingId);
   
    return Object.fromEntries(rawPages.map(p => [p.title, p.links]));
}
```

<br>

- うー、軽く見たけど、頭追いつかん感じ
    - アルゴリズム系は大体こうなる
        - というか久々すぎてｗ
        - だいぶ鈍ってるな
            - まあ[SIer](SIer.md)だもんね……
            - コード書く場合も一人でつくっておしまいのパターンばかりやもん
        - これでも全盛期の頃は脳内でどんどん構造を再現してシミュレートできてたんや……
    - が、いけないことはない:sta:
        - 俺もエンジニア名乗るならこれくらいサクッと読めなきゃダメンゴよ
- 次やるときの戦略
    - ガチで机上トレースして書きながら見ていくか、デバッグ実行で変数の値見ながらするかしないとダメそう
    - あとローカルでVSCodeとか使って置換使いながら[机上リファクタリング](机上リファクタリング.md)した方がいい
        - Scrapbox上でコード書くのはきっちい
    - 先にデータ構造全部洗い出して、名前付け直す
        - predは、わからんならテキトーに名前つけなおす
        - 捕食する、的な意味っぽい？
            - <https://eow.alc.co.jp/search?q=pred&ref=sa>
            - 経路たどることを「捕食する」とたとえているのだろう
        - prevのtypoっぽい？

<br>

## 2hop Links
- → [1](1.md)
    - ← [PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現](PythonでinlineのScrapbox記法をMarkdown記法に変換する正規表現.md)
    - ← [isTaskPageの残骸](isTaskPageの残骸.md)
    - ← [カクヨムに書いた小説を KDP で出版する](カクヨムに書いた小説を_KDP_で出版する.md)
- → [SIer](SIer.md)
    - ← [プロフィール](プロフィール.md)
    - ← [「部下のメンタル不調」を見抜く3つのサイン](「部下のメンタル不調」を見抜く3つのサイン.md)
    - ← [知的生産で食べていきたい](知的生産で食べていきたい.md)
