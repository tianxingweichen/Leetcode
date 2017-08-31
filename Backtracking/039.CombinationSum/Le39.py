#!/usr/bin/env python
# coding=utf-8
import sys
class Solution(object):
    def __init__(self):
        self.results = []
    def dfs(self, candidates, target, last, table):
        if target==0:
            self.results.append(table)
        if target<0:
            return
        for i in candidates:
            if i > target:
                continue
            if i < last:
                continue
            self.dfs(candidates, target-i, i, table+[i])
    def combinationSum(self, candidates, target):
        self.dfs(sorted(candidates), target, 0,[])
        return self.results

candidates = sys.stdin.readline().strip()
candidates = list(map(int, candidates.split(' ')))
target = int(sys.stdin.readline().strip())
sol = Solution()
results = sol.combinationSum(candidates, target)
print(results)



