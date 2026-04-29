MAX_N = int(5e4)
MAX_PRICE = int(5e4)
MAX_FEE = int(5e4)

INF = MAX_N * MAX_PRICE * MAX_FEE


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        memo = [{True: 0, False: 0} for _ in range(N+1)]

        memo[-1][True] = -INF
        memo[-1][False] = 0
        for i in range(N):
            memo[i][True] = max(memo[i-1][True], memo[i-1][False]-prices[i]-fee)
            memo[i][False] = max(memo[i-1][False], memo[i-1][True]+prices[i])
        
        return max(memo[N-1][True], memo[N-1][False])
