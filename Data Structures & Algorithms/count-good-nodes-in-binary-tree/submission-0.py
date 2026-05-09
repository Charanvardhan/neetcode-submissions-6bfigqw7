# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        base = root.val
        return dfs(root, base)

def dfs(root, base):
    if not root:
        return 0

    isgood = 0
    
    if root.val >= base:
        isgood = 1
        base = root.val
    
    return dfs(root.left, base) + dfs(root.right, base) + isgood

        