
# Link - https://leetcode.com/problems/k-th-symbol-in-grammar/

# Time: O(n)

# Recursive
class Solution:
    def kthGrammar(self, n: int, k: int) -> int: # Space: O(n)
        
        if n == 1: return 0
        
        if k % 2: return self.kthGrammar(n-1, (k + 1)//2)
        
        return (self.kthGrammar(n-1, k//2) + 1) % 2

# Iterative
class Solution:
    def kthGrammar(self, n: int, k: int) -> int: # Space: O(1)
        
        reverse = False
        
        while n > 1:
            
            n -= 1
            
            if k % 2: k = (k + 1) // 2
            else:
                k //= 2
                reverse = not reverse
        
        return [0, 1][reverse]