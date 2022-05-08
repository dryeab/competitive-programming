
# Link - https://leetcode.com/problems/longest-word-in-dictionary/

# Space: 
# Time:

class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        set_of_words = set(words)
        
        heap = [(-len(word), word) for word in words]
        heapify(heap)
        
        while heap:
            
            _, word = heappop(heap)
            
            found = True
            for i in range(len(word)):
                if word[:i+1] not in set_of_words:
                    found = False
                    break;
            
            if found: return word
        
        return ""