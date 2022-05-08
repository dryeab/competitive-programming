
# Link - https://leetcode.com/problems/di-string-match/

# Space: O(n)
# Time: O(n)

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        
        ans, q = [], deque([i for i in range(len(s)+1)])
        
        for l in s:
            if l == "I":
                ans.append(q.popleft())
            else:
                ans.append(q.pop())
                
        ans.append(q.pop()) # one left
        return ans