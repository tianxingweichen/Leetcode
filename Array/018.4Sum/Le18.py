class Solution(object):
  def fourSum(self, nums, target):
    l = len(nums)
    ans = []
    nums.sort()
    i = 0
    while i < l-3:
      z = i + 1
      while z<l-2:
        j = z + 1
        k = l - 1
        print(nums[i],nums[z])
        while j < k:
          s = nums[i] + nums[z] + nums[j] + nums[k]
          if s < target:
            j = j + 1
          elif s > target:
            k = k - 1
          else:
            ans.append([nums[i], nums[z], nums[j], nums[k]])
            j = j + 1
            k = k - 1
            while j < k:
              if nums[j] != nums[j-1]:
                break
              if nums[k] != nums[k+1]:
                break
              j = j + 1
              k = k - 1
        z = z + 1
        while z < l-2:
          if  nums[z] != nums[z-1]:
            break
          z = z + 1
      i = i + 1
      while i < l-3:
        if nums[i] != nums[i-1]:
          break
        i = i + 1
    return ans
        
        
