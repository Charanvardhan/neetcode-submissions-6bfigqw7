# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        op = -1001
        def dfs(root):
            nonlocal op
            if not root:
                return 0  # cleaner than -1001; explained below
            
            left = max(dfs(root.left), 0)   # if negative, just don't use that side
            right = max(dfs(root.right), 0)
            
            # Path THROUGH this node (can use both sides) — update global
            op = max(op, root.val + left + right)
            
            # Path EXTENDING UP from this node (only one side)
            return root.val + max(left, right)
        dfs(root)
        return op