
# Link - https://leetcode.com/problems/longest-palindromic-substring/

# Space: O(n)
# Time: ~

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        ans, last_indices = "", defaultdict(list)
        
        for end in range(len(s)):
            last_indices[s[end]].append(end)
            for start in last_indices[s[end]]:
                if s[start] == s[end]:
                    substring = s[start:end+1]
                    if substring == substring[::-1]: # is palindrome
                        ans = max([ans, substring], key=lambda x: len(x))
                        break;
            
        return ans