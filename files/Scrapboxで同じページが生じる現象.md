## Scrapboxで同じページが生じる現象
<a href="https://gyazo.com/3fe40cce30bb0575f4ad90481ecfc3b4" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/3fe40cce30bb0575f4ad90481ecfc3b4/raw)</a>

- あとで調べるけど、たぶん以下どっちかだと思う
    - MacとWindowsで濁点の文字コードが違う問題
        - [GitHub 上で同じ日本語ファイル名が二つ存在してしまう問題 - stamemo](https://stakiran.hatenablog.com/entry/2018/01/05/143953)
    - 追加読み込みで表示する際の境界ページがこれになる仕様

<br>

- 気のせいか
    - <a href="https://gyazo.com/ca849c6eef0bc4f03bb495748e9e09f4" target="_blank" rel="noopener noreferrer">![](https://gyazo.com/ca849c6eef0bc4f03bb495748e9e09f4/raw)</a>
    - Gyampが境界だったけど別に増えてない
    - ユビキタスも増えてない

<br>

