class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1], x[0])) # O(N log N)?

        cnt, prev_front, prev_back = 0,-50000,-50000
        # O(N)
        for interval in intervals:
            curr_front, curr_back = interval[0], interval[1]
            if curr_front < prev_back: #overlap
                cnt += 1
            else:
                prev_front, prev_back = curr_front, curr_back
        
        return cnt