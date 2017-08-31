#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def minimumTotal(self, triangle):
        length = len(triangle[-1])
        raw = len(triangle)
        maxs = [0 for i in range(length)]
        for i in range(length):
            maxs[i] = triangle[-1][i]
        for i in range(raw-2,-1,-1):
            for j in range(len(triangle[i])):
                maxs[j] = max(maxs[j],maxs[j+1])+triangle[i][j]
        return maxs[0]
        
