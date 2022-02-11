
# link - https://leetcode.com/problems/permutation-in-string/

# space: O(n)
# time: -

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2): return False
        
        i, j = 0, len(s1)
        c, cs = Counter(s2[:j]), Counter(s1)
        
        while (c != cs and j < len(s2)):
            c[s2[i]] -= 1
            if not c[s2[i]]:
                c.pop(s2[i])
            c[s2[j]] += 1
            i += 1
            j += 1
        return c == cs
