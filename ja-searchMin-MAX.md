# ArrayListの要素の最大値や最小値を求める
  
  ## どういう理屈？
  
  まず最大値を格納する変数 x に、それぞれの型が取りうる最小値を代入する。\*1  
  
  次に、ArrayListの要素 y と x で、その大小を比較する。  
  x > y ならば x に y を代入する。  
  ArrayListの要素がなくなるまでこの操作を繰り返す。  
  
  最小値を求める場合も同じ。  
  
  \*1 Math.max(x, y)を単純にループすることでも大小の比較は可能だが、ArrayListの要素が1つであった場合に対応できない。
  
  ## ソースコード
  
  ```Java
  // int型の配列の最大値を求める
    public int maxInt(ArrayList<Integer> list){
        int maxNumber = Integer.MIN_VALUE;
        for(int n : list){
            if (maxNumber < n){
                maxNumber = n;
            }
        }
        return maxNumber;
    }

    // double型の配列の最大値を求める
    public double maxDouble(ArrayList<Double> list){
        double maxNumber = Double.MIN_VALUE;
        for(double n : list){
            if (maxNumber < n){
                maxNumber = n;
            }
        }
        return maxNumber;
    }

    // int型の配列の最小値を求める
    public int minInt(ArrayList<Integer> list){
        int minNumber = Integer.MAX_VALUE;
        for(int n : list){
            if (minNumber < n){
                minNumber = n;
            }
        }
        return minNumber;
    }

    // double型の配列の最小値を求める
    public double minDouble(ArrayList<Double> list){
        double minNumber = Double.MIN_VALUE;
        for(double n : list){
            if (minNumber < n){
                minNumber = n;
            }
        }
        return minNumber;
    }
    
    ```
