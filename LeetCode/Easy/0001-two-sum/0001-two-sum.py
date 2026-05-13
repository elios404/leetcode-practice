class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index = [(i, num) for i, num in enumerate(nums)]
        nums_index.sort(key=lambda x:x[1])
        left, right = 0, len(nums)-1

        while left < right:
            s = nums_index[left][1] + nums_index[right][1]
            if s == target:
                return [nums_index[left][0], nums_index[right][0]]
            elif s < target:
                left += 1
            else:
                right -= 1