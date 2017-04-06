class Solution(object):
    def twoSum(self, nums, target):
        l = len(nums)
        if l == 0:
            return []
        for i in range(l-1):
            for j in range(i+1,l):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []     
