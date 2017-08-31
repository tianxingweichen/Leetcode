#!/usr/bin/env python
# coding=utf-8
import sys
class Solution(object):
    def __init__(self):
        self.results = []
    def dfs(self, start, candidates, target, table):
        if target==0 and table not in self.results:
            self.results.append(table)
            return
        if target<0:
            return
        for i in range(start, len(candidates)):
            self.dfs(i+1, candidates, target-candidates[i], table+[candidates[i]])
    def combinationSum2(self, candidates, target):
        self.dfs(0,sorted(candidates),target, [])
        return self.results
candidates = sys.stdin.readline().strip()
candidates = list(map(int, candidates.split(' ')))
target = int(sys.stdin.readline().strip())
sol = Solution()
results = sol.combinationSum2(candidates, target)
print(results)


