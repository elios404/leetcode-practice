class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])

        ret = [intervals[0]]
        for i in range(1, len(intervals)):
            end, start = ret[-1][1], intervals[i][0]
            if end >= start:
                before = ret.pop()
                ret.append([min(before + intervals[i]), max(before + intervals[i])])
            else:
                ret.append(intervals[i])
        
        return ret