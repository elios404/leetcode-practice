class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i, num in enumerate(nums):
            needed = target - num
            if needed in s:
                return [s[needed], i]
            s[num] = i
            