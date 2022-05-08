
# Link - https://leetcode.com/problems/find-eventual-safe-states/

# Space: O(V + E)
# Time: O(V + E)

# DFS
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        n = len(graph)
        safe, color = [False]*n, ["white"]*n

        def dfs(node):

            color[node] = "gray"

            for neighbor in graph[node]:
                if color[neighbor] == "gray":
                    return False
                if color[neighbor] == "white" and not dfs(neighbor):
                    return False

            safe[node] = True
            color[node] = "black"

            return True

        for i in range(n):
            color[i] == "white" and dfs(i)

        return [i for i in range(n) if safe[i]]

# BFS
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
