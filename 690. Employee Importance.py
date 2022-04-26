
# Link - https://leetcode.com/problems/employee-importance/

# Space: O(n)
# Time: O(n)

# DFS
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        employees = {emp.id: emp for emp in employees}
        
        def dfs(id):
            
            emp = employees[id]
            
            return emp.importance + sum(dfs(sub_id) for sub_id in emp.subordinates)

        return dfs(id)


# BFS
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        emps = {emp.id: emp for emp in employees}
        
        answer, q = 0, deque([id])
        while q:
            
            emp = emps[q.popleft()]
            answer += emp.importance
            
            for sub in emp.subordinates:
                q.append(sub)
        
        return answer