# -*- coding: utf-8 -*-
class Solution:
    def lengthOfLongestSubstring(self, s):
        # 打算用滑窗来做,但是自己好垃圾，我的想法是用个字典来记录中间有的元素位置
        # 看了下这个题解和我的差不多啊，就是不满足要求的时候移除左边的元素
        # 这比我想的还简单，直接就一直移动就行了
        length = len(s)
        if length == 0: return 0
        if length == 1: return 1
        word_position = {}
        back_cur = 0
        max_len = 0
        cur_len = 0
        for i in range(length):
            # 长度先加一
            cur_len = cur_len + 1
            # 这里要用while，因为if只能删一次，while可以一直删完重复的
            while word_position.get(s[i]) is not None:
                # 这个是删back_cur，而不是i，这个其实就是一直删到s[back_cur] = s[i]的时候退出while循环
                word_position.pop(s[back_cur])
                back_cur = back_cur + 1
                cur_len = cur_len - 1
            word_position[s[i]] = i
            if cur_len > max_len: max_len = cur_len
        return max_len

print(Solution().lengthOfLongestSubstring("pwwkew"))

