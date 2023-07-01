class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.isEnd = True
        curr.val = 1
        self.size += 1

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

    def put(self, val: str) -> str:
        pass

    def get(self, key: str) -> str:
        pass

    def remove(self, key: str) -> bool:
        pass

    def containsKey(self, key: str) -> bool:
        pass

    def size(self):
        return self.size


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.val = None
