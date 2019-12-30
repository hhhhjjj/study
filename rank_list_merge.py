# 在LeetCode上刷题遇到的一个阶段
# 两个有序列表合并成一个新的有序列表
# 我的想法是双指针
list1 = [1,2,3,4,5]
list2 = [4,5,6]
res = []
while list1 and list2:
    if list1[0]<list2[0]:
        res.append(list1[0])
        del list1[0]
    else:
        res.append(list2[0])
        del list2[0]
if list1:
    # 在这就是讲list1剩下的直接接到最后的结果中去
    res.extend(list1)
if list2:
    res.extend(list2)
print(res)



