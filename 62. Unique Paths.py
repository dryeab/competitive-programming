# link - https://leetcode.com/problems/unique-paths/

# space: O(n)
# time: O(m*n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {(m, n):0}
        
        if n == 1 and m == 1:
            return 1
        
        def helper(i, j):
            if (i, j) not in memo:
                if j == n or i == m:
                    ans = 1
                else:
                    ans = helper(i+1, j) + helper(i, j+1)
                    
                memo[(i, j)] = ans
            
            return memo[(i, j)]
        
        return helper(1, 1)
            
