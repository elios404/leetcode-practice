class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x : x[1])

        right = float('-inf')
        cnt = 0
        for p_left, p_right in points:
            if right < p_left: #if not in area
                right = p_right
                cnt += 1

        return cnt