class Solution(object):
    def removeDuplicates(self, nums):
        l = len(nums)
        d = []
        d.append(nums[0])
        tmp = 1
        for i in range(1,l):
            if nums[i]==nums[i-1]:
                tmp += 1
                if tmp<3:
                    d.append(nums[i])
            else:
                tmp = 1
                d.append(nums[i])
        p = 0
        for number in d:
            nums[p] = number
            p +=1
        return p