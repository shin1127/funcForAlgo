
# 再帰関数を使わずに多次元行列をflattenせよ


## 考えたこと

次の2つの関数に分けると解決しやすいと考えた。

1. 与えられた配列がn次元であると判定する関数をつくる
2. (n - 1) 回flattenする

### 与えられた行列は何次元か？

与えられたリスト型の行列 array の要素 i をひとつずつ取り出し、type(i)によってクラス型を判定する。  
要素からひとつずつクラス型を取り出し、list型かどうかを比較する。  
arrayにlist型のクラスが含まれていれば、配列の次元を数える変数 count をインクリメントする。  
次に、arrayをflattenする。  
クラス型比較前のcountと、クラス型比較後のcountが一致しているかどうかを調べる。  

countが一致しないとき、これはまだ配列の中に配列が存在していることを意味するので、ループ処理によりtype(i)によるクラス型判定へと戻る。
countが一致したとき、これは配列の中に配列は存在しないことを意味するので、ループ処理を終了する。  

最後にcountの数値を調べ、与えられた配列が何次元かを判定する。  

### flattenする

以下の関数を用いる。
```Python

sum(array, [])

```

## ソースコード（できたところまで）

```Python
#  行列が何次元か数える

array = [1, 2, [3, 5], 6]

checker = [i for i in array]  # ディープコピーする

print(checker)

count = 1

while True:

    changeNumber = count
    hoge = []

    for i in checker:
        if list == type(i):
            count += 1  # リスト型があれば次元の数をインクリメント
            break  # for文のブレイク

    for i in checker:  # リストの中身を1次元下げる
        hoge.append(i)

    checker.clear()

    for i in hoge:  # checkerの中身を1次元下がったものに入れ替える
        checker.append(i)

    if changeNumber == count:  # 次元の変化がなければwhile文ブレイク
        break

print(hoge)
print(count)
```

```Python

array = [[1. 2], [3], [4, 5, [6]]]
checker = [i for i in array]  # ディープコピーする

count = 1

print(checker)

while True:
    if list in [type(i) for i in checker]:
        print("YES")
        count += 1
        print(count)
    break
````

