# link - https://leetcode.com/problems/valid-palindrome/

# space: O(n)
# time: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s) - 1
        while (i < j):
            while i < j and not s[i].isalnum(): i += 1
            while i < j and not s[j].isalnum(): j -= 1
            if s[i] != s[j]: return False
            i, j = i +1, j - 1
        return True
