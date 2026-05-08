from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        dq = deque()
        dq.append(root)
        op = [root.val]

        while dq:
            level_size = len(dq)
            level = []

            for _ in range(level_size):
                node = dq.popleft()
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            
            if dq:
                op.append(dq[-1].val)
        
        return op

        