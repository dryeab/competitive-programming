
# Link - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        
        parent = {i: i for i in range(1, n+1)}
        size = {i: 1 for i in range(1, n+1)}
        
        def find(v):
            if v == parent[v]:
                return v
            parent[v] = find(parent[v])
            return parent[v]
        
        def union(v1, v2):
            
            root1, root2 = find(v1), find(v2)
            
            if root1 != root2:
                
                if size[root1] < size[root2]:
                    parent[root1] = root2
                    size[root2] += size[root1]
                else:
                    parent[root2] = root1
                    size[root1] += size[root2]
                
                return True
            
            return False
        
        answer = None
        for a, b in edges:
            if union(a, b) == False:
                answer = [a, b]
        
        return answer