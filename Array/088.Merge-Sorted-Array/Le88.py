class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1.append(nums2[i])
        while nums1.count(0) > 0:
            nums1.remove(0)
        nums1.sort()
        return nums1

