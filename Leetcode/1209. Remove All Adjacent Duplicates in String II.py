
# Link - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

# Space: O(n)
# Time: O(n)

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        
        for letter in s:
            
            if not stack or letter != stack[-1][0]:
                stack.append([letter, 1])  
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k: stack.pop()
        
        return "".join(char*freq for char, freq in stack)
