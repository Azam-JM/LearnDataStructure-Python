class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for num in range(len(nums)):
            if nums[num] in hashSet:
                return True
            else:
                hashSet.add(nums[num])
        return False
        