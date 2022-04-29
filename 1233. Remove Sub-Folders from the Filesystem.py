
# Link - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

# Solution 1
    # Space: O(n)
    # Time: O(nlog(n) + m*n)

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        heapq.heapify(folder) # O(m*n)
        answer = [heapq.heappop(folder)] # n
        
        while folder: # O(nlog(n))
            f = heapq.heappop(folder)
            n = len(answer[-1])
            if f[:n] != answer[-1] or f[n] != '/':
                answer.append(f)
        
        return answer


# Solution 2
    # Space: O(n)
    # Time: (m^2 * n)
    
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        c_folder = set(folder)
        
        for f in folder:
            for j in range(1, len(f)):
                if f[j] == '/':
                    if f[:j] in c_folder:
                        c_folder.remove(f)
                        break
        
        return list(c_folder)

# Solution 3: Trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        current = self.root
        
        for char in word.split("/"):
            if char:
                if char not in current.children:
                    if current.isEnd: return
                    current.children[char] = TrieNode()
                current = current.children[char]
        
        current.children = {} # remove all its subfolders
        current.isEnd = True

    def search(self, word: str, isPrefix=False) -> bool:
        
        current = self.root
        
        for char in word.split("/"):
            if char:
                if char not in current.children:
                    return False
                current = current.children[char]
                
        current.isEnd = False
        return True
    
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        trie = Trie()
        for f in folder: trie.insert(f)
        
        result = []
        for f in folder:
            if f.endswith("/"):
                if trie.search(f[:-1]): continue
            if trie.search(f):
                result.append(f)
                
        return result