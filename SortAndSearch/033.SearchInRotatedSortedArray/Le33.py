class Solution(object):
    def search(self, nums, target):
        l = len(nums)
        low = 0
        high = l -1 
        while low <= high:
            mid = (low+high)/2
            if target == nums[mid]:
                return mid
            if nums[mid] > nums[low]:
                if target >= nums[low] and target <= nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1
            else:
                if target >= nums[low] or target <= nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1
        return -1