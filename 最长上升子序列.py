# -*- coding: utf-8 -*-
# 最长上升子序列，其实也是动态规划的方法
# 子串是连续的，但是子序列不是连续的
class Solution:
    def lengthOfLIS(self, nums):
        length = len(nums)
        if length == 0: return 0
        if length == 1: return 1
        # 这个是走到i的时候，计算前面的最长子序列，前面每一个都要遍历一下
        # 如果nums[i]大于nums[j]，那么就可以加一，不然就跳过
        # 先构造一个dp出来存储值
        dp = [1]*length
        for i in range(length):
            for j in range(i):
                if nums[j] < nums[i]:
                    # 这个dp[i]是记录之前的最长序列
                    # 状态转移方程
                    dp[i] = max(dp[i],dp[j] + 1)
        return max(dp)
