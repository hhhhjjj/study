# -*- coding: utf-8 -*-
class Solution:
    def myAtoi(self, str):
        length = len(str)
        if length == 0:
            return 0
        cur = 0
        res_str = ""
        first_word = ""
        while cur<= length - 1:
            if str[cur] == ' ' and res_str == "":
                pass
            else:
                if (is_number(str[cur]) or str[cur] == '-' or str[cur] == "+") and first_word == "":
                    # 判断开头
                    first_word = str[cur]
                    res_str = res_str + str[cur]
                elif is_number(str[cur]) == False and first_word == "":
                    return 0
                elif first_word != "" and is_number(str[cur]):
                    # 判断中间部分
                    res_str = res_str + str[cur]
                else:
                    break
            cur += 1
        # print("res_str:" + res_str)
        if res_str == "" or res_str == "-" or res_str == "+":
            return 0
        res_int = int(res_str)
        if -(2**31) >= res_int:
            return -(2**31)
        if res_int >= 2**31 - 1:
            return 2**31 - 1
        return res_int


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False



print(Solution().myAtoi("words and 987"))

