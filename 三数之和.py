# -*- coding: utf-8 -*-
class Solution:
    def threeSum(self, nums):
        length = len(nums)
        if length < 3:
            return []
        res = []
        # 用题解的排序加双指针，排序的话就能避免重复解了
        # 如果nums[i]大于0，那么就可以直接返回结果了，因为排序后，后面不可能再有三个数和相加为1了
        # 重复的元素直接跳过
        # 左指针i+1,右指针length-1,如果和小于0就右指针左移，大于0就左指针右移
        nums.sort()
        # 每个数值都要遍历
        for i in range(length):
            if nums[i]>0:
                return res
            if i >0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = length - 1
            while (L<R):
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while L<R and nums[L] == nums[L + 1]:
                        # 可能有多个，不能用if，要用while
                        L = L + 1
                    while L<R and nums[R] == nums[R - 1]:
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif nums[i] +nums[L] + nums[R]>0:
                    R = R - 1
                else:
                    L = L + 1
        return res



print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))