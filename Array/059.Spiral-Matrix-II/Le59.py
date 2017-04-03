class Solution(object):
    def generateMatrix(self, n):
        lists = []
        left = 0
        right = n-1
        top = 0
        down = n-1
        matrix = [[0 for i in range(n)] for j in range(n)]
        mins = min(right-left, down-top)
        i = 0
        j = 0
        d = 1
        while mins > 0:
            while j <= right:
                matrix[i][j] = d
                j = j + 1
                d = d + 1
            j = j - 1
            i = i + 1
            while i <= down:
                matrix[i][j] = d
                i = i + 1
                d = d + 1
            i = i - 1
            j = j - 1
            while j >= left:
                matrix[i][j] = d
                j = j - 1
                d = d + 1
            j = j + 1
            i = i - 1
            while i > top:
                matrix[i][j] = d
                d = d + 1
                i = i - 1
            i = i + 1
            j = j + 1
            left = left + 1
            right = right - 1
            top = top + 1
            down = down - 1
            mins = min(right-left, down-top)
        if mins == 0:
            while j<=right:
                matrix[i][j] = d
                d = d + 1
                j = j + 1
            d = d - 1
            j = j - 1
            i = i + 1
            while i<=down:
                matrix[i][j] = d
                i = i + 1
                d = d + 1
        return matrix
       