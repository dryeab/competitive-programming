
# Link - https://leetcode.com/problems/course-schedule-iv/

# Space: O(E) : E - number of edges / len(prerequisites)
# Time: O(n^2)

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        dependents = defaultdict(set)
        for pre, course in prerequisites:
            dependents[pre].add(course)
        
        store = defaultdict(set) 
        # key: course
        # value: all descendants of course
        
        def dfs(course, descendant):
            
            if descendant in store:
                store[course].update(store[descendant])
            else:
                for dependent in dependents[descendant]:
                    if dependent not in store[course]:
                        store[course].add(dependent)
                        dfs(course, dependent)
        
        for course in range(numCourses):
            dfs(course, course)
        
        for i, (u, v) in enumerate(queries):
            queries[i] = v in store[u]
        
        return queries