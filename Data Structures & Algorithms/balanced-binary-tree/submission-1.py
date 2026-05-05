# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return helper(root)[1]
        
def helper(root):
    if root is None:
        return [0, True]
    
    left = helper(root.left)
    right = helper(root.right)
    valid = False if abs(left[0] - right[0]) > 1 else True
    return [max(left[0], right[0]) + 1, valid and left[1] and right[1]]