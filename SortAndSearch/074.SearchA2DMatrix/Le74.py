class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        if matrix[0][0] > target or matrix[m-1][n-1] < target:
            return False
        high = m - 1
        low = 0
        while low <= high:
            mid = (low+high)/2
            if target == matrix[mid][0]:
                return True
            elif target > matrix[mid][0]:
                low = mid + 1
            else:
                high = mid - 1
        row = mid
        if matrix[mid][0] > target:
            if mid > 0:
                row = mid - 1
            else:
                return False
        low = 1
        high = n - 1
        while low <= high:
            mid = (low+high)/2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                low = mid + 1
            else:
                high = mid - 1
        return False