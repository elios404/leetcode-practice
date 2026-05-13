class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        steps = 0
        cur_idx = reachable_range = 0

        while reachable_range < n-1:
            # print(steps, cur_idx, reachable_range)
            next_reachable_range = 0
            for i in range(cur_idx, reachable_range+1):
                next_reachable_range = max(next_reachable_range, i+nums[i])
            
            steps += 1
            cur_idx = reachable_range+1
            reachable_range = next_reachable_range
            

        return steps