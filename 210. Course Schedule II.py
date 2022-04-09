
# Link - https://leetcode.com/problems/course-schedule-ii/

# Space: O(n + E) 
# Time: O(n + E)

# n = numCourses, E = sum(len(prerequisites[i] for each i))

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        dependents, num_of_reqs = defaultdict(set), [0]*numCourses
        
        for course, pre in prerequisites:
            dependents[pre].add(course)
            num_of_reqs[course] += 1
        
        answer, visited, q = [], set(), deque()
        for i in range(numCourses):
            if i not in visited and num_of_reqs[i] == 0:
                q.append(i)
                while q:
                    course = q.popleft()
                    visited.add(course)
                    answer.append(course)
                    
                    for dependent in dependents[course]:
                        num_of_reqs[dependent] -= 1
                        if num_of_reqs[dependent] == 0:
                            q.append(dependent)
        
        return answer if len(visited) == numCourses else []