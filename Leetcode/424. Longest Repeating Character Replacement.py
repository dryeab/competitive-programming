
# Link - https://leetcode.com/problems/longest-repeating-character-replacement/

# Space: O(1)
# Time: O(n)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        store = defaultdict(int)
        ans = start = end = 0
        
        while end < len(s): # window : [start, end]
            
            store[s[end]] += 1
            
            M = max([store[i] for i in store])
            
            while end - start + 1 - M > k:
                store[s[start]] -= 1
                start += 1
                
                M = max([store[i] for i in store])
            
            ans = max(ans, end - start + 1)
            end += 1
            
        return ans