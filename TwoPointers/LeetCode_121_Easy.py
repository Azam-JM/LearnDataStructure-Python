class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximumProfit = 0

        if len(prices) == 1:
            return 0

        leftPointer = 0
        rightPointer = leftPointer + 1
        while rightPointer < len(prices):
            if prices[leftPointer] <= prices[rightPointer]:
                maximumProfit = max(maximumProfit, prices[rightPointer] - prices[leftPointer])
                rightPointer += 1
            else:
                leftPointer = rightPointer
                rightPointer = leftPointer + 1
        
        return maximumProfit
        
