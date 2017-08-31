#!/usr/bin/env python
# coding=utf-8
import sys
class Solution(object):
    def __init__(self):
        self.results = []
    def dfs(self, start, nums, k, table):
        if len(table)==k:
            self.results.append(table)
            return
        for i in range(start, len(nums)):
            print(self.results)
            self.dfs(i+1, nums, k, table+[nums[i]])
    def combine(self, n, k):
        nums = list(range(1,n+1))
        self.dfs(0, nums, k, [])
        return self.results
n, k = sys.stdin.readline().strip().split(' ')
n = int(n)
k = int(k)
sol = Solution()
results = sol.combine(n,k)
print(results)


