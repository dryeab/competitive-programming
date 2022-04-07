
# Link - https://leetcode.com/problems/course-schedule/

# Space: O(n)
# Time: O(V + E) ;-> V = numCourses, E = len(prerequisites)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        dependents, num_of_reqs = defaultdict(set), [0]*numCourses
        
        for course, pre in prerequisites:
            dependents[pre].add(course)
            num_of_reqs[course] += 1
        
        visited, q = set(), deque()
        for i in range(numCourses):
            if i not in visited and num_of_reqs[i] == 0:
                q.append(i)
                while q:
                    course = q.popleft()
                    visited.add(course)
                    
                    for dependent in dependents[course]:
                        num_of_reqs[dependent] -= 1
                        if num_of_reqs[dependent] == 0:
                            q.append(dependent)
        
        return len(visited) == numCourses