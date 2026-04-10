"""
1. Approach:
    - Scan grid and save the rotten orange's locations by deque and how many fresh oranges exist.
    - Use BFS in grid which moves 4-directionally adjacent.
    - Before BFS, if there are none fresh orange, return 0 mins. And though while loop ended but if there are still fresh oranges, return -1.
2. Time Complexity: O(M * N) - For scanning `grid` take O(M * N) and, in worst case every cell of grid can be putted in deque so while loop also takes O(M * N)
3. Space Complexity: O(M * N) - For visited 2D-array need auxiliary O(M*N) and deque also need maximum O(M*N), and other `di`, `dj` or variable need constant auxiliary space.
"""

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        di = [-1,1,0,0]
        dj = [0,0,-1,1]

        def checkBorder(i,j,m,n):
            return 0<=i and i<m and 0<=j and j<n

        m = len(grid)
        n = len(grid[0])
        rotten = deque()
        fresh_cnt = 0

        #search grid and find rotten orange's location and how many fresh oranges are there
        # O(M * N)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_cnt += 1
                elif grid[i][j] == 2:
                    rotten.append((i,j,0)) #row, col, time

        if fresh_cnt == 0:
            return 0

        #O(V+E) ~= O(M * N)?
        while rotten:
            i, j, mins = rotten.popleft()

            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if not checkBorder(ni,nj,m,n): continue # out of border

                if grid[ni][nj] == 1: #if adjacent is fresh orange
                    fresh_cnt -= 1
                    if fresh_cnt == 0: # if all fresh oranges are rotten
                        return mins+1
                    grid[ni][nj] = 2
                    rotten.append((ni,nj,mins+1))
        
        return -1