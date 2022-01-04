# link - https://leetcode.com/problems/power-of-three/

# space: O(1)
# time: O(log(n))


# recursive solution
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def helper(n):
            if n < 3:return False
            if n == 3: return True
            if n % 3: return False
            return helper(n//3)
        return True if n==1 else helper(n)


# iterative solution
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1: return True
        while (n > 3):
            if n % 3: return False
            n //=3
        return True if n == 3 else False
