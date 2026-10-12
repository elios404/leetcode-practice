class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        idx = {}

        for i, num in enumerate(nums):
            finding = target - num

            if finding in idx:
                return [idx[finding], i]

            idx[num] = i