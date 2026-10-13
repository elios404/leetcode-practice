import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)

        for i in range(k):
            ret = -heapq.heappop(nums)
        
        return ret