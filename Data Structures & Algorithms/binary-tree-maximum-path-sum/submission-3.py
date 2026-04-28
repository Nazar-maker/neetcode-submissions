# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = [root.val]

        def dfs(node):
            if not node:
                return 0

            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            maxSum[0] = max(maxSum[0], node.val+leftMax+rightMax, node.val)

            return max(node.val+max(leftMax, rightMax), node.val)
        
        # maxSum[0] = max(maxSum[0], dfs(root))
        out = dfs(root)
        print(maxSum[0])
        print(out)
        maxSum[0] = max(maxSum[0], out)

        return maxSum[0]

"""
                -1
            -2       10 
        -6       -3      -6

"""


