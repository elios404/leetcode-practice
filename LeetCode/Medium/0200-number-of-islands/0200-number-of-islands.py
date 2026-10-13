from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(i, j, grid):
            queue = deque([(i, j)])
            grid[i][j] = "0" # visited

            di = [-1, 0, 1, 0]
            dj = [0, 1, 0, -1]

            while queue:
                ci, cj = queue.popleft()

                for d in range(4):
                    ni, nj = ci + di[d], cj + dj[d]

                    if ni < 0 or len(grid) <= ni or nj < 0 or len(grid[0]) <= nj:
                        continue
                    if grid[ni][nj] == "0": # water or visited
                        continue
                    
                    queue.append((ni, nj))
                    grid[ni][nj] = "0"
        
        number_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    number_of_islands += 1
                    bfs(i, j, grid)
        
        return number_of_islands
