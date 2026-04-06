from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        q = deque()

        q.append(0)
        visited[0] = True

        cnt = 1
        while q:
            cur = q.popleft()
            keys = rooms[cur]

            for key in keys:
                if not visited[key]:
                    visited[key] = True
                    q.append(key)
                    cnt += 1
        
        return cnt == n