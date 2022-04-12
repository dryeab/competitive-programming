
# Link - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

# Space: O(n + E) : E = len(edges)
# Time: O(n^2)

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        num_of_parents, children = [0]*n, defaultdict(set)
        for frm, to in edges:
            num_of_parents[to] += 1
            children[frm].add(to)
        
        answer, q = [set() for _ in range(n)], deque()
        for i in range(n):
            if num_of_parents[i] == 0 and not answer[i]:
                q.append(i)
                while q:
                    edge = q.popleft()
                    for child in children[edge]:
                        answer[child] = answer[child].union(answer[edge]).union({edge})
                        num_of_parents[child] -= 1
                        if num_of_parents[child] == 0:
                            q.append(child)
        
        return [sorted(list(ancestors)) for ancestors in answer]


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        children = defaultdict(set)
        for frm, to in edges:
            children[frm].add(to)
        
        answer = [[] for _ in range(n)]
        
        def dfs(ancestor, current):
            for child in children[current]:
                if not answer[child] or answer[child][-1] != ancestor:
                    answer[child].append(ancestor)
                    dfs(ancestor, child)
        
        for i in range(n):
            dfs(i, i)
        
        return answer