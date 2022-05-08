
# Link - https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

# Space:
# Time:

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        neighbors, time = defaultdict(set), {}
        for x, y, t in roads:
            neighbors[x].add(y)
            neighbors[y].add(x)
            time[(x, y)] = time[(y, x)] = t

        # dijkstra
            
        heap, ways, shortest_time = [(0, 0)], [0]*n, [float('inf')]*n
        ways[0], shortest_time[0] = 1, 0
        
        while heap:
            
            time_taken, node = heapq.heappop(heap)

            if node == n - 1:
                return ways[-1] % (10**9 + 7)
                
            for neighbor in neighbors[node]:
                
                time_to_neighbor = time_taken + time[(node, neighbor)]
                
                if time_to_neighbor < shortest_time[neighbor]:
                    ways[neighbor] = ways[node]
                    shortest_time[neighbor] = time_to_neighbor
                    heapq.heappush(heap, (time_to_neighbor, neighbor))
                elif time_to_neighbor == shortest_time[neighbor]:
                    ways[neighbor] += ways[node]