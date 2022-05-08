
# Link - https://leetcode.com/problems/minimum-size-subarray-sum/

# Solution 1
    # Space: O(1)
    # Time: O(n)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        i = j = sum =  0
        ans = float('inf')
        
        while j < len(nums):
            
            sum += nums[j]
                
            while sum >= target and i <= j:
                ans = min(ans, j- i + 1)
                sum -= nums[i]
                i += 1
                
            j += 1
            
        return [ans, 0][ans == float('inf')]

# Solution 2
    # Space: O(1)
    # Time: O(n*log(n))

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        def isNPossible(n):
            s, i = sum(nums[:n]), n
            
            while i < len(nums):
                if s >= target: 
                    return True
                s += nums[i]  - nums[i-n]
                i += 1
                
            return s >= target
            
        left, right = 1, len(nums)
        while left < right:
            
            mid = (left + right)//2
            
            if isNPossible(mid):
                right = mid
            else:
                left = mid + 1
                
        return [0, left][isNPossible(left)]