class Solution(object):
    def sortColors(self, nums):
        l = len(nums)
        tmp = [0 for i in range(3)]
        for i in range(l):
            tmp[nums[i]] += 1
        p = 0
        for i in range(3):
            d = tmp[i]
            for j in range(d):
               nums[p] = i
               p = p + 1