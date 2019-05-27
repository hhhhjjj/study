# coding=utf-8
"""题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个n级的台阶总共有多少种跳法？"""
# 先分类讨论把简单的0,1,2分类出来
# 如果台阶级数大于2
# 第一次跳有两种选择，你要么跳一级要么跳两级
# 这个跳两级不能算两个一级这样子，因为是第一次跳，所以两个一级应该同样算到一级里面


class Solution:
    def jumpFloor(self, number):
        # write code here
        if number==0:
            return 0
        if number==1:
            return 1
        if number==2:
            return 2
        ans=[0 for i in range(0,number+1)]
        ans[1],ans[2]=1,2
        for i in range(3,number+1):
            # 这个其实就是斐波那契数列
            ans[i]=ans[i-1]+ans[i-2]
        return ans[number]


if __name__ == '__main__':
    solution = Solution()
    n=int(input())
    ans=solution.jumpFloor(n)
    print(ans)


