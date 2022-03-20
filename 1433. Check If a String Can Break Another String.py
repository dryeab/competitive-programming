
# Link - https://leetcode.com/problems/check-if-a-string-can-break-another-string/

# Space: O(1) ~ O(26)
# Time: O(n)

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        
        c1, c2 = Counter(s1), Counter(s2)
        
        def isBigger(c1, c2):
            
            s1 = s2 = 0
            
            for l in string.ascii_lowercase[::-1]:
                
                s1 += c1[l]
                s2 += c2[l]
                
                if s1 < s2: return False
            
            return True
        
        return isBigger(c1, c2) or isBigger(c2, c1)
            