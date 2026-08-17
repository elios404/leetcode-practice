class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        visited = set()

        def backtrack(path: List[int]):
            if len(path) == len(nums):
                ret.append(path[:])  # path.copy()
                return

            for num in nums:
                if num not in visited:
                    visited.add(num)
                    backtrack(path + [num])  # 또는 append/pop 사용
                    visited.remove(num)

        backtrack([])
        return ret