from collections import deque, defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = defaultdict(list)

        # Pythonic: Tuple unpacking for cleaner assignments
        for (u, v), cost in zip(equations, values):
            edges[u].append((v, cost))
            edges[v].append((u, 1 / cost))

        ret = []
        for start, end in queries:
            # 1. EARLY REJECTION: If either node doesn't exist, it's strictly -1.0
            # Using 'in' does NOT trigger defaultdict's automatic key creation.
            if start not in edges or end not in edges:
                ret.append(-1.0)
                continue

            # 2. IDENTITY CASE: If a node divides by itself
            if start == end:
                ret.append(1.0)
                continue

            # 3. BFS SEARCH
            queue = deque([(start, 1.0)])
            visited = {start} # Pythonic: Set initialization
            found = False
            
            while queue and not found:
                cur_node, cur_value = queue.popleft()
                
                for next_node, weight in edges[cur_node]:
                    if next_node not in visited:
                        if next_node == end:
                            ret.append(cur_value * weight)
                            found = True
                            break
                        
                        visited.add(next_node)
                        queue.append((next_node, cur_value * weight))
            
            if not found:
                ret.append(-1.0)

        return ret