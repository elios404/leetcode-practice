class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = []
        ret = []
        
        def permutation():
            if len(visited) == len(nums):
                ret.append([nums[i] for i in visited])
                return
            
            for idx in range(len(nums)):
                if idx not in visited:
                    visited.append(idx)
                    permutation()
                    visited.pop()
        
        permutation()

        return ret