class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.idx = -1
        self.refs = 0

    def addWord(self, word, i):
        node = self
        node.refs += 1
        for w in word:
            index = ord(w) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
            node.refs += 1
        node.idx = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        res = []

        root = TrieNode()
        for i in range(len(words)):
            root.addWord(words[i], i)
        
        def getIndex(c):
            index = ord(c) - ord('a')
            return index

        def dfs(r, c, node):
            if (r<0 or c<0 or
                r>=ROWS or c>=COLS or
                board[r][c] == '*' or
                not node.children[getIndex(board[r][c])]): return

            ch = board[r][c]
            board[r][c] = '*'
            node = node.children[getIndex(ch)]
            
            if node.idx != -1:
                res.append(words[node.idx])
                node.idx = -1
                node.refs -= 1
                if not node.refs:
                    node.children[getIndex(ch)] = None
                    node = None
                    board[r][c] = ch
                    return
            
            dfs(r+1, c, node)
            dfs(r-1, c, node)
            dfs(r, c+1, node)
            dfs(r, c-1, node)

            board[r][c] = ch
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return res