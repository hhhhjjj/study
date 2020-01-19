# -*- coding: utf-8 -*-
def lists_combination(lists, code=""):
    '''输入多个列表组成的列表, 输出其中每个列表所有元素可能的所有排列组合
    code用于分隔每个元素'''
    try:
        import reduce
    except:
        from functools import reduce

    def myfunc(list1, list2):
        return [str(i) + code + str(j) for i in list1 for j in list2]

    return reduce(myfunc, lists)

res = lists_combination([[1,2], [3,4], [5,6]])
print(res)