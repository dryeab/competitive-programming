# Link - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

# Space: O(1)
# Time: O(n * log(m)) :-> m = max(nums)

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        left, right = 1, max(nums)
    
        while left < right:
            
            mid = (left + right)//2
            
            if sum(ceil(num/mid) for num in nums) <= threshold:
                right = mid
            else:
                left = mid + 1
        
        return left