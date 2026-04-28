# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([[root, 0]])

        while queue:
            node, index = queue.popleft()
            if index >= len(res):
                res.append([])
            res[index].append(node.val)
            if node.left:
                queue.append([node.left, index + 1])

            if node.right:
                queue.append([node.right, index + 1])

        return res