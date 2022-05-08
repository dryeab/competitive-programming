
# Link - https://leetcode.com/problems/h-index-ii/

# Space: O(1)
# Time: O(log(n))

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        if not citations: return 0
        
        left, right = 0, len(citations) - 1
        while left <= right:
            mid = (left + right)//2
            if mid + citations[mid] >= len(citations):
                right = mid - 1
            else:
                left = mid + 1                
        return len(citations) - left