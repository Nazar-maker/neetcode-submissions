# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def dfs(self, node, tree):
        if node == None: return tree.append('null')
        tree.append(str(node.val))
        self.dfs(node.left, tree)
        self.dfs(node.right, tree)
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        tree = []
        self.dfs(root, tree)
        
        return ",".join(tree)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i = 0
        values = data.split(',')
        def dfs_rev():
            if values[self.i] == 'null':
                self.i += 1
                return None
            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = dfs_rev()
            node.right = dfs_rev()
            return node
        
        return dfs_rev()