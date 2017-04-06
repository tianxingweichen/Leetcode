class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        matrix2 = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                matrix2[i][j] = matrix[n-1-j][i]
                # print(matrix[n-1-j][i])
        # print(matrix)
        matrix = matrix2
        return matrix
        