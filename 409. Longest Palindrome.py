# link - https://leetcode.com/problems/longest-palindrome/

# space: O(n)
# time: O(n)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        c, odd, ans = Counter(s), 1, 0
        
        for i in c:
            if c[i] % 2: # odd
                if odd:
                    ans += c[i]
                    odd -= 1
                else:
                    ans += c[i]//2 * 2
            else:
                ans += c[i]
                
        return ans
