

# link - https://leetcode.com/problems/teemo-attacking/

# space: O(1)
# time: O(n)

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        i = ans = 0
        while i < len(timeSeries):
            ans += min(duration, timeSeries[i+1]-timeSeries[i]) if i != len(timeSeries) - 1 else duration
            i += 1
        return ans
