
# Link - https://leetcode.com/problems/sum-of-distances-in-tree/

# Space: O(n)
# Time: O(n)

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        answer, adj = [0]*n, defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        # treat 0 as root
        children = {} # node: number of its children
        
        def dfs(i, depth, parent):
            
            answer[0] += depth
            
            children[i] = sum(dfs(a, depth + 1, i) for a in adj[i] if a != parent)
            
            return 1 + children[i]
        
        dfs(0, 0, None)
        
        def adjust(i):
            for a in adj[i]:
                if answer[a] == 0: # if not its parent
                    answer[a] = answer[i] - children[a] + (n - children[a] - 2)
                    adjust(a)
        
        adjust(0)
        
        return answer