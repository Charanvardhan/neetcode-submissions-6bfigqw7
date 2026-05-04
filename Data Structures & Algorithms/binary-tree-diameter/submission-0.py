# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]
        helper(root, result)
        return result[0]
        
def helper(root, sol):
    if root is None:
        return 0
    
    ld = helper(root.left, sol)
    rd = helper(root.right, sol)
    sol[0] = max(sol[0], ld + rd)
    return max(ld, rd) + 1
    