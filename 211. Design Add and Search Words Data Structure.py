
# Link - https://leetcode.com/problems/design-add-and-search-words-data-structure/

# Space:
# Time:

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        current = self.root
        
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        
        current.isEnd = True

    def dfs_search(self, word: str, i: int, current: TrieNode) -> bool:
        
        if i == len(word): return current.isEnd # reached the end
        
        if word[i] == ".":
            for child in current.children:
                if self.dfs_search(word, i+1, current.children[child]):
                    return True
        else:
            if word[i] not in current.children:
                return False
            return self.dfs_search(word, i+1, current.children[word[i]])
        
        return False
    
class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.dfs_search(word, 0, self.trie.root)