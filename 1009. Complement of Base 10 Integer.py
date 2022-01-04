
# link - https://leetcode.com/problems/complement-of-base-10-integer/

# space: O(1)
# time: O(n)

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        b = bin(n)[2:]
        ans = 0
        
        for i in range(len(b)):
            ans += (2**i) * (1 if b[-(i+1)] == '0' else 0)
        
        return ans
            
            
