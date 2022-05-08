
# Link - https://leetcode.com/problems/number-of-provinces/

# Space: -
# Time: -

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n, visited = len(isConnected), set()
        
        def addProvince(city):
            visited.add(city)
            for i in range(n):
                if (isConnected[city][i] == 1) and (i not in visited):
                    addProvince(i)
                    
        provinces = 0     
        for city in range(n):
            if city not in visited:
                addProvince(city)
                provinces += 1
                    
        return provinces


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        parent = {i: i for i in range(n)}
        size = {i: 1 for i in range(n)}
        
        def find(v):
            if v == parent[v]:
                return v
            parent[v] = find(parent[v])
            return parent[v]
        
        def union(v1, v2):
            
            root1, root2, = find(v1), find(v2)
            
            if root1 == root2: return  # already in the same group
            
            if size[root1] < size[root2]:
                parent[root1] = root2
                size[root2] += size[root1]
            else:
                parent[root2] = root1
                size[root1] += size[root2]
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    union(i, j)
        
        answer = set()
        for i in range(n): # just to be safe
            find(i)
            answer.add(parent[i])
        
        return len(answer)