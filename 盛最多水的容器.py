# -*- coding: utf-8 -*-
class Solution:
    def maxArea(self, height):
        # 这个暴力法是最蠢的
        # length = len(height)
        # if length == 2:
        #     if height[0] >= height[1]:
        #         return height[1]
        #     else:
        #         return height[0]
        # max_area = 0
        # for i in range(1, length):
        #     for j in range(i):
        #         if height[i] >= height[j]:
        #             area = height[j] * (i - j)
        #         else:
        #             area = height[i] * (i - j)
        #         if area >= max_area:
        #             max_area = area
        # return max_area

        # 然后换成用双指针来解决这个问题
        # 一个在头，一个在尾
        length = len(height)
        if length == 2:
            if height[0] >= height[1]:
                return height[1]
            else:
                return height[0]
        pre_cur =length - 1
        back_cur = 0
        max_area = 0
        while pre_cur != back_cur:
            if height[pre_cur] >= height[back_cur]:
                area = (pre_cur - back_cur) * height[back_cur]
                # 变的话一定是把先矮的一端进行改变,来判断能不能让面积增加
                back_cur = back_cur + 1
            else:
                area = (pre_cur - back_cur) * height[pre_cur]
                pre_cur = pre_cur - 1
            if area >= max_area:
                max_area = area
        return max_area




print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))

