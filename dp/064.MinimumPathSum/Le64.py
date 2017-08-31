#!/usr/bin/env python
# coding=utf-8
import sys
class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        for i in range(1,n):
            dp[0][i] = dp[0][i-1]+grid[0][i]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[m-1][n-1]

sol = Solution()
try:
    lines = []
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        line = list(map(int,line.split()))
        lines.append(line)
    print(sol.minPathSum(lines))
except:
    pass


