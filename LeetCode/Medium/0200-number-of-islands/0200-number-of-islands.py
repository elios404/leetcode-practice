from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid) # row
        m = len(grid[0]) # col
        island_count = 0

        visited = [[False] * m for _ in range(n)]
        def bfs(grid, visited, i, j, n, m):
            di = [-1,0,1,0]
            dj = [0,1,0,-1]

            q = deque()
            q.append((i, j))

            while q:
                curr = q.popleft() # tuple (i, j)
                for d in range(4):
                    ni = curr[0] + di[d]
                    nj = curr[1] + dj[d]

                    if ni < 0 or n <= ni or nj < 0 or m <= nj: # out of range
                        continue
                    if visited[ni][nj] or grid[ni][nj] == "0": # already visited or if it's water
                        continue
                    
                    visited[ni][nj] = True # check visited
                    q.append((ni,nj))

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == "1":
                    bfs(grid, visited, i, j, n, m)
                    island_count += 1
        
        return island_count