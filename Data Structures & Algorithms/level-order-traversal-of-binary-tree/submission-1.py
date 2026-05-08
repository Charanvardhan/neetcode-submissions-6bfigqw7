from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        q.append(root)
        q.append('checker')
        op = []
        return helper(q, op)

def helper(q, op):
    temp = []
    while q:
        node = q.popleft()
        if node.left: q.append(node.left)
        if node.right: q.append(node.right) 
        temp.append(node.val)
        
        if q[0] == "checker":
            op.append(temp)
            temp = []
            q.popleft()
            if q: q.append('checker') 

    return op