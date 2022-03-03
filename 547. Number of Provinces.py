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