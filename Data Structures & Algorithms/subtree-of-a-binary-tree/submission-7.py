# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        left = self.isSubtree(root.left, subRoot) 
        right = self.isSubtree(root.right, subRoot)
        
        return left or right or helper(root, subRoot)
        
        



def helper(root, subRoot):
    if root is None and subRoot is None:
        return True
    
    if root is None:
        return False
    
    if subRoot is None:
        return False
    
    if root.val == subRoot.val:
        return helper(root.left, subRoot.left) and helper(root.right, subRoot.right)
    else:
        return False
    
    