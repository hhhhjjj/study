# -*- coding: utf-8 -*-
class Solution:
    def maximum69Number (self, num):
        num = str(num)
        length = len(num)
        if length == 0:
            return None
        if length == 1:
            return 9
        for i in range(length):
            if num[i] == "6" and i + 1<=length - 1:
                # python里面字符串创建就不可以修改了
                return int(num[:i] + "9" + num[i + 1:])
            elif num[i] == "6" and i == length - 1:
                return int(num[:i] + "9")
        return int(num)


print(Solution().maximum69Number(96))


