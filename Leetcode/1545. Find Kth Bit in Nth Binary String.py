
# Link - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

# Time: O(n)

# Recursive
class Solution:
    def findKthBit(self, n: int, k: int) -> str: # Space: 0(n)

        def helper(n, k):
            if n == 1: return 0
            
            mid = (2**n)/2
            
            if k == mid: return 1
        
            if k < mid: return helper(n-1, k)
           
            k = 2**(n-1) - (k-mid)
            
            val = helper(n-1, k)
            
            return 0 if val == 1 else 1
        
        return str(helper(n,k))

    
# Iterative
class Solution:
    def findKthBit(self, n: int, k: int) -> str: # Space: 0(1)
        
        k -= 1
        reverse = False
        
        while n > 1:
            
            mid = (2**n - 1) // 2
            
            if k == mid:
                return "0" if reverse else "1"
            
            n -= 1
            
            if k > mid:
                reverse = not reverse
                k = mid - ((k - mid - 1) +1)
                
        return "1" if reverse else "0"