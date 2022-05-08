
# link - https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

# space: O(n)
# time: O(n)

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        return [s[i:i+k] + fill*max(0, i+k-len(s)) for i in range(0, len(s), k)]
