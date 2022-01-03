
# link - https://leetcode.com/problems/k-th-symbol-in-grammar/

# space: O(1)
# time: O(n) (n = number of rows)

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def helper(n, k):
            if n == 1: return 0

            val = helper(n-1, k//2)

            return val if k % 2 == 0 else (1 if val == 0 else 0)
        
        return helper(n, k-1)
