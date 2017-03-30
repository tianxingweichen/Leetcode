import numpy as np

class Solution(object):
    def maxSubArray(self, nums):
        l = len(nums)
        maxtmp = 0
        maxs = 0
        for i in range(l):
            if maxtmp+nums[i] > nums[i]:
                maxtmp = maxtmp+num[i] 
            else:
                maxtmp = num[i]
            if maxtmp > maxs:
                maxs = maxtmp
                