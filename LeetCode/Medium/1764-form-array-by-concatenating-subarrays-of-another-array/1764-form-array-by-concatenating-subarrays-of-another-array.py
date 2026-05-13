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