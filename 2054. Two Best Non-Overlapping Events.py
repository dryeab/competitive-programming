
# Link - https://leetcode.com/problems/two-best-non-overlapping-events/

# Space: O(n)
# Time: O(nlog(n))

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        best_up_to = defaultdict(int)
        
        start_sort = sorted(events) # sort by start
        end_sort = sorted(events, key=lambda event: event[1]) # sort by end
        
        max_so_far = j = 0
        for start, _, __ in start_sort:
            while j < len(events) and end_sort[j][1] < start:
                max_so_far = max(max_so_far, end_sort[j][2])
                j += 1
            best_up_to[start] = max_so_far
        
        answer = 0
        for start, _, value in events:
            answer = max(answer, value + best_up_to[start])
        
        return answer