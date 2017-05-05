class Solution(object):
    def searchInsert(self, nums, target):
        l = len(nums)
        if nums[0]>target:
            return 0
        low = 0
        high = l-1
        while low<=high:
            mid = (low+high)/2
            if target==nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        if target > nums[mid]:
            return mid + 1
        else:
            return mid