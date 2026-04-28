class MyHashSet:

    def __init__(self):
        self.head = []
        self.tail = None

    def add(self, key: int) -> None:
        if not self.contains(key): self.head.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key): self.head.pop(self.head.index(key))

    def contains(self, key: int) -> bool:
        for i in self.head:
            if i == key: return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(ke0y)
# param_3 = obj.contains(key)