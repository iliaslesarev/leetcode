from typing import Dict


class Trie:
    def __init__(self, val: str = ""):
        self.val = val
        self.children: Dict[str, Trie] = {}
        self.is_end: bool = False

    def insert(self, word: str) -> None:
        root = self
        for l in word:
            if root.children.get(l) is None:
                root.children[l] = Trie(l)
            root = root.children[l]
        root.is_end = True

    def search_prefix(self, word: str):
        root = self
        for l in word:
            if root.children.get(l) is None:
                return None
            root = root.children[l]
        return root

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self.search_prefix(prefix) is not None

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
