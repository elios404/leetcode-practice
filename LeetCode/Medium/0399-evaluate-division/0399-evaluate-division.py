from collections import deque, defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = defaultdict(list)

        for edge, cost in zip(equations, values):
            edges[edge[0]].append((edge[1], cost))
            edges[edge[1]].append((edge[0], 1/cost))

        ret = []
        for query in queries:
            start, end = query[0], query[1]

            if start == end and len(edges[start]) != 0: # hmm.. but isn't it weird that at the bottom, not exist key added so need to check the length.
                ret.append(1.0)
                continue

            queue = deque()
            visited = set()

            queue.append((start,1))
            visited.add(start)
            found = False
            while queue and not found:
                cur_node, cur_value = queue.popleft()
                for next_node in edges[cur_node]: # at here, though cur_node does actually not exist in equations but still new key `cur_node` and empty list added..
                    if next_node[0] not in visited:
                        if next_node[0] == end:
                            ret.append(cur_value * next_node[1])
                            found = True
                            break
                
                        visited.add(next_node[0])
                        queue.append((next_node[0], cur_value * next_node[1]))
            
            if not found:
                ret.append(-1.0)

        return ret