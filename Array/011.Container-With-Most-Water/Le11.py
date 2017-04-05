class Solution(object):
    def maxArea(self, height):
        l = len(height)
        left = 0 
        right = l-1
        maxV =0
        while left < right:
            maxV = max(maxV, min(height[left], height[right])*(right-left))
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return maxV
            
 
