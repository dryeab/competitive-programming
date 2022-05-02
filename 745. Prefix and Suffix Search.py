
# Link - https://leetcode.com/problems/prefix-and-suffix-search/

# Space: 
# Time:

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = -1
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, j: int) -> None:
        
        current = self.root
        
        for i in range(len(word)):
            
            char = word[i] + word[-(i+1)]
            
            if char not in current.children:
                current.children[char] = TrieNode()
                
            current = current.children[char]
        
        current.isEnd = max(current.isEnd, j)

class WordFilter:

    def __init__(self, words: List[str]):
        
        self.words = words
        self.trie = Trie()
        
        for i, word in enumerate(words):
            self.trie.insert(word, i)
        
    def f(self, prefix: str, suffix: str) -> int:
        
        def dfs(root, i):
            
            ans = -1
            
            if root.isEnd != -1 and i >= max(len(prefix), len(suffix)):
                ans = root.isEnd
            
            for child in root.children:
                
                current = root.children[child]
                
                pre = prefix[i] if i < len(prefix) else None
                suf = suffix[-(i+1)] if i < len(suffix) else None
                    
                if (not pre and not suf) or ( not pre and suf == child[1] ) or \
                   ( not suf and pre == child[0] ) or ( pre and suf and pre + suf == child):
                    
                    ans = max(ans, dfs(current, i+1))
            
            return ans
        
        return dfs(self.trie.root, 0)