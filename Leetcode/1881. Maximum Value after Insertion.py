# link - https://leetcode.com/problems/maximum-value-after-insertion/

# space: O(n)
# time: O(n)

class Solution:
    def maxValue(self, n: str, x: int) -> str:
        pos = (n[0] != '-')
        for i in range([1, 0][pos], len(n)):
            if [int(n[i]) > x, int(n[i]) < x][pos]:
                return n[:i] + str(x) + n[i:]
        return n + str(x)
