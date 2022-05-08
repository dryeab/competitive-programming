
# link - https://leetcode.com/problems/smallest-integer-divisible-by-k/

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:

        def validityChecker(k):
            last_digit = k % 10
            for i in range(10):
                if (last_digit * i) % 10 == 1:
                    return True
            return False

        if not validityChecker(k):
            return -1

        n = int('1'*len(str(k)))

        while (n % k):
            n = (n*10) + 1

        return len(str(n))
