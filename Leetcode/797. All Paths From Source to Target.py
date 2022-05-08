
# Link - https://leetcode.com/problems/all-paths-from-source-to-target/

# Space: O(n*2^n)
# Time:  O(2^n)

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def dfs(i):
            
            if i == len(graph) - 1: return [[i]]
            
            result = []
            for neighbor in graph[i]:
                for val in dfs(neighbor):
                    val.append(i)
                    result.append(val)
            
            return result
        
        return [l[::-1] for l in dfs(0)]