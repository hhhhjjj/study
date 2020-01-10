# -*- coding: utf-8 -*-
class Solution:
    def maxUncrossedLines(self, A, B):
        # 这种类型的我还很垃圾
        # 现在假设最大连线数为f(x,y),对于任意位置的f(i, j)
        # 如果A[i] ==B[j],也就是可以连线，那么这时候f(i,j) = f(i -1, j -1) + 1
        # 否则就不可以连接，这时候就取前一个状态的较大值
        # 感觉和我想的思路不一样，我还考虑了什么相交这些条件，还有各种乱七八糟的

        all_col = len(A)
        all_row = len(B)
        dp = [([0] * all_col) for i in range(all_row)]
        for row in range(all_row):
            for col in range(all_col):
                if A[col] == B[row]:
                    # 因为我这个是大小正好，外面没多加一圈，所以要考虑边界情况
                    if row == 0:
                        dp[row][col] = 1
                    elif col == 0:
                        dp[row][col] = 1
                    else:
                        dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])
        # print(dp)
        return dp[-1][-1]

print(Solution().maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2]))



