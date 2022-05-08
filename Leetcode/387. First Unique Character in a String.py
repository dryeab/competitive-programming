
# link - https://leetcode.com/problems/first-unique-character-in-a-string/

#space: O(n)
#time: O(n)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
        return -1
        
