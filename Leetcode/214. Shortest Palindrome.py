
# Link - https://leetcode.com/problems/shortest-palindrome/

# Space: O(1)
# Time:

class Solution:
    def shortestPalindrome(self, s: str) -> str:

        for i in range(len(s) - 1, -1, -1):
            if s[i] == s[0]:
                substring = s[:i+1]
                if substring == substring[::-1]: # is palindrome
                    return s[i+1:][::-1] + s
        
        return s[::-1] + s