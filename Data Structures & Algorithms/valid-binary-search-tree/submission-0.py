# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return dfs(root, 1001, -1001)

def dfs(root, leftMax, rightMin):
    if not root:
        return True
    
    if root.val <= rightMin:
        return False
    
    if root.val >= leftMax:
        return False
    
    return dfs(root.left, root.val, rightMin) and dfs(root.right, leftMax, root.val)
