
# Link - https://leetcode.com/problems/first-bad-version/

# Space: O(n)
# Time: O(log(n))

class Solution:
    def firstBadVersion(self, n: int) -> int:

        i, j = 0, n
        
        while i < j:
            
            mid = (i+j)//2
            isBad = isBadVersion(mid)
            
            if isBad: j = mid
            else: i = mid + 1
                
        return i
