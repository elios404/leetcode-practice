class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        range_tuples = []
        start = end = nums[0]

        # O(N)
        for i in range(1, len(nums)):
            if nums[i] - 1 == end:
                end = nums[i]
                continue
            else:
                range_tuples.append((start, end))
                start = end = nums[i]
        range_tuples.append((start,end))

        ret = []
        # O(N)
        for s, e in range_tuples:
            r = f"{s}->{e}" if s != e else f"{s}"
            ret.append(r)
        
        return ret