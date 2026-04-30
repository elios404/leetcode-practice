import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        nums = [(a,b) for a, b in zip(nums1, nums2)]
        nums.sort(key=lambda x:x[1], reverse=True) #O(N log N)

        pq = [] # min-heap?
        ans = 0
        curr_sum = 0
        # O(N * log N)
        for num in nums: #num is tuple
            heapq.heappush(pq, num[0]) #O(log N?)
            curr_sum += num[0]

            if len(pq) < k:
                continue
            elif len(pq) > k:
                sub = heapq.heappop(pq)
                curr_sum -= sub
            
            ans = max(ans,curr_sum * num[1])

        return ans
