class Solution:
    def majorityElement(self, nums):
        # 直接调用计数器自动计数出来，原理还是哈希表存储之后遍历
#       还可以用排序，题目说的是众数大于 一半，那么直接拿中位数就行
# 还可以用分治法，不过最后还要合并这些，看起来也挺麻烦的
# 这种众数大于一半的也可以用投票算法，反正其他的加起来都没他多，等于都不行，就是要大于一半
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
