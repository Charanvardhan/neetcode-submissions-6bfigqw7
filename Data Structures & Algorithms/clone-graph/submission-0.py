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
    op = Node(node.val)
    visited[node] = op
    for i in node.neighbors:
        if visited.get(i, False):
            op.neighbors.append(visited[i])
        else:
            op.neighbors.append(helper(i, visited))
    
    return op
        