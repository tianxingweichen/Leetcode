import numpy as np
class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        table = [[0 for i in range(n)] for j in range(m)]
        table[0][0] = grid[0][0]
        for i in range(1,n):
            table[0][i] = table[0][i-1] + grid[0][i]
        for j in range(1,m):
            table[j][0] = table[j-1][0] + grid[j][0]
        for i in range(1,m):
            for j in range(1,n):
                table[i][j] = min(table[i-1][j], table[i][j-1]) + grid[i][j]
        return table[m-1][n-1]
        