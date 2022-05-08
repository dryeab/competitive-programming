
# Link - https://leetcode.com/problems/course-schedule-ii/

# Space: O(n + E) 
# Time: O(n + E)

# n = numCourses, E = sum(len(prerequisites[i] for each i))

# DFS - Topological Sort
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        self.hasCycle = False
        
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        topsort, color = [], ["white"]*numCourses
        
        def dfs(course):
            
            color[course] = "gray"
            
            for neighbor in graph[course]:
                if color[neighbor] == "gray":
                    self.hasCycle = True
                if color[neighbor] == "white":
                    dfs(neighbor)
            
            topsort.append(course)
            color[course] = "black"
        
        for course in range(numCourses):
            if color[course] == "white":
                dfs(course)
        
        return [] if self.hasCycle else topsort
        

# BFS - Topological Sort
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph, outgoing = defaultdict(list), defaultdict(int)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            outgoing[course] += 1
        
        q = deque([course for course in range(numCourses) if outgoing[course] == 0])
        count, topsort = 0, []
        
        while q:
            course = q.popleft()
            topsort.append(course)
            count += 1
            
            for neighbor in graph[course]:
                outgoing[neighbor] -= 1
                if outgoing[neighbor] == 0:
                    q.append(neighbor)
        
        return topsort if count == numCourses else []