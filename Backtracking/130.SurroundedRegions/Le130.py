#!/usr/bin/env python
# coding=utf-8
import sys
class Solution(object):
    def fill(self, x, y):
        if x<0 or x>self.m-1 or y<0 or y>self.n-1 or self.board[x][y]!='O':
            return
        self.queue.append((x,y))
        self.board[x][y]='*'
    def bfs(self, x, y):
        if self.board[x][y]=='O':
            self.fill(x, y)
        while self.queue:
            cur = self.queue.pop(0)
            i = cur[0]
            j = cur[1]
            self.fill(i+1, j)
            self.fill(i-1, j)
            self.fill(i, j+1)
            self.fill(i, j-1)
    def solve(self, board):
        self.board = board
        m = len(board)
        if m==0:
            return
        n = len(board[0])
        self.m = m
        self.n = n
        self.queue = []
        for i in range(m):
            self.bfs(i, 0)
            self.bfs(i, n-1)
        for j in range(1, n-1):
            self.bfs(0, j)
            self.bfs(m-1, j)
        for i in range(m):
            for j in range(n):
                if self.board[i][j]=='O':
                    self.board[i][j]='X'
                elif self.board[i][j]=='*':
                    self.board[i][j]='O'
