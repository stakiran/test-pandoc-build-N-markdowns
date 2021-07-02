## Scrapbox用途マトリクス
難儀してるのでいったんばいちゃ

<br>

- 要素
    - Visibility 見せる/見せない Public/Private
    - Headcount 個人/複数人 Personal/Social
    - Liveness 生かす/生かさない Live/Dead
- VL
    - public live
    - public dead
    - private live
    - private dead
- VH
    - public personal
    - public social
    - private personal
    - private social
- LH
    - personal live
    - personal dead
    - social live
    - social dead

<br>

倉庫 = 死んだテキスト倉庫

Wiki = 生きたテキストを扱うシステム

table:matrix

|  | 一人？ | 見せる？ | 生かす？ |  |
| - | - | - | - | - |
|  |  |  |  | 複数人の、秘匿された、倉庫 | s pri d | prisd | pri-ND |
|  | y |  |  | 個人の、秘匿された、倉庫 | p pri d | pripd | pri-1D |
|  |  | y |  | 複数人の、公開された、倉庫 | s pub d | pubsd | pub-ND |
|  | y | y |  | 個人の、公開された、倉庫 | p pub d | pubpd | pub-1D |
|  |  |  | y | 複数人の、秘匿された、Wiki | s pri l | prisl | pri-NL |
|  | y |  | y | 個人の、秘匿された、Wiki | p pri l | pripl | pri-1L |
|  |  | y | y | 複数人の、公開された、Wiki | s pub l | pubsl | pub-NL |
|  | y | y | y | 個人の、公開された、Wiki | p pub l | pubpl | pub-1L |

<br>

- たいていは複数要素を含むので、複数要素含んでいることを表現できねばならないな

<br>

- priN
- pri1
- pubN
- pub1

<br>

- 純粋なwiki
- 純粋な倉庫

<br>

- 時間制限
- 未完成 or not

<br>

- 個人 or 複数人
    - 性善説
- 生かす or 殺す

<br>

- 死んだテキストとは？生きたテキストとは？
    - 段階がありませんか
        - lv1: display
            - 名言や引
        - lv2: log
            - 日記や記録
            - ある時間以降にピタリと更新が止む
        - lv3: 死んだテキスト、完成という概念を目指すテキスト
        - lv4: 生きたテキスト、未完成テキスト
    - lv1: 時系列縛り（対象とする時間範囲以降は修正されない）
        - 日記
            - ただし後から追記することはできる
        - 事実の引用
            - 引用箇所を変えることで修正はできる
    - 属性？
        - 期限の有無
        - 完成という名のゴールの有無
        - table:table

|  | 期限がある | 期限がない |
| - | - | - |
| ゴールがある | タスク | 検討 |
| ゴールがない | 縛りプレイ | アイデア |

- ...
    - ...
        - 微妙か（象限の中が浮かばん
    - 
    - `AU`: 追記できるし、修正もできる
    - `A-`: 追記できるが、修正はできない
    - `-U`: 追記できないが、修正はできる
    - `--`: 追記できないし、修正もできない
    - 
    - 切り出し
    - 
    - `SS`: 自分が書いたものに、自分が手を入れる
    - `SO`: 自分が書いたものに、人が手を入れる
    - `OS`: 人が手を入れたものに、自分が手を入れる
    - `OO`: 人が手を入れたものに、人が手を入れる
    - 
    - `SOO`: 自分が書いたものに人が手を入れたものに、人が手を入れる（たたき台）
    - `SOS`: 自分が書いたものに人が手を入れたものに、自分が手を入れる（補足を入れる）
    - `OSS`: 人が手を入れたものに自分が手を入れたものに、自分が手を入れる（横取り）
    - `OSO`: 人が手を入れたものに自分が手を入れたものに、人が手を入れる（補足をもらう）

<br>

<br>

:hr:

<br>

table:matrix

|  | テキストは殺したい | テキストは殺したくない |
| - | - | - |
| 人に見せたい | 1:Private Dead Text | 2:Private Live Text |
| 人に見せたくない | 3:Public Dead Text | 4:Public Live Text |

<br>

:sta:あー、ちょっとまって

「人に見せる見せない」と「個人・複数人」がごっちゃになってる

8通りかもしれん

<br>

- 1: privateな死んだテキスト
    - :skk:まあ使いたいなら
    - [Scrapbox As A Aete](Scrapbox_As_A_Aete.md)として
- 2: privateな生きたテキスト
    - :o:向いている
    - 個人の学習や知的生産活動に
    - 人に見せることは考えない
- 3: publicな死んだテキスト
    - :x:向いてない
    - [Scrapbox As A Aete](Scrapbox_As_A_Aete.md)としては割と厳しい印象がある
    - メンバーへの啓蒙コストや運用コストがある
    - メンバーが賢いなら成立するが、そうじゃない場合は割に合わない
- 4: publicな生きたテキスト
    - :o:向いている
    - リテラシーを持つ人が自然と

<br>

table:8通り案

| 一人でやりたい？ | 公開したい？ | 殺したい? |  | どう? |
| - | - | - | - | - |
|  |  |  | Team Private Live text |  |
| y |  |  | Personal Private Live text |  |
|  | y |  | Team Public Live text |  |
| y | y |  | Personal Public Live text |  |
|  |  | y | Team Private Dead text |  |
| y |  | y | Personal Private Dead text |  |
|  | y | y | Team Public Dead text |  |
| y | y | y | Personal Public Dead text |  |

<br>

ちょっと頭こんがらかってきた

<br>

## Links
- ← [Scrapbox As A XXXX](Scrapbox_As_A_XXXX.md)

## 2hop Links
- → [Scrapbox As A Aete](Scrapbox_As_A_Aete.md)
    - ← [Scrapbox As A XXXX](Scrapbox_As_A_XXXX.md)
    - ← [プライベートな用事にもScrapboxは役立つ](プライベートな用事にもScrapboxは役立つ.md)
    - ← [オフィスでの仕事で何が生まれていたか a.k.a リモートワーク時代でも取り戻したいもの](オフィスでの仕事で何が生まれていたか_a.k.a_リモートワーク時代でも取り戻したいもの.md)
