# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node, tree):
            if node:
                tree.append(node.val)
                if node.left: dfs(node.left, tree)
                else: tree.append(None)
                if node.right: dfs(node.right, tree)
                else: tree.append(None)
        
        tree1 = []
        tree2 = []
        dfs(p, tree1)
        dfs(q, tree2)
        return tree1 == tree2
        

        