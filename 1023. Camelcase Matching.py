
# Link - https://leetcode.com/problems/camelcase-matching/

# Space: 
# Time:

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        def helper(query, i, j): # i - query, j - pattern
             
            if i == len(query): 
                return i == len(query) and j == len(pattern)
            
            if query[i].isupper():
                if j >= len(pattern) or query[i] != pattern[j]:
                    return False
                return helper(query, i+1, j+1)
            else:
                if j < len(pattern) and query[i] == pattern[j]:
                    return helper(query, i+1, j+1)
                return helper(query, i+1, j)
        
        return [helper(query, 0, 0) for query in queries]