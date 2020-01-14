# -*- coding: utf-8 -*-
# class Solution:
#     def longestPalindrome(self, s):
#         length = len(s)
#         if length == 1:
#             return s[0]
#         if length == 0:
#             return ""
#         # 想了半天这种题目还是用动态规划来做，之前想的方法是暴力的
#         # 大问题的最优解如何由小问题的最优解得到？
#         # P(i, j)就两种情况，一种是从i到j是回文，一种就是不是
#         # 状态转移方程P(i, j) = P(i + 1, j - 1) and s[i] = s[j]
#         P = [([False] * length) for i in range(length)]
#         # 有的时候要注意状态压缩，不然这个矩阵太大了
#         max_length = 1
#         start = 0
#         for i in range(length):
#             P[i][i] = True
#         for i in range(length):
#             for j in range(i):
#                 if s[i] == s[j]:
#                     if i - j < 3:
#                         # 这里i - j不能等于三，不然的话就夹了四个数进去了
#                         P[i][j] = True
#                     else:
#                         P[i][j] = P[i - 1][j + 1]
#                 if P[i][j]:
#                     if i - j + 1 > max_length:
#                         max_length = i - j + 1
#                         start = j
#                         # print(max_length)
#                         print(i)
#                         print(j)
#         # print(P)
#         return s[start:start + max_length]
# 上面用的是动态规划的解法，慢的一匹，空间复杂度还高，为n方
# 现在优化成中心扩展算法，空间复杂度降为1
class Solution:
    def longestPalindrome(self, s):
        # 因为回文中心两侧互为镜像，所以回文可以从中心展开，并且只有2n - 1个中心
        # 为什么是2n - 1个而不是n个，因为长度为偶数的回文的中心可以在两个字母中间，比如bb这样子
        # 其实就是遍历每个索引，然后往两边扩展，看最远能走多远
        # 字符和间隙都要扩散看看
        length = len(s)

        if length <2:
            return s
        max_length = 1
        res = s[0]
        for i in range(length):
            odd_str, odd_len = self.center_spead(s, length, i ,i)
            even_str, even_len = self.center_spead(s, length, i, i+1)
            if odd_len >= even_len:
                cur_max_sub = odd_str
                cur_max_len = odd_len
            else:
                cur_max_sub = even_str
                cur_max_len = even_len
            if cur_max_len > max_length:
                max_length = cur_max_len
                res = cur_max_sub
        return res

    # 在这设计一个函数，传入字符的话，中心是字符，传入空隙，中心就是空隙
    def center_spead(self, s, size, left, right):
        # 当left == right时候就说明是空隙了
        i = left
        j = right
        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
        # 最后返回的是不成立时候的条件，这时候i已经被 - 1了，j也被 + 1了
        # 然后还返回了个长度
        return s[i + 1:j], j - i -1





print(Solution().longestPalindrome("babad"))







