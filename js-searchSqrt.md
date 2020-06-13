# 与えられる入力である自然数Nに対して、N >= n**2　を満たす最大の自然数nを求める

## 具体例

- N=1234567　n=1111
- N=25　n=5
- N=26　n=5

## ソースコード

二分探索法を利用する

```JS


var n = 1234567;

nSize = n.toString().length;


var rangeMin = 10 ** ((nSize - 1) / 2);
var rangeMax = 10 ** (nSize / 2);
var rangeCenter = (rangeMin + rangeMax) / 2;


while (rangeMax - rangeMin >= 1){
    if (rangeCenter ** 2 <= n){
        rangeMin = rangeCenter;
        rangeMax = rangeMax;
    }
    if (rangeCenter ** 2 > n){
        rangeMin = rangeMin;
        rangeMax = rangeCenter;
    }
    rangeCenter = (rangeMin + rangeMax) / 2;
    rangeMin -= (rangeMin % 1);

}
console.log(rangeMin);

```

## 他の簡単なやり方


```JS

const n = N ** 0.5

```
