class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # {2:0}
        for num in range(len(nums)): # 1
            expected_num = target - nums[num] # 9- 7 = 2
            if expected_num in hashMap: 
                return [hashMap[expected_num], num] # [0, 1]
            else:
                hashMap[nums[num]] = num
        
