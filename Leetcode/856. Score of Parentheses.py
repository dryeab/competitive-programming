
# Link - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        def score(i, j):
 
            ans, count = 0, [0, 0] # answer, count of "(" and ")"
            
            start = end = i
            while end < j:
                
                count[s[end] == ')'] += 1 # increment the count
                
                if count[0] == count[1]: # balanced
                    if end == start + 1:
                        ans += 1
                    else:
                        ans += 2*score(start+1, end)   
                    start, count = end + 1, [0, 0] # reset start and count
                    
                end += 1
            
            return ans
        
        return score(0, len(s))