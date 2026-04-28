class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w in node.children: 
                node = node.children[w]
            else: break
        return node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for pre in prefix:
            if pre in node.children:
                node = node.children[pre]
            else:
                return False
        return True
        