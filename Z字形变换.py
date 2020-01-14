# -*- coding: utf-8 -*-
class Solution:
    def convert(self, s, numRows):
        # 这题目找的规律就好办了，其实就是补上成完整的就行
        length = len(s)
        if length <= 1 or numRows == 1:
            return s
        a_box = numRows + numRows - 2
        integers = length // a_box
        remainder = length % a_box
        res = ""
        if remainder != 0:
            s = s + " " * (a_box - remainder)
            integers = integers + 1
        for i in range(integers):
            if s[a_box * i] != " ":
                res += s[a_box * i]
        for i in range(numRows - 1):
            for j in range(integers):
                if s[a_box * j + i + 1] != " ":
                    res = res + s[a_box * j + i + 1]
                if s[a_box * (j + 1) - i - 1] != " " and i != numRows - 2:
                    res = res + s[a_box * (j + 1) - i - 1]
        return res


print(Solution().convert("AB", 1))





