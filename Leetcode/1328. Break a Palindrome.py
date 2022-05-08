
# Link - https://leetcode.com/problems/break-a-palindrome/

# Space: O(n)
# Time: O(n)

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        for i in range(len(palindrome)):
            if palindrome[i] != 'a':
                if len(palindrome) % 2 == 0 or \
                        (i != len(palindrome)//2):
                    return palindrome[:i] + 'a' + palindrome[i+1:]
        
        return palindrome[:-1] + 'b' if len(palindrome) != 1 else ''