#!/usr/bin/env python
# coding=utf-8
import sys
import copy
class Solution(object):
    def getmap(self, s):
        length = len(s)
        dp = [[False for i in range(length)] for j in range(length)]
        dp[0] = True
        for i in range(length):

    def dfs(self, s, i,  maps, stringlist):
    def partition(self, s):
        Solution.res = []
        arr = self.getmap(s)
        self.dfs(s, 0, arr, [])
        return Solution.res

s = sys.stdin.readline().strip()
sol = Solution()
print(sol.partition(s))

