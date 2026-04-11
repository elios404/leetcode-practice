import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, -num) #heapq only supports min-heap
        
        for _ in range(k-1):
            heapq.heappop(heap)

        return -heappop(heap)