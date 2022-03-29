
# Link - https://leetcode.com/problems/palindromic-substrings/

# Space: O(n)
# Time: 

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        answer, last_indices = 0, defaultdict(list)
        
        for end in range(len(s)):
            last_indices[s[end]].append(end)
            for start in last_indices[s[end]]:
                substring = s[start:end+1]
                if substring == substring[::-1]:
                    answer += 1
        
        return answer