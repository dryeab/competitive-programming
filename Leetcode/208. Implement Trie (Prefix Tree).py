
# Link - https://leetcode.com/problems/implement-trie-prefix-tree/

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

    def search(self, word: str, isPrefix=False) -> bool:
        
        current = self.root
        
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        
        return isPrefix or current.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, True)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)