class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # given sum = 0
        givenSum = 0
        for num in range(len(nums)): # (0 - 3)
            givenSum += nums[num] # 

        # Sum of numbers
        actualSum = (len(nums) * (len(nums) +1)) // 2

        return actualSum - givenSum
        
