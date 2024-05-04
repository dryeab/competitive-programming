class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]

        cur.isEnd = True

    def search(self, word: str, isPrefix=False) -> bool:

        cur = self.root

        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]

        return isPrefix or cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, True)
