# -*- coding: utf-8 -*-
class Solution:
    def romanToInt(self, s):
        length = len(s)
        word_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        # 这个字典可以扩展，就是把IV这样子的值也记录进来，反正实际上就那么多种情况，直接枚举就是了
        if length == 1:
            return word_dict.get(s[0])
        res = 0
        i = 0
        while i < length:
            if i + 1 < length and word_dict.get(s[i]) >= word_dict.get(s[i + 1]):
                res += int(word_dict.get(s[i]))
                i = i + 1
            else:
                temp = i
                while s[temp] == s[i]:
                    if temp == length - 1:
                        res += (temp - i) * word_dict.get(s[temp])
                        break
                    temp += 1
                res += int(word_dict.get(s[temp])) - (temp - i) * word_dict.get(s[i])
                i = temp + 1
        return res




print(Solution().romanToInt("IX"))






