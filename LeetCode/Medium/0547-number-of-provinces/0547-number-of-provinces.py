"""
1. Approach:
    - At first, I wanted to use union-find algorithm but failed to solve with that.
    - So changed the way of solving, search all connected nodes and track that with visited boolean list
    - Count how many new start points appear whlie linear search of the `isConnected`
2. Time Complexity : O(N^2) - Check exactly once of N*N grid
3. Space Comeplextiy : O(N) - boolean list for tracking visit take O(N) and deque also need O(N) maximum.
"""
from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        q = deque()
        visited = [False] * n
        
        answer = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                q.append(i)

                answer += 1
                while q:
                    cur_num = q.popleft()
                    for j in range(n):
                        if isConnected[cur_num][j] == 1 and not visited[j]:
                            visited[j] = True
                            q.append(j) 

        return answer