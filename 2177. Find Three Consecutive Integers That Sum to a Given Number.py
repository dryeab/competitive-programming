
# link - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

# space: O(1)
# time: O(1)

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        return [] if num % 3 else [num//3-1, num//3, num//3+1]
