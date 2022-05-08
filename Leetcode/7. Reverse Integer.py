
# link - https://leetcode.com/problems/reverse-integer/

# space: O(1)
# time: O(n)

class Solution:
    def reverse(self, x: int) -> int:
        is_positive, reverse, x= (x >= 0), 0, abs(x)
        while x:
            reverse = reverse * 10 + x%10
            x //= 10
        if -(2**31) <= reverse <= 2**31 - 1:
            return reverse if is_positive else -reverse
        return 0
