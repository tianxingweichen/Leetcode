#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def minDistance(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        D = [[0 for i in range(len2)] for j in range(len1)]
        for i in range(1,len1):
            for j in range(1,len2):
                D[i][j] = min(D[i-1][j]+1, D[i][j-1]+1, D[i-1][j-1]+1)
        print(D[len1][len2])

