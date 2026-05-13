"""
Constraints:

groups.length == n
1 <= n <= 10^3
1 <= groups[i].length, sum(groups[i].length) <= 10^3
1 <= nums.length <= 10^3
-10^7 <= groups[i][j], nums[k] <= 10^7

1. Approach
    - Using two pointer method, when num in nums are same in current group's k'th element. Then widen the range.
    - If it's not same, then increase start point index and set `move` back to 0
    - if `move` is same with current group's length, then this subarray is equal with current group, so move to next group
2. Time Complexity : O(N * M) - N is the length of `nums` and M is maximum length of a group in groups.
3. Space Complexity : O(1) - Constant space for `gIdx`, `start`, `move` are needed.
"""
class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        gIdx = 0
        start = move = 0

        while start + move < len(nums):
            # check every group appears
            if gIdx == len(groups):
                return True

            # check current num is same with group's element
            if nums[start+move] == groups[gIdx][move]:
                move += 1
            else:
                start += 1
                move = 0
            
            #check whether one group finished
            if move == len(groups[gIdx]):
                start = start + move
                move = 0
                gIdx += 1
        
        return gIdx == len(groups)