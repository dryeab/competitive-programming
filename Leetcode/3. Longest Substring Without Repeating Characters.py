# link - https://leetcode.com/problems/longest-substring-without-repeating-characters/

# space: O(n)
# time: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = set()
        i = j = ans = 0
        while (j < len(s)):
            if s[j] in current:
                ans = max(ans, j-i)
                while (s[i] != s[j]):
                    current.remove(s[i])
                    i += 1
                i += 1
            current.add(s[j])
            j += 1
        
        return max(ans, j-i)
                
        
