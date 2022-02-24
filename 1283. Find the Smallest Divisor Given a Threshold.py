# Link - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

# Space: O(1)
# Time: -

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        start = 1
        n = len(nums) if threshold != len(nums) else len(nums) - 1
        end = ceil(sum(nums)/(threshold - n))
        
        while start < end:
            
            mid = (start + end)//2
            
            total = 0
            for num in nums:
                total += ceil(num/mid)
            
            if total > threshold:
                start = mid + 1
            else:
                end = mid
                
        return start
