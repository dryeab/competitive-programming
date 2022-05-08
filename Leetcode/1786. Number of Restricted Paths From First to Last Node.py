
# Link - https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

# Space: 
# Time: O(m*log(n)) :-> m = len(edges)

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))
        
        # dijkstra
        
        heap, shortest, ways = [(0, n)], [float('inf')]*(n+1), [0]*(n+1)
        ways[n] = 1

        while heap:
            
            distance, node = heappop(heap)
            
            if shortest[node] != float('inf'): # we have already reached it
                continue
                
            shortest[node] = distance
            
            for neighbor, weight in graph[node]:
                
                if shortest[neighbor] < shortest[node]:
                    ways[node] += ways[neighbor]
                else:
                    heappush(heap, (distance + weight, neighbor))
        
        return ways[1] % (10**9 + 7)