class Solution(object):
    def firstMissingPositive(self, nums):
        l = len(nums)
        if l == 0:
            return 1
        maxn = max(nums)
        if maxn < 1:
            return 1
        bucket = [0 for i in range(maxn+2)]
        for i in range(l):
            if nums[i] > 0:
                bucket[nums[i]] = 1
        bucket[0] = 1
        return bucket.index(0)


