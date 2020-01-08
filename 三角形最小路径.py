# -*- coding: utf-8 -*-
class Solution:
    def minimumTotal(self, triangle):
        high = len(triangle)
        res = 0
        if high == 0:
            return 0
        if high == 1:
            return triangle[0][0]
        for i in range(high):
            for j in range(len(triangle[i])):
                # print("i:" + str(i))
                if i == j == 0:continue
                elif j ==0 and i != high - 1:
                    triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] = triangle[i - 1][j - 1] + triangle[i][j]
                    if triangle[i][j] <= res:
                        res = triangle[i][j]
                elif i == high - 1 and j == 0:
                    triangle[i][j] = triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
                    res = triangle[i][j]
                else:
                    triangle[i][j] = min(triangle[i - 1][j], triangle[i - 1][j - 1]) + triangle[i][j]
                    if triangle[i][j] <= res:
                        res = triangle[i][j]
                # print("triangle[i][j]:" + str(triangle[i][j]))
                # print("res:" + str(res))
        return res

print(Solution().minimumTotal([[-1],[-2,-3]]))
