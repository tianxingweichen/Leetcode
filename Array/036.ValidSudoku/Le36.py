class Solution(object):
    def isValidSudoku(self, board):
        m = [0,0,0,1,1,1,2,2,2]
        n = [0,1,2,0,1,2,0,1,2]
        for i in range(9):
            tempr = [0 for k in range(9)]
            tempc = [0 for k in range(9)]
            tempo = [0 for k in range(9)]
            for j in range(9):
                if board[i][j] != '.':
                    tempr[int(board[i][j])-1] += 1
                if board[j][i] != '.':
                    tempc[int(board[j][i])-1] += 1
                d = m[i]*3 + m[j]
                h = n[i]*3 + n[j]
                if board[d][h] != '.':
                    tempo[int(board[d][h])-1] +=1
            tempr.sort()
            if tempr[-1] > 1:
                return False 
            tempc.sort()
            # print(tempc)
            if tempc[-1] > 1:
                return False
            tempo.sort()
            if tempo[-1] > 1:
                return False
        return True
