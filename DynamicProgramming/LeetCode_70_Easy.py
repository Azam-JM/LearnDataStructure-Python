class Solution:
    def climbStairs(self, n: int) -> int:
        prevStep = 1
        nextStep = 1

        for step in range(n-1):
            prevStep, nextStep = nextStep, prevStep + nextStep
            # temp = prevStep + nextStep
            # prevStep = nextStep
            # nextStep= temp
        
        return nextStep
