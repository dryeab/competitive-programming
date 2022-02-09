
# link - https://leetcode.com/problems/valid-parentheses

# space: O(n)
# time: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        
        match = {
            ')': '(',
            '}': '{',
            ']': '['
        }
    
        if s[0] in match: return False
        
        for i in s:
            if i not in match:
                l.append(i)
            else:
                if len(l) == 0:
                    return False
                if match[i] != l.pop():
                    return False
        
        return len(l) == 0
