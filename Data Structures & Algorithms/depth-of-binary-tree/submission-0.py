# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, depth):
            if not root:
                return depth

            depth += 1

            depthLeft = dfs(root.left, depth)
            depthRight = dfs(root.right, depth)

            depth = max(depthLeft, depthRight)
            return depth

        return dfs(root, 0)
