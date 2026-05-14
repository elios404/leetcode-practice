class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        range_strings = []
        s = e = nums[0]

        # O(N)
        for i in range(1, len(nums)):
            if nums[i] - 1 == e:
                e = nums[i]
                continue
            else:
                range_strings.append(f"{s}->{e}" if s != e else f"{s}")
                s = e = nums[i]
        range_strings.append(f"{s}->{e}" if s != e else f"{s}")
        
        return range_strings