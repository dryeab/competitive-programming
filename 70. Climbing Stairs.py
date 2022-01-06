# link - https://leetcode.com/problems/climbing-stairs/

# space: O(1)
# time: O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1: return n
        prev, prev_prev = 1, 1
        for i in range(2, n):
            prev, prev_prev = prev + prev_prev, prev
        return prev_prev + prev
