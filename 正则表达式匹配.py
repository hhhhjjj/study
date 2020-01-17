# -*- coding: utf-8 -*-
class Solution:
    def isMatch(self, s, p):
        # # 多出来的b*这部分没处理好，还是来看题解吧
        # # 第一种方法是用回溯
        # # 其实.还是好处理的，就是*不好处理
        # # 如果*出现在后面一位，那么有两种选择，一个是删除这两个字符，一个是删除匹配第一个字符的。就这两种情况，来回溯就行
        # # 这个用的是回溯加上递归
        if not p:
            # 注意在没有p的时候不能返回false,要返回not s
            # s为None的时候，not s是True
            # print(not s)
            return not s
        # 第一个字符进行匹配
        first_match = bool(s) and p[0] in {s[0], "."}
        if len(p) >=2 and p[1] == "*":
            # 判断第二个字符，进行回溯,其实也简单，一个or就行
            # 删除这两个字符              删除匹配第一个字符的。就这两种情况，来回溯就行
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])


        # 第二种方法就是用动态规划，题目有最优子结构，就是问题的最优解包含子问题的最优解,其实就是和之前的一样构造dp矩阵
        # s的前i个能不能被p的前j个匹配



print(Solution().isMatch("aa", "a*"))



