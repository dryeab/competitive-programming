
# Link - https://leetcode.com/problems/min-cost-to-connect-all-points/

# Space:
# Time:

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # MST - minimum spanning tree
        
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
        
        heap, visited, = [], set() # key: edge, value: manhattan distance
        for i, point1 in enumerate(points):
            for j, point2 in enumerate(points):
                if i != j and (i, j) not in visited and (j, i) not in visited:
                    distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                    heappush(heap, (distance, (i, j)))
                    visited.add((i, j))
        
        parent = {i: i for i in range(len(points))}
        size = {i: 1 for i in range(len(points))}
        
        answer = 0
        while heap:
            distance, (i, j) = heappop(heap)
            if union(i, j):
                answer += distance
        
        return answer