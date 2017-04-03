class Solution(object):
    def spiralOrder(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        lists = []
        left = 0
        right = m-1
        top = 0
        down = n-1
        mins = min(right-left, down-top)
        i = 0
        j = 0
        while mins > 0:
            while j <= right:
                lists.append(matrix[i][j])
                print(matrix[i][j])
                j = j + 1
            j = j - 1
            i = i + 1
            while i <= down:
                lists.append(matrix[i][j]) 
                print(matrix[i][j])
                i = i + 1
            i = i - 1
            j = j - 1
            while j >= left:
                lists.append(matrix[i][j])
                print(matrix[i][j])
                j = j - 1
            j = j + 1
            i = i - 1
            while i > top:
                lists.append(matrix[i][j])
                print(matrix[i][j])
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
                lists.append(matrix[i][j])
                j = j + 1
            j = j - 1
            i = i + 1
            while i<=down:
                lists.append(matrix[i][j])
                i = i + 1
        return lists

            
