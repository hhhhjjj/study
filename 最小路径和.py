# -*- coding: utf-8 -*-
# leetcode第64题最小路径和
class Solution:
    def minPathSum(self, grid):
        # 还不会动态规划，先跟着题解走一遍
        # 先出转移方程，当前的最小路径和为min（上方的最小路径和，左方的最小路径和） +  当前的值
        # 扫过的时候会把当前的值变成最小路径和
        if len(grid) == len(grid[0]) == 1:
            return grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 开始循环遍历每一行，每一个值都去计算一遍
                if i == j == 0: continue
                # 这个就是在第一行，那么就不看上一行的了，值改成了到目前这个位置的路径和
                elif i == 0: grid[i][j] = grid[i][j - 1] +grid[i][j]
                elif j == 0: grid[i][j] = grid[i -1 ][j] +grid[i][j]
                # 不在边界就找左和上的最小路径和
                else:grid[i][j] = min(grid[i][j - 1], grid[i - 1][j]) + grid[i][j]
        return grid[-1][-1]







