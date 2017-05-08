class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        tri = [[1],[1,1]]
        for i in range(2,numRows):
            d = [1 for z in range(i+1)]
            for j in range(1, i):
                d[j] = tri[i-1][j-1] + tri[i-1][j]
            tri.append(d)
        return tri