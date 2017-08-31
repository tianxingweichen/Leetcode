#!/usr/bin/env python
# coding=utf-8
import sys
class Solution(object):
    def dfs(self, x, y, word, depth):
        if depth==len(word):
            return True
        if x<0 or x>self.m-1 or y<0 or y>self.n-1 or self.board[x][y]!=word[depth]:
            return False
        tmp = self.board[x][y]
        self.board[x][y] = '0'
        if self.dfs(x-1, y, word, depth+1):
            return True
        if self.dfs(x, y-1, word, depth+1):
            return True
        if self.dfs(x+1, y, word, depth+1):
            return True
        if self.dfs(x, y+1, word, depth+1):
            return True
        self.board[x][y]=tmp
        return False
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        self.board = board
        self.m = m
        self.n = n
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if self.dfs(i,j, word, 0):
                        return True
        return False
sol = Solution()
board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
        ]
word = sys.stdin.readline().strip()
print(sol.exist(board, word))

