class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        overlapping_area = []
        points.sort(reverse=True)

        added = False
        for point in points:
            
            for area in overlapping_area:
                if point[0] > area[1] or point[1] < area[0]: # not in area
                    continue
                #if in area
                area[0] = max(area[0], point[0])
                area[1] = min(area[1], point[1])
                added = True
                break
            
            # if not in overlapping area
            if not added:
                overlapping_area.append(point)
            
            added = False
            
            # print(overlapping_area)
        
        return len(overlapping_area)