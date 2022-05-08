# Link - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

# Space: O(1)
# Time: ~

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def findNumberOfDays(capacity):
            i = sum = 0
            for weight in weights:
                if sum + weight > capacity:
                    i += 1
                    sum = 0
                sum += weight
            return i + 1
        
        start, end = max(weights), sum(weights)
        
        while start < end:
            
            mid = (start + end)//2
            
            d = findNumberOfDays(mid)
            
            if d <= days:
                end = mid
            else:
                start = mid + 1
        
        return start
