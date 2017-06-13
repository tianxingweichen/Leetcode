class Solution(object):
    def jump(self, nums):
        length = len(nums)
        if length == 1:
            return 0
        s = 0
        t = 0
        reach = s+nums[s]
        while reach<length-1:
            reach = s+nums[s]
            i = 0 
            while i<=nums[s] and i<length-1:
                if s+i+nums[s+i]>=reach:
                    reach = s +i+nums[s+i]
                    p = s + i
                i = i + 1
            s = p
            t = t + 1
        t = t+1
        return t
