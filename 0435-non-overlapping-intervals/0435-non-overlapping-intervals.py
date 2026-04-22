class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1]) # O(N log N)?

        cnt = 0
        prev_back = float('-inf')
        # O(N)
        for start, end in intervals:
            if start < prev_back:
                cnt += 1
            else:
                prev_back = end
                
        return cnt