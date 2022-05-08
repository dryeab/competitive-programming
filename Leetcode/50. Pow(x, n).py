
# link - https://leetcode.com/problems/powx-n/

# space: O(1)
# time: O(log(n))

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, -n)
        if n % 2 == 0:
            return  self.myPow(x, n//2) ** 2
        return x * self.myPow(x, n-1)
