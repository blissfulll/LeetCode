class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = [cost[0], cost[1]]
      
        for i in range(len(cost)):
            if i > 1:
                cost[i] = min(cost[i-1], cost[i-2]) + cost[i]

        return min(cost[-1], cost[-2])
