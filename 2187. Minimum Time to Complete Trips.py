
# Link - https://leetcode.com/problems/minimum-time-to-complete-trips/

# Space: O(1)
# Time: O(n*log(D)) :-> D = sum(time)*totalTrips

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        left, right = 1, sum(time)*totalTrips
        
        while left < right:
            mid = (left + right)//2
            if sum(mid//t for t in time) >= totalTrips:
                right = mid
            else:
                left = mid + 1
        
        return left