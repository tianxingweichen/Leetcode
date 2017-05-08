class Solution(object):
    def trap(self, height):
        l = len(height)
        if l < 2:
            return 0
        left = 0
        right = l - 1
        sums = 0
        while left<right:
            if height[left]<=height[right]:
                temp = height[left]
                left = left + 1
                while temp > height[left]:
                    sums = sums + temp - height[left]
                    left = left + 1
            else:
                temp = height[right]
                right = right - 1
                while temp > height[right]:
                    sums = sums + temp - height[right]
                    right = right - 1
        return sums