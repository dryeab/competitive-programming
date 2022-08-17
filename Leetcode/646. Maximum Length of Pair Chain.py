# https://leetcode.com/problems/maximum-length-of-pair-chain/
# Time: O(NlogN)
# Space: O(1)

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort(key=lambda x: x[1])

        cur, res = -1001, 0

        for left, right in pairs:
            if left > cur:
                res += 1
                cur = right

        return res
