#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def subsets(self, nums):
        length = len(nums)
        N = [[]]
        for i in range(length):
            d = N[:]
            for j in range(len(d)):
                d[j].append(nums[i])
            N = N + d
        return N
