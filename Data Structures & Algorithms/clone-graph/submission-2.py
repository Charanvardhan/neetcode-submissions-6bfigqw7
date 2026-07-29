"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        visited = dict()
        return helper(node, visited)
        

def helper(node, visited):
    if node in visited:
        return visited[node]
    op = Node(node.val)
    visited[node] = op
    for i in node.neighbors:
        op.neighbors.append(helper(i, visited))
    return op
        