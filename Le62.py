import numpy as np
class Solution(object):
    def uniquePaths(self, m, n):
        table = np.zeros([m,n],'int32')
        for i in range(m):
            table[i,0] = 1
        for i in range(n):
            table[0,i] = 1
        if m==1 or n==1:
            return 1
        for i in range(1,m):
            for j in range(1,n):
                table[i,j] = table[i-1,j] + table[i,j-1]
        return table[m,n]
