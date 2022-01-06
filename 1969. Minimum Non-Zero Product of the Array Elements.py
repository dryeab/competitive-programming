# link - https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

# space: O(1)
# time: O(p)

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        last = 2**p -1
        m = 10**9 + 7
        return (pow(last-1, last//2, m) * last)%m
