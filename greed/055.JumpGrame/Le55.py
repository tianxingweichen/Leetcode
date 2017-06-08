class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index = 0
        reach = 0
        length = len(nums)
        for i in range(length):
            if reach < i:
                return False
            reach = max(reach,nums[i]+i)
        return True