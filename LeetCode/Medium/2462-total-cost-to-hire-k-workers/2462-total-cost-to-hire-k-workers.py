import heapq

# O(K log N) time Complexity
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left, right = 0, len(costs)-1

        left_pq = []
        right_pq = []

        for _ in range(candidates):
            if left > right:
                break

            heapq.heappush(left_pq, costs[left])
            left += 1

            if left > right:
                break

            heapq.heappush(right_pq, costs[right])
            right -= 1

        
        total_cost = 0
        for _ in range(k):
            # print(left_pq, right_pq)
            left_min = left_pq[0] if left_pq else float('inf')
            right_min = right_pq[0] if right_pq else float('inf')

            if left_min <= right_min: #include same case
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