import functools


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        @functools.lru_cache(maxsize=None)
        def solve(i: int = 0, has_stock: bool = False) -> int:
            if i == len(prices):
                return 0
            if has_stock:
                return max(
                    solve(i+1, False) + prices[i], # 판매
                    solve(i+1, True),  # 존버
                )
            else:
                return max(
                    solve(i+1, True) - prices[i] - fee,  # 구매
                    solve(i+1, False),  # 존버
                )

        for i in reversed(range(len(prices))):
            solve(i, False)
            solve(i, True)

        return solve()