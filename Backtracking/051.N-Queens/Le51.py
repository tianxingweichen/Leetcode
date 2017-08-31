#!/usr/bin/env python
# coding=utf-8
import sys
class Solution(object):
    def __init__(self):
        self.results = []
    def isValid(self, depth, j, board):
        for i in range(depth):
            if board[i]==j or abs(depth-i)==abs(board[i]-j):
               return False
        return True
    def dfs(self, n, depth, board):
        if depth==n:
            valuelist = []
            s = '.'*n
            for i in range(n):
                if board[i]==n-1:
                    tmp = s[:board[i]]+'Q'
                else:
                    tmp = s[:board[i]] +'Q'+s[board[i]+1:]
                valuelist.append(tmp)
            self.results.append(valuelist)
        for i in range(n):
            if self.isValid(depth, i, board):
                self.dfs(n, depth+1, board+[i])
    def solveNQueens(self, n):
        self.dfs(n,0,[])
        return self.results
n = int(sys.stdin.readline().strip())
sol = Solution()
results = sol.solveNQueens(n)
print(results)


