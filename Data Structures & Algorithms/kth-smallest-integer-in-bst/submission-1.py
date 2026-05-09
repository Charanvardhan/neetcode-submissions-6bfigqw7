# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return find(root, [k])

def find(node, k):
    if not node:
        return None
    
    # 1. Search Left
    left = find(node.left, k)
    if left is not None:
        return left
    
    # 2. Visit Node
    k[0] -= 1
    if k[0] == 0:
        return node.val
    
    # 3. Search Right
    return find(node.right, k)