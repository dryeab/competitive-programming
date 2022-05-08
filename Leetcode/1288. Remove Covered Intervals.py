
# link - https://leetcode.com/problems/remove-covered-intervals/


# space: O(1)
# time: O(nlog(n))

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        def isCovered(a, b, c, d):
            return c <= a and b <= d
            
        intervals.sort()
        
        j = 0
        for i in range(1, len(intervals)):
            if isCovered(*intervals[i], *intervals[j]):
                intervals[i] = None
            else:
                if isCovered(*intervals[j], *intervals[i]):
                    intervals[j] = None
                j = i
                
        return len(intervals) - intervals.count(None)
      
      
# space: O(1)
# time: O(n**2)

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        for i in range(len(intervals)):
            if intervals[i]:
                a, b = intervals[i]
                for j in range(len(intervals)):
                    if i != j and intervals[j]:
                        c, d = intervals[j]
                        if a <= c and d <= b:
                            intervals[j] = None
                            
        ans = 0
        for interval in intervals:
            if interval:
                ans += 1
                
        return ans
