
# Link - https://leetcode.com/problems/parallel-courses-iii/

# Space: O(n + m) : m = len(relations)
# Time: O(n + m)

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        graph = defaultdict(list)
        for prev, next in relations:
            graph[prev].append(next)
            
        memo = {}
        
        def dp(course):
            
            if len(graph[course]) == 0:
                return time[course - 1]
            
            if course not in memo:
                memo[course] = time[course - 1] + max(dp(next) for next in graph[course])
                
            return memo[course]
        
        return max(dp(course) for course in range(1, n+1))