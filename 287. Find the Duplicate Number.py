
# Link - https://leetcode.com/problems/find-the-duplicate-number/

# Space: O(1)
# Time: O(n*log(n))

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        def count(val):
            ans = 0
            for num in nums:
                if num <= val:
                    ans += 1
            return ans
        
        start, end = 1, len(nums) - 1
        
        while start < end:
            
            mid = (start + end)//2
            c = count(mid)
            
            if c > mid:
                end = mid
            else:
                start = mid + 1
                
        return start
