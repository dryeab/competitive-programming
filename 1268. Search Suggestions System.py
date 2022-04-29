
# Link - https://leetcode.com/problems/search-suggestions-system/

# Space:
# Time: 

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = [] # heap
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        current = self.root
        
        for char in word:
            
            if char not in current.children:
                current.children[char] = TrieNode()
                
            current = current.children[char]
            heappush(current.words, word) # push the word to it

    def startsWith(self, prefix: str) -> bool:
        
        current = self.root
        
        for char in prefix:
            if char not in current.children:
                return None
            current = current.children[char]
        
        return current
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        trie = Trie()
        
        for product in products:
            trie.insert(product)
        
        result = []
        for i in range(len(searchWord)):
            
            prefix = searchWord[:i+1]
            node = trie.startsWith(prefix)
            
            temp = [heappop(node.words) for _ in range(min(3, len(node.words)))] if node else []
            result.append(temp[::])
            
            while temp:
                heappush(node.words, temp.pop())

        return result