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
                return -1001
            
            left = dfs(root.left)
            right = dfs(root.right)

            if left < 0 and right < 0:
                curMax = root.val
            elif left < 0:
                curMax = root.val + right
            elif right < 0:
                curMax = root.val + left
            else:
                curMax = root.val + left + right

            op = max(op, curMax)

            # if curMax < 0:
            #     return -1
            # else:
            return root.val + max(left, right, 0)

        dfs(root)
        return op
        