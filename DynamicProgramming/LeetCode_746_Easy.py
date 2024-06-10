class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stepOne = 0
        stepTwo = cost[-1]

        for step in range(len(cost)-2, -1, -1):
            cost[step] = min(cost[step] + stepOne, cost[step] + stepTwo)
            stepOne = stepTwo
            stepTwo = cost[step]
        
        return cost[0] if cost[0] < cost[1] else cost[1]

        
