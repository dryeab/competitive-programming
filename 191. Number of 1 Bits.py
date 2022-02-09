# link - https://leetcode.com/problems/number-of-1-bits/

# space: O(1) 
# time: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
