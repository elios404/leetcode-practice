import bisect

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # bisect_left finds the exact insertion point to maintain sorted order
        return bisect.bisect_left(nums, target)