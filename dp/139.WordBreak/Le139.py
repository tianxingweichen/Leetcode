#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def wordBreak(self, s, wordDict):
        length = len(s)
        dp = [False for i in range(length+1)]
        dp[0] = True
        for i in range(1,length+1):
            for j in range(i+1):
                if dp[j]==True and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[length]
