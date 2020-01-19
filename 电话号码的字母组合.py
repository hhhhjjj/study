# -*- coding: utf-8 -*-
class Solution:
    def letterCombinations(self, digits):
        word_dictionary = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"],"8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
        length = len(digits)
        num_list = []
        for i in range(length):
            num_list.append(word_dictionary.get(digits[i]))
        return lists_combination(num_list)




def lists_combination(lists, code=""):
    '''输入多个列表组成的列表, 输出其中每个列表所有元素可能的所有排列组合
    code用于分隔每个元素'''
    try:
        import reduce
    except:
        from functools import reduce

    def myfunc(list1, list2):
        return [i + code + j for i in list1 for j in list2]

    return reduce(myfunc, lists)

print(Solution().letterCombinations("23"))



