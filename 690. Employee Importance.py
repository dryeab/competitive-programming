"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        mapper = {employee.id: i for i, employee in enumerate(employees)}
        
        def helper(id):
            
            employee = employees[mapper[id]]
            total = employee.importance
            
            for sub in employee.subordinates:
                total += helper(sub)
                
            return total
        
        return helper(id)