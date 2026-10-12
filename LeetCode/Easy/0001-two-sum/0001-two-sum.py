from collections import defaultdict

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        idx = defaultdict(list)

        for i, num in enumerate(nums):
            finding = target - num
            if len(idx[finding]) != 0:
                return idx[finding] + [i]
            idx[num].append(i)