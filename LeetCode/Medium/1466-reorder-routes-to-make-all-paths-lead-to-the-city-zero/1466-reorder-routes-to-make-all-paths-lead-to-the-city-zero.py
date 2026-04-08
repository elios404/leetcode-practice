from collections import deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = [False] * n
        graph = [[]*n for _ in range(n)]
        rGraph = [[]*n for _ in range(n)]

        for edge in connections:
            start, end = edge[0], edge[1]
            graph[start].append(end)
            rGraph[end].append(start)
        
        q = deque()
        q.append(0)
        visited[0] = True

        ans = 0
        while q:
            cur = q.popleft()

            for i in graph[cur]:
                if not visited[i]:
                    ans += 1
                    q.append(i)
                    visited[i] = True

            for i in rGraph[cur]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
        
        return ans
            