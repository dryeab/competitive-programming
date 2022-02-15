
# link - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        return int('1'*(len(bin(num))-2), 2) - num
