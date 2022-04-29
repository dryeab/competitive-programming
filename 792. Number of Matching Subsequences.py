

# Link - https://leetcode.com/problems/number-of-matching-subsequences/

# Space: 
# Time:

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = 0
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        current = self.root
        
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        
        current.isEnd += 1

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        def dfs(root: TrieNode, i: int) -> int:
            
            ans = root.isEnd
            
            for child in root.children:
                j = s.find(child, i, len(s))
                if j != -1:
                    ans += dfs(root.children[child], j+1)
                    
            return ans
        
        return dfs(trie.root, 0)
        