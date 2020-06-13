# %記号を使わずにFizzBuzzを実装する

## 自分のソースコード

```JS
function calc3a(n){
    n = String(n);
    array = n.split("");
    str = [];
    for (s of array){
        str.push(parseInt(s));
    }
    sum = 0;
    for (n of str){
        sum += n;
    }
    return sum;
}

function calc3b(n){
    if(n <= 9){
        return n;
    }
    return calc3b(calc3a(n));
}

function calc3c(n){
    if (calc3b(n) == 3 || calc3b(n) == 6 || calc3b(n) == 9){
        return true;
    }
    else{
        return false;
    }
}

function calc5a(n){
    n = String(n);
    nLen = n.length;
    array = n.split("");
    lastNum = array.slice(-1)
    
    if (nLen > 0){
        if (lastNum == 0 || lastNum == 5){
            return true;
        }
        else{
            return false;
        }
    }
    else{
        if (lastNum == 5){
            return true;
        }
        else{
            return false;
        }
    }
    
}

function fzbz(n){
    for (var i = 1; i <= n; i++){
        if (calc3c(i) && calc5a(i)){
            console.log("FizzBuzz");
        }
        else if (calc3c(i)){
            console.log("Fizz");
        }
        else if (calc5a(i)){
            console.log("Buzz");
        }
        else{
            console.log(i);
        }
    }
}

fzbz(100);
```

## 他の解き方

n > 0 を満たす限り、愚直に引き算し続ける  
できなくなったら戻り値を返す
```JS
[...Array(101).keys()].slice(1).map(n=>{
    let fizz = buzz = n;
    while (fizz > 0) fizz -= 3;
    while (buzz > 0) buzz -= 5;
    return (fizz == 0 ? 'Fizz' : '') + (buzz == 0 ? 'Buzz' : '') || n
});
```
