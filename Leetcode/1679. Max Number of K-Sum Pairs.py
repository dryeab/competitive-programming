
# Link - https://leetcode.com/problems/max-number-of-k-sum-pairs/

# Space: O(n)
# Time: O(n)

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        ans, count = 0, Counter(nums)
        
        for num in count:
            
            ans += min(count[num], count[k-num])
        
        return ans // 2