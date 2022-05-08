# link - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

# space: -
# time: O(n**2)

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        store = [i for i in range(1, n+1)]
        
        def helper(k, store):
            if len(store) == 1:
                return store[0]
            i = (k-1)%len(store)
            return helper(k, store[i+1:] + store[:i])
        return helper(k, store)
