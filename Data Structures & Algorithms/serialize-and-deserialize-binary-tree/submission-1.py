# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return 'null'
        stack = [root]
        out = []
        while stack:
            node = stack.pop()
            if not node: 
                out.append('null')
            else:
                out.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)
        print(' '.join(out))
        return ' '.join(out)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(' ')
        if nodes[0] == 'null': return None
        root = TreeNode(int(nodes[0]))
        stack = [root]
        index = 1
        while index < len(nodes):
            parent = stack[-1]
            left_val = nodes[index]
            index += 1
            if left_val != 'null':
                parent.left = TreeNode(int(left_val))
                stack.append(parent.left)
                continue

            while stack and nodes[index] == 'null':
                stack.pop()
                index += 1
            
            if stack and index < len(nodes):
                parent = stack.pop()
                right_val = nodes[index]
                index += 1
                if right_val != 'null':
                    parent.right = TreeNode(int(right_val))
                    stack.append(parent.right)
        return root
