# link - https://leetcode.com/problems/jump-game-vi/

# space: O(n)
# time: O(n)

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:

        dmq = deque() # decreasing monotic queue
        dp = [None] * len(nums)
        dp[-1] = nums[-1]

        for i in range(len(nums)-2, -1, -1):
        
            while (dmq and dmq[0] - i > k):
                dmq.popleft()

            while (dmq and dp[i+1] >= dp[dmq[-1]]):
                dmq.pop()
            dmq.append(i+1)

            dp[i] = nums[i] + dp[dmq[0]]

        return dp[0]
