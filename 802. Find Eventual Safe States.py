
# Link - https://leetcode.com/problems/find-eventual-safe-states/

# Space: O(n + E) 
# Time: O(n + E)

# n = len(graph), E = number of edges (sum(len(graph[i]) for each i))

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        num_of_reqs, dependents = [0]*len(graph), defaultdict(set)
        for i, neighbors in enumerate(graph):
            num_of_reqs[i] = len(neighbors)
            for neighbor in neighbors:
                dependents[neighbor].add(i)
        
        answer, q = set(), deque()
        for node in range(len(graph)):
            if node not in answer and num_of_reqs[node] == 0:
                q.append(node)
                while q:
                    safe = q.popleft()
                    answer.add(safe)
                    
                    for dependent in dependents[safe]:
                        num_of_reqs[dependent] -= 1
                        if num_of_reqs[dependent] == 0:
                            q.append(dependent)
        
        return sorted(list(answer))