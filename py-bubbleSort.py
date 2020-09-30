ary = [1, 3, 8, 4, 6, 7]
ary_num = len(ary)

for i in range(ary_num - 1):
    is_swapped = True
    for j in range(ary_num - i - 1):
            
        if ary[j] > ary[j + 1]:
            temp = ary[j]
            ary[j] = ary[j + 1]
            ary[j + 1] = temp
            is_swapped = False
            
    if is_swapped == True:
        break

print(ary)
# [1, 3, 4, 6, 7, 8]