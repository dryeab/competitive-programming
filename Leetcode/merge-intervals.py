# link - https://leetcode.com/problems/merge-intervals/submissions/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) < 2:
            return intervals  # nothing to merge

        intervals = sorted(intervals) # sort the intervals

        i = 0
        j = 1
        while (j < len(intervals)):
            if intervals[i][1] >= intervals[j][0]:
                intervals[i] = [intervals[i][0], max(intervals[j][1], intervals[i][1])]
            else:
                i += 1
                intervals[i] = intervals[j] 
            j += 1

        return intervals[:i+1]
