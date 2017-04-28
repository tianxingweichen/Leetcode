class Solution(object):
     def setZeroes(self, matrix):
         m = len(matrix)
         n = len(matrix[0])
         temp = [[0 for i in range(n)] for j in range(m)]
         for i in range(m):
            for j in range(n):
                if temp[i][j] == 0 and matrix[i][j] ==0:
                    for k in range(m):
                        if matrix[k][j] != 0:
                            temp[k][j] = 1
                        matrix[k][j] = 0
                    for k in range(n):
                        if matrix[i][k] != 0:
                            temp[i][k] = 1
                        matrix[i][k] = 0
                    temp[i][j] = 1
