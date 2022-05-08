
# Link - https://leetcode.com/problems/short-encoding-of-words/

# Space:
# Time:

class TrieNode:
    def __init__(self):
        self.children = {}
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        current = self.root
        
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        trie = Trie()
        for word in words:
            trie.insert(word[::-1])
        
        def dfs(root, count):
            
            if not root.children: return count + 1

            return sum(dfs(root.children[child], count+1) for child in root.children)
        
        return dfs(trie.root, 0)