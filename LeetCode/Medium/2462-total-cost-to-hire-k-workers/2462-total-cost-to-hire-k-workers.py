import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # Edge Case: If the candidate pools overlap or cover the whole array,
        # all workers are candidates. Just sort and take the cheapest k.
        if 2 * candidates >= len(costs):
            return sum(sorted(costs)[:k])

        # Pythonic: Slice the arrays and use O(N) heapify instead of pushing in a loop!
        left_pq = costs[:candidates]
        right_pq = costs[-candidates:]
        heapq.heapify(left_pq)
        heapq.heapify(right_pq)

        # Set pointers to the remaining unvisited elements in the middle
        left = candidates
        right = len(costs) - candidates - 1
        total_cost = 0

        # Your beautiful greedy extraction logic remains exactly the same
        for _ in range(k):
            left_min = left_pq[0] if left_pq else float('inf')
            right_min = right_pq[0] if right_pq else float('inf')

            if left_min <= right_min:
                total_cost += heapq.heappop(left_pq)
                if left <= right:
                    heapq.heappush(left_pq, costs[left])
                    left += 1
            else:
                total_cost += heapq.heappop(right_pq)
                if left <= right:
                    heapq.heappush(right_pq, costs[right])
                    right -= 1
        
        return total_cost