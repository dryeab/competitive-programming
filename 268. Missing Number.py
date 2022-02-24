# link - https://leetcode.com/problems/missing-number/

# Solution 1
    # Space: O(1)
    # Time: O(n)
    
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n*(n+1)//2) - sum(nums)
