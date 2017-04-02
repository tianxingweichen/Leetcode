import numpy as np
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        table = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            if obstacleGrid[0][i] != 1:
                table[0][i] = 1
            else:
                break
        for j in range(m):
            if obstacleGrid[j][0] != 1:
                table[j][0] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    table[i][j] = table[i-1][j] + table[i][j-1]
        return table[m-1][n-1]
