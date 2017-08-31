#!/usr/bin/env python
# coding=utf-8
import sys
class Solution(object):
    def numDistinct(self, s, t):
        dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1) ]
        for j in range(len(s)+1):
            dp[j][0] = 1
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                    print(i,j)
                else:
                    dp[i][j] = dp[i-1][j]
        print(dp)
        return dp[len(s)][len(t)]
s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

sol = Solution()
print(sol.numDistinct(s,t))

