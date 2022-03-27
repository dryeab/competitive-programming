
# Link - https://leetcode.com/problems/minimum-operations-to-make-array-equal/

# Space: O(1)
# Time: O(n)

class Solution:
    def minOperations(self, n: int) -> int:
        
        mid = (1 + (2*(n-1) + 1))//2
        
        return sum([mid - (2*i + 1) for i in range(n//2)])