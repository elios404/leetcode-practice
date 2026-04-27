class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]

        # O(N)
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-2], dp[i-1])

        return min(dp[-1], dp[-2])
