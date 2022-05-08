
# Link - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

# Space: O(n)
# Time: O(n)

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack, answer = [], 0
        
        for bracket in s:
            if bracket == '(':
                stack.append(bracket)
            else:
                if not stack:
                    answer += 1
                else:
                    stack.pop()
        
        return answer + len(stack)