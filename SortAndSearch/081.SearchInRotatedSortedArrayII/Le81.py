class Solution(object):
    def search(self, nums, target):
        l = len(nums)
        low = 0
        high = l - 1
        while low<=high:
            mid = (low+high)/2
            if target == nums[mid]:
                while mid>l-1 and target == nums[mid]:
                    mid -= 1
                return True
            if nums[mid] >= nums[low]:
                if target >= nums[low] and target <= nums[mid]:
                    high -= 1
                else:
                    low += 1
            else:
                if target >= nums[low] or target <= nums[mid]:
                    high -= 1
                else:
                    low += 1
        return False