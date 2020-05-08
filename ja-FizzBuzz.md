# JavaにおけるFizzBuzz

```Java

public class Main {
    public static void main(String[] args) {
        fzbz(10);
    }
    
    private static void fzbz(int num){
        
        int i = 1;
        
        while(true){
            
            if (i % 15 == 0){
                System.out.print("FizzBuzz");
            }
            else if (i % 3 == 0){
                System.out.print("Fizz");
            }
            else if (i % 5 == 0){
                System.out.print("Buzz");
            }
            else{
                System.out.print(i);
            }
            
            if (i == num){
                break;
            }
            
            i++;
            
            System.out.print(" ");
        }
    }
}
```

最後の数字を判定した後、半角スペースが出力されないように工夫。
