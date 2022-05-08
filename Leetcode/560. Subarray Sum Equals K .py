# link - https://leetcode.com/problems/subarray-sum-equals-k/

# space: O(n)
# time: O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        ans, c = 0, Counter(nums)
        
        for num in nums:
            
            c[num] -= 1
            
            if num == k:
                ans += 1
            
            ans += c[num + k]

        return ans
