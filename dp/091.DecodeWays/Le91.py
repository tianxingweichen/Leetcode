#!/usr/bin/env python
# coding=utf-8
import sys
class Solution(object):
    def numDecodings(self, s):
        length = len(s)
        if length==0 or s[0]=='0':
            return 0
        dp = [0 for i in range(length+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2,length+1):
            if 10<=int(s[i-2:i])<=26 and s[i-1]!='0':
                dp[i] = dp[i-1] + dp[i-2]
            elif int(s[i-2:i])==10 or int(s[i-2:i])==20:
                dp[i] = dp[i-2]
            elif s[i-1] != '0':
                dp[i] = dp[i-1]
            else:
                return 0
        print(dp)
        return dp[length]

sol = Solution()
s = sys.stdin.readline().strip()
n = sol.numDecodings(s)
print(n)
