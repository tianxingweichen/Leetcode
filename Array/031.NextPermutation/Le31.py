class Solution(object):
    def nextPermutation(self, nums):
        l = len(nums)
        temp = [0 for i in range(l)]
        temp[-1] = 1
        for i in range(l-1)[::-1]:
            if nums[i] >= nums[i+1]:
                temp[i] = 1
            else:
                break
        if temp.count(0) == 0:
            nums.sort()
        else:
            t = temp.index(1)
            print(t)
            subnums = nums[t:] 
            print(subnums)
            for i in range(l)[::-1]:
                if nums[i] > nums[t-1]:
                    d = nums[t-1]
                    nums[t-1] = nums[i]
                    nums[i] = d
                    subnums[i-t] = d
                    break
            subnums.sort()
            for i in range(t,l):
                nums[i] = subnums[i-t]

        
        