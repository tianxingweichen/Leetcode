#!/usr/bin/env python
# coding=utf-8
import sys
class Solution(object):
    def isScramble(self, s1, s2):
        l = len(s1)
        dp = [[[False for _len in range(l+1)] for j in range(l)] for i in range(l)]
        for i in range(l):
            for j in range(l):
                if s1[i]==s2[j]:
                    dp[i][j][1] = True
        for _len in range(2,l+1):
            for i in range(l-_len+1):
                for j in range(l-_len+1):
                    for k in range(1,_len):
                        if dp[i+k][j+k][_len-k] and dp[i][j][k] or (dp[i][j+_len-k][k] and dp[i+k][j][_len-k]):
                            dp[i][j][_len] = True
        return dp[0][0][l]

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
sol = Solution()
print(sol.isScramble(s1,s2))

        
