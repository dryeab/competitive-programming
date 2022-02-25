# Link - https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

# Space: O(1)
# Time: O(n*log(n))

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        def count(val):
            ans = 0
            for num in nums:
                ans += [0, 1][num >= val]
            return ans
        
        low, high = 1, len(nums)
        
        while low < high:
            
            mid = low + (high - low)//2

            if count(mid) > mid: low = mid + 1
            else: high = mid
        
        return [-1, low][count(low) == low]
