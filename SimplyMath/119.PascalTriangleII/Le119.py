class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        tri = [[1],[1,1]]
        for i in range(2,rowIndex+1):
            d = [1 for z in range(i+1)]
            for j in range(1, i):
                d[j] = tri[i-1][j-1] + tri[i-1][j]
            tri.append(d)
        return tri[rowIndex]