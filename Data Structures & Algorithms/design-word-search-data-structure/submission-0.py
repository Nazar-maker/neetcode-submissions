class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(root, i):
            node = root

            for j in range(i, len(word)):
                w = word[j]

                if w == '.':
                    for child in node.children.values():
                        if dfs(child, j+1):
                            return True
                    return False
                else:
                    if w in node.children:
                        node = node.children[w]
                    else:
                        return False
            
            return node.endOfWord

        
        return dfs(self.root, 0)
