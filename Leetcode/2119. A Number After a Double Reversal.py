
# link - https://leetcode.com/problems/a-number-after-a-double-reversal/

# space = time = O(1)

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num%10 != 0 if num else True
