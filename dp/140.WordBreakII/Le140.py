#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def check(self, s, wordDict):
        length = len(s)
        dp = [0 for i in range(length+1)]
        dp[0]=1
        for i in range(1,length+1):
            for j in range(i+1):
                if dp[j]!=0 and s[j:i] in wordDict:
                    dp[i] = True
        return dp[length]
    def dfs(self, s, dicts, stringlist):
        if self.check(s, dicts):
            if len(s)==0:
                Solution.res.append(stringlist[1:])
            for i in range(1,len(s)+1):
                if s[:i] in dicts:
                    self.dfs(s[i:], dicts, stringlist+' '+s[:i])
    def wordBreak(self, s, dict):
        Solution.res = []
        self.dfs(s, dict, '')
        return Solution.res
