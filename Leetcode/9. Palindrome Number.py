# link - https://leetcode.com/problems/palindrome-number/

# space: O(1)
# time: O(n)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0: return False
        
        reverse, copy = 0, x
        while copy:
            reverse = (reverse*10) + copy%10
            copy //= 10
        return x == reverse
