class Solution(object):
    def threeSumClosest(self, nums, target):
        l = len(nums)
        lists = []
        nums.sort()
        mins = float('inf')
        for i in range(l-2):
            j = i + 1
            k = l-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s <target:
                    j = j + 1
                    lists.append(s)
                    if abs(s-target) < abs(mins):
                        mins = s - target
                elif s>target:
                    k = k - 1
                    lists.append(s)
                    if abs(s-target) < abs(mins):
                        mins = s - target
                else:
                    return target
                print(mins)
        return mins + target

