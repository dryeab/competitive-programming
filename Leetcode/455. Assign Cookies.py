
# Link - https://leetcode.com/problems/assign-cookies/

# Space: O(1)
# Time: O(nlog(n))

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort(reverse=True)
        s.sort(reverse=True)
        
        i = j = n = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                n += 1
                j += 1
            i += 1
        
        return n
        