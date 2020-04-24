# float型のリテラルに対して、それが整数かどうかを判断する

## どういう理屈？

与えられた2数k, nに対して、
小数点以下を切り上げた数をkx, nxとする。  
小数点以下を切り上げた数をky, nyとする。  

kx = nx, ky = ny であれば整数となる。

### 例 1
k = 1.1 のとき、
kx = 2
ky = 1
となり、False

### 例 2
x = 1.0 のとき、
kx = 1
ky = 1
となり、True

## ソースコード

```Python
import math

def isIntger(k):
    kx = math.ceil(k)
    ky = math.floor(k)
    
    return kx == ky
```
