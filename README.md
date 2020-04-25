# funcForAlgo

## Introduction

アルゴリズムに関するクイズを解答する時に利用したい関数をまとめた。
主として、以下のものを記載する。

-  （非効率的であったとしても）問題の解決手段として、発想やアプローチの仕方が独特な関数  
-  一般に知られているロジックを利用・応用し、自分なりに作成した関数

## Background
2020年4月現在、所属するWeb開発系のコミュニティで、  
『Code challenge』と称した、アルゴリズムのソースコードを記述するクイズを解き合う遊びが流行している。  

試行錯誤しながらもそれに参加していくうちに、独特な表現をするコードをいくつか思いつくことができた。  
ただし、遠回りで実用的ではないアプローチ方法にはなるかもしれないという問題点がある。  
 

これらのコードについて、そのまま解答に利用したものもあれば、  
よりよいコードを~~思いついてしまって~~ 思いつくことが出来たおかげで、置換せざるを得なかったものもある。  

とはいえ、苦心して思いついたこれらの発想を記憶の隅に追いやってしまうだとか、完成したソースコードを消去してしまうのは、もったいないことだと感じている。  
そこで、  
"いつかその発想たちを利用するケースがあるかもしれない"  
"その発想を土台にして新しい発想が生まれるかもしれない"  
ということを期待して、自分なりに整理した上で保存・公開することにした。

## Things learned
READMEの中身が膨大になってしまうことを危惧して、得られた知見は別ファイルにて列挙し、そのURLをこのセクションに記載する予定。

## Functions

### Python
- [その小数は整数と実質的に等価ですか？( 小数点以下がゼロなら整数とみなしたい )](py-thisFloatIsInt.md)
- 「リストの要素を、特定のリテラルが出るまで取り出す操作」を繰り返し、要素がなくなればループを終了する

### Java
-  [ArrayListの要素から最大値や最小値を求める](ja-searchMin-MAX.md)
-  ArrayListの要素の和を求める
-  ArrayListの要素の算術平均を求める

### JavaScript
-  リストの要素を順に取り出し、要素がなくなればループを終了する
