def sortFunc(array):
    for i in range(len(array)):
        if i == 0:
            continue
        m = 0
        for _ in range(i):
            if array[i - 1 + m] >= array[i + m]:
                temp = array[i - 1 + m]
                array[i - 1 + m] = array[i + m]
                array[i + m] = temp
                
                m -= 1
            else:
                break
    print(array)

array = [8, 5, 4, 1, 9, 6, 7, 3, 2]
sortFunc(array)
