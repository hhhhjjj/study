# -*- coding: utf-8 -*-
class Solution:
    def intToRoman(self, num):
        # 这个比那个罗马数字转整数确实难些，在这用贪心算法
        # 在这我想的是构造成两个列表，一个是罗马数字，一个是对应的值
        # 不断的找最小的差
        roman_list = ["I", "IV", "V","IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        value_list = [1,    4,    5,   9,   10,   40,   50, 90,   100, 400,  500, 900,1000]
        length_value = len(value_list)
        res = ""
        diffrences = num
        while True:
            for i in range(length_value):
                diffrences1 = diffrences - value_list[i]
                if diffrences1 == 0:
                    res += roman_list[i]
                    return res
                if i + 1 < length_value and diffrences - value_list[i] >0 and diffrences - value_list[i + 1] < 0:
                    res += roman_list[i]
                    diffrences = diffrences1
                    break
                if i == length_value - 1 and diffrences > 0:
                    res += roman_list[i]
                    diffrences = diffrences1
            # print(res)

print(Solution().intToRoman(1994))


