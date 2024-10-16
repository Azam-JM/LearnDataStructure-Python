# Given an array of integers, nums, and an integer value, target, determine if there are any three integers in nums whose sum is equal to the target, that is, nums[i] + nums[j] + nums[k] == target. Return TRUE if three such integers exist in the array. Otherwise, return FALSE.

def find_sum_of_three(nums, target):
   # [-1,2,1,-4,5,-3] 
   # -8
   nums.sort()
   for a in range(0, len(nums)-2):
      left = a + 1
      right = len(nums)-1
      while left < right:
         value = nums[a] + nums[left] + nums[right]
         if value == target:
            return True
         elif value > target:
            right = right - 1
         else:
            left = left + 1
   return False
