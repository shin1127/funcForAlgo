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



# ary = [1, 3, 8, 4, 6, 7]
# ary_num = len(ary)

# # print(ary_num)

# def is_sorted(ary_num):
#     for k in range(ary_num - 1):
#         if ary[k] > ary[k + 1]:
#             return False
    
#     return True

# if is_sorted(ary_num) == False:
#     for i in range(ary_num - 1):
        
#         for j in range(ary_num - i - 1):
#             if is_sorted(ary_num):
#                 break;
                
#             if ary[j] > ary[j + 1]:
#                 temp = ary[j]
#                 ary[j] = ary[j + 1]
#                 ary[j + 1] = temp
                
#             # print(ary)

# print(ary)

# is_sortedをforでまわすのは回答としてはよくないですね。ForのなかにさらなるForは避けましょう

