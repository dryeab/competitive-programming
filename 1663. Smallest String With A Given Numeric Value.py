
# Link - https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

# Space: O(n)
# Time: O(n)

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        store = {ord(char) % 96: char for char in string.ascii_lowercase}
        
        def helper(n, k, ans=[]):
            
            if n == 0:
                return ans

            dif = k - 26*(n-1)
            val = 1 if dif <= 1 else dif
            
            ans.append(store[val])
            
            return helper(n-1, k-val, ans)
        
        return "".join(helper(n, k))