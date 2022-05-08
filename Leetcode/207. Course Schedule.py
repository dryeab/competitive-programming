
# Link - https://leetcode.com/problems/course-schedule/

# Space: O(n + m)
# Time: O(n + m)
        # n = numCourses, m = len(prerequisites)

# DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        color = ["white" for _ in range(numCourses)]

        def dfs(course):
            
            color[course] = "gray" # is being visited
            
            for neighbor in graph[course]:
                if color[neighbor] == "gray": # back-edge
                    return False
                if color[neighbor] == "white" and not dfs(neighbor):
                    return False
                
            color[course] = "black"
            
            return True
        
        for course in range(numCourses):
            if color[course] == "white" and not dfs(course):
                return False
        
        return True

# BFS + Topological Sort
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph, outdegree = defaultdict(list), defaultdict(int)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            outdegree[course] += 1
        
        count, q = 0, deque([course for course in range(numCourses) if outdegree[course] == 0])

        while q:
            
            course = q.popleft()
            count += 1
            
            for neighbor in graph[course]: # all dependents of course
                outdegree[neighbor] -= 1
                if outdegree[neighbor] == 0:
                    q.append(neighbor)
        
        return count == numCourses