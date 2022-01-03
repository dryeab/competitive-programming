
# link - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

# space: 0(1)
# time: O(n) < O(20)


# solution 1

class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def helper(n, k):
            if n == 1: return 0
            
            mid = (2**n)/2
            
            if k == mid: return 1
        
            if k < mid: return helper(n-1, k)
           
            k = 2**(n-1) - (k-mid)
            
            val = helper(n-1, k)
            
            return 0 if val == 1 else 1
        
        return str(helper(n,k))

    
# solution 2

class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        store = { 'prev': None, 'prev_inv': None }

        def helper(n):
            
            if n == 1:
                cur, inv = '0', '1'
            else:
                prev = helper(n-1)
                inv = store['prev_inv']
                cur =  prev + '1' + inv[::-1]

            for i in range(len(inv), len(cur)):
                inv += ('0' if cur[i] == '1' else '1')
                
            store['prev'] = cur
            store['prev_inv'] = inv

            return cur

        return helper(n)[k-1]
