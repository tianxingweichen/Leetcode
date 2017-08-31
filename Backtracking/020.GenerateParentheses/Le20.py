#!/usr/bin/env python
# coding=utf-8
import sys
class Solution(object):
    def __init__(self):
        self.results = []
        self.bracket = ['(',')']
    def judgeParent(self, table):
        table = list(table)
        length = len(table)
        stack = []
        for i in range(length):
            if table[i]=='(':
                stack.append(table[i])
            else:
                if len(stack)==0:
                    return False
                else:
                    if stack.pop()!='(':
                        return False
        if len(stack)==0:
            return True
        else:
            return False
    def dfs(self, n, table):
        if len(table)==(n*2):
            if self.judgeParent(table):
                self.results.append(table)
            return
        for i in self.bracket:
            self.dfs(n, table+i)
    def generateParenthesis(self, n):
        self.dfs(n, '')
        return self.results
n = int(sys.stdin.readline().strip())
sol = Solution()
results = sol.generateParenthesis(n)
print(results)
        
