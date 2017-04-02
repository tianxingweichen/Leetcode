class Solution(object):
    def removeElement(self, nums, val):
        num = nums.count(val)
        for i in range(num):
            nums.remove(val)
        return len(num)
