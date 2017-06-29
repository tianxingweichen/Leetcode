class Solution(object):
    def maxSubArray(self, nums):
        l = len(nums)
        maxtmp = 0
        maxs = nums[0]
        if l == 1:
            return nums[0]
        for i in range(l):
            if maxtmp+nums[i] > nums[i]:
                maxtmp = maxtmp+nums[i] 
            else:
                maxtmp = nums[i]
            if maxtmp > maxs:
                maxs = maxtmp
        return maxs