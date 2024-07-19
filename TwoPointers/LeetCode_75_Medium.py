# https://leetcode.com/problems/sort-colors/description/
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        current = 0
        end = len(nums) - 1

        while current <= end:
            if nums[current] == 0:
                # swap with start and increment
                nums[start], nums[current] = nums[current], nums[start]
                start += 1
                current += 1
            
            elif nums[current] == 1:
                current += 1
            
            else:
                nums[current], nums[end] = nums[end], nums[current]
                end -= 1
            

                
        
