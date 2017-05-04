class Solution(object):
    def searchRange(self, nums, target):
        l = len(nums)
        if l == 0 or target<nums[0] or target>nums[l-1]:
            return [-1,-1]
        low = 0
        high = l-1
        while low<=high:
            mid = (low+high)/2
            if target>nums[mid]:
                low = mid+1
            elif target < nums[mid]:
                high = mid-1
            else:
                start = mid
                end = mid
                while start>0 and target==nums[start-1]:
                    start -= 1
                while end<l-1 and target==nums[end+1]:
                    end += 1
                return [start,end]  
        return [-1,-1]