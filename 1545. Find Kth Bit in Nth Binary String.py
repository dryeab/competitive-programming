
# link - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

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
