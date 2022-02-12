
# link - https://leetcode.com/problems/insert-interval/

# space: O(n)
# time: O(n)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, answer = 0, []
        while (i < len(intervals)):
            interval = intervals[i]
            if newInterval:
                if interval[0] <= newInterval[0]:
                    answer.append(interval)
                    i += 1
                else:
                    if answer and answer[-1][1] >= newInterval[0]:
                        answer[-1][0] = min(answer[-1][0], newInterval[0])
                        answer[-1][1] = max(answer[-1][1], newInterval[1])
                    else:
                        answer.append(newInterval)
                    newInterval = None
            else:
                if answer and answer[-1][1] >= interval[0]:
                    answer[-1][0] = min(answer[-1][0], interval[0])
                    answer[-1][1] = max(answer[-1][1], interval[1])
                else:
                    answer.append(interval)
                i += 1
                
        if newInterval:
            if answer and answer[-1][1] >= newInterval[0]:
                answer[-1][0] = min(answer[-1][0], newInterval[0])
                answer[-1][1] = max(answer[-1][1], newInterval[1])
            else:
                answer.append(newInterval)
            
        return answer
