# Topic: Longest Palindromic Substring
import numpy as np

class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        table = np.zeros(n,n)
        for i in range(n):
            table[i][i] = 1
        lens = 0
        begin = 0
        end = 0
        for i in range(1,n):
            if s[i-1] == s[i]:
                table[i-1][i] = 2 
                lens = 2
                begin = i-1
                end = i
        for l in range(3, n):
            for i in range(n-l+1):
                j = i + l - 1
                if table[i+1, j-1] != 0 && s[i] == s[j]:
                    table[i+1,j-1] = j-i+1
                    if table[i+1,j-1] > len:
                        lens = j-i+1
                        begin = i
                        end = j
        return s[begin,end+1]