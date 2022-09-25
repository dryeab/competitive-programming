
# https://leetcode.com/contest/weekly-contest-312/problems/number-of-good-paths/
# Time: O(NlogN)
# Space: O(N)

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        
        n, res = len(vals), 0
        
        adj = [[] for _ in range(n)]
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        parent = [i for i in range(n)]
        sz = [1] * n
        
        def find(i):
            if i == parent[i]:
                return i
            
            parent[i] = find(parent[i])
            return parent[i]
        
        def unite(i, j):
            
            i = find(i)
            j = find(j)
            
            if i == j:
                return
            
            if sz[i] > sz[j]:
                i, j = j, i
            
            parent[i] = j
            sz[j] += sz[i]
            
        order = defaultdict(list)
        for i, val in enumerate(vals):
            order[val].append(i)
        
        for val in sorted(order.keys()):
            for i in order[val]:
                for j in adj[i]:
                    if vals[j] <= val:
                        unite(i, j)
            
            cnt = Counter()
            for i in order[val]:
                cnt[find(i)] += 1
                res += cnt[find(i)]
        
        return res
        
        