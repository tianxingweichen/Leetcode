#!/usr/bin/env python
# coding=utf-8
import sys
class Solution(object):
    def __init__(self):
        self.results = []
        self.book = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    def isSame(self, target, table):
        if len(target) != len(table):
            return False
        for i in range(len(target)):
            q = self.book[target[i]]
            if table[i] not in q:
                return False
        return True
    def dfs(self, start, target, table):
        if len(table) > len(target):
            return
        if self.isSame(target, table):
            self.results.append(table)
            return 
        for i in range(start, len(target)):
            letter = self.book[target[i]]
            for j in letter:
                self.dfs(i+1, target, table+j)
    def letterCombinations(self, digits):
        if digits=='':
            return []
        self.dfs(0, digits,  "")
        return self.results

digits = sys.stdin.readline().strip()
sol = Solution()
results = sol.letterCombinations(digits)
print(results)

