
# Link - https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

# Space: O(n)
# Time: O(n)

m = 10**9 + 7

class Solution:
    
    def countOrders(self, n: int) -> int:

        if n == 1:
            return 1
        
        return (n * (2*n-1) * self.countOrders(n-1)) % m