class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(n: int) -> List[List[int]]: 
            
            if n == len(graph) - 1:
                return [[n]]
            
            store = []
            
            for i in graph[n]:
                val = dfs(i)
                while val:
                    store.append([n] + val.pop())
            return store
        
        return dfs(0)