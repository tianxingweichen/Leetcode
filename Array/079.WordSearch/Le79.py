class Solution:
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        def dfs(x, y, word):
            if len(word)==0:
                return True
            tmp = board[x][y]
            if x>0 and board[x-1][y]==word[0]:
                board[x][y]="#"
                if dfs(x-1,y,word[1:]):
                    return True
                board[x][y]=tmp
            if x < m-1 and board[x+1][y]==word[0]:
                board[x][y]="#"
                if dfs(x+1,y,word[1:]):
                    return True
                board[x][y]=tmp
            if y>0 and board[x][y-1]==word[0]:
                board[x][y]="#"
                if dfs(x,y-1,word[1:]):
                    return True
                board[x][y]=tmp
            if y<n-1 and board[x][y+1]==word[0]:
                board[x][y]="#"
                if dfs(x,y+1,word[1:]):
                    return True
                board[x][y]=tmp
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i,j,word[1:]):
                        return True
        return False