
# Link - https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# Space: O(n)
# Time: O(n)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        to_be_removed, stack = set(), []
        
        for i, char in enumerate(s):
            
            if char == '(':
                stack.append(i)
            
            if char == ')':
                if not stack:
                    to_be_removed.add(i)
                else:
                    stack.pop()
        
        while stack:
            to_be_removed.add(stack.pop())
            
        return "".join([ s[i] for i in range(len(s)) if i not in to_be_removed])