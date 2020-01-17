# -*- coding: utf-8 -*-
# 这个题目和前面的最长上升子序列差不多，都是动态规划来解
# 这个是可以用所有的顺序，卡到这不知道怎么解了
# 题解是先将这个数组排序，这样子就可以首字母到后面越来越大了
class Solution:
    def findLongestChain(self, pairs):
        length = len(pairs)
        if length == 0:return 0
        if length == 1:return 1
        pairs.sort()
        # 直接用这个来排序
        print(pairs)
        dp = [1]*length
        for i in range(length):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i],dp[j] + 1)
        return max(dp)

# 慢的一匹

print(Solution().findLongestChain([[9,10],[9,10],[4,5],[-9,-3],[-9,1],[0,3],[6,10],[-5,-4],[-7,-6]]))
# 优化的方法是用贪心算法