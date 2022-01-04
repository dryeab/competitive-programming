# link - https://leetcode.com/problems/power-of-four/

# space: O(1)
# time: O(log(n))

# recursive solution
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def helper(n):
            if n < 4:return False
            if n == 4: return True
            if n % 4: return False
            return helper(n//4)
        return True if n==1 else helper(n)


# iterative solution
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1: return True
        while (n > 4):
            if n % 4: return False
            n //= 4
        return True if n == 4 else False
