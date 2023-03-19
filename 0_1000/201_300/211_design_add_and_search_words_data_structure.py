from typing import Dict


class Node:
    def __init__(self):
        self.children: Dict[str, Node] = {}
        self.is_end: bool = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for l in word:
            if node.children.get(l) is None:
                node.children[l] = Node()
            node = node.children.get(l)
        node.is_end = True

    def search(self, word: str) -> bool:
        def helper(node: Node, index: int = 0) -> bool:
            for i in range(index, len(word)):
                if node.children.get(word[i]) is None:
                    if word[i] == "." and len(node.children.keys()) != 0:
                        for v in node.children.values():
                            if helper(v, i + 1):
                                return True
                    return False
                else:
                    node = node.children.get(word[i])
            return node.is_end

        return helper(self.root)


# wordDictionary = WordDictionary()
# wordDictionary.addWord("bad")
# wordDictionary.addWord("dad")
# wordDictionary.addWord("mad")
# wordDictionary.addWord("baq")
# print(wordDictionary.search("pad"))
# print(wordDictionary.search("bad"))
# print(wordDictionary.search(".ad"))
# print(wordDictionary.search("b.."))
# print(wordDictionary.search("b..w"))

wordDictionary = WordDictionary()
wordDictionary.addWord("a")
wordDictionary.addWord("a")
# print(wordDictionary.search("."))
# print(wordDictionary.search("a"))
# print(wordDictionary.search("aa"))
# print(wordDictionary.search("a"))
print(wordDictionary.search(".a"))
print(wordDictionary.search("a."))
