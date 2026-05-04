# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return helper(root, 0)
        
def helper(root, height):
    if root is None:
        return height
    
    return max(helper(root.left, height + 1), helper(root.right, height + 1))