#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def numTrees(self, n):
        if n<3:
            return n
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[n]
