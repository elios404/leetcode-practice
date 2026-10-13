"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        new_nodes = {}
        new_nodes[node.val] = Node(val=node.val)
        visited = {node.val}

        def copy(node, new_node):
            if not node.neighbors:
                return
            
            for neighbor in node.neighbors:
                new_neighbor = new_nodes.get(neighbor.val, Node(val=neighbor.val))
                new_nodes[new_neighbor.val] = new_neighbor
                new_node.neighbors.append(new_neighbor)

                if new_neighbor.val not in visited:
                    visited.add(new_neighbor.val)
                    copy(neighbor, new_neighbor)
        
        copy(node, new_nodes[node.val])

        return new_nodes[node.val]