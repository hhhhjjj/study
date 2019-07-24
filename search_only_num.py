class Solution:
    def singleNumber(self, nums):
        # 这个用字典应该还是比较好想到的，现在比较好的方法是位运算，用的异或XOR
        # 相同的二进制位进行XOR返回是0,0和二进制位XOR得到这个二进制位
        # 两个值不同就结果为1
        # 这玩意还满足交换律和结合律
        # a异或b异或a最后得到b
        a = 0
        for i in nums:
            a ^= i
            return a


Solution().singleNumber([2, 2, 1])
