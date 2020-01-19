# -*- coding: utf-8 -*-
class Solution:
    def threeSumClosest(self, nums, target):
        # 这个和三数之和的题目差不多
        length = len(nums)
        if length < 3:
            return None
        if length == 3:
            return nums[0] + nums[1] + nums[2]
        res = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(length):
            # 这次重复的也无所谓，不用跳过
            L = i + 1
            R = length - 1
            while L<R:
                if nums[L] + nums[i] + nums[R] == target:
                    return target
                elif nums[i] + nums[L] + nums[R] > target:
                    if nums[i] + nums[L] + nums[R] - target < abs(res - target):
                        res = nums[i] + nums[L] + nums[R]
                    R = R - 1
                else:
                    if target - (nums[i] + nums[L] + nums[R]) < abs(res - target):
                        res = nums[i] + nums[L] + nums[R]
                    L = L + 1
        return res


print(Solution().threeSumClosest([1,1,1,0], -100))