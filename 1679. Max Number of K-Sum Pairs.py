# link - https://leetcode.com/problems/max-number-of-k-sum-pairs

# space: O(n)
# time: O(n)

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        ans, count = 0, Counter(nums)
        for num in count:
            if k / 2 == num:
                val = count[num]//2
                count[num] -= val*2
            else:
                val = min(count[num], count[k-num])
                count[num] -= val
                if k - num in count:
                    count[k-num] -= val
            ans += val
        return ans
            
