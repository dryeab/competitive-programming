
# link - https://leetcode.com/problems/count-operations-to-obtain-zero/

# space: O(1)
# time: O(n)

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        i = 0
        while num1 and num2:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            i +=1
        return i
