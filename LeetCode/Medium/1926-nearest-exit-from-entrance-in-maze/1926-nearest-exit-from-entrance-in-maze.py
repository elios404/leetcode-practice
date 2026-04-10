from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        di = [-1,1,0,0]
        dj = [0,0,-1,1]

        m = len(maze)
        n = len(maze[0])

        def checkBorder(i, j, m, n) -> bool:
            return 0<=i and i<m and 0<=j and j<n
        
        queue = deque()
        visited = [[False]*n for _ in range(m)]
        queue.append([entrance[0], entrance[1], 0]) # i,j,step
        visited[entrance[0]][entrance[1]] = True

        while queue:
            i,j,step = queue.popleft()

            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if not checkBorder(ni,nj,m,n): #escape
                    if step == 0:
                        continue
                    else:
                        return step
                
                if maze[ni][nj] == "." and not visited[ni][nj]: #if not wall
                    visited[ni][nj] = True
                    queue.append([ni,nj,step+1])

        return -1