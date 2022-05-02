
# Link - https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

# Space:
# Time:

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        self.hasCycle = False
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
        
        topsort, state = [], ["white" for _ in range(len(colors))]
        
        def dfs(node):
            
            state[node] = "gray"
            
            for neighbor in graph[node]:
                if state[neighbor] == "gray":
                    self.hasCycle = True
                elif state[neighbor] == "white":
                    dfs(neighbor)
            
            topsort.append(node)
            state[node] = "black"
        
        for i in range(len(colors)):
            if state[i] == "white":
                dfs(i)
                
        if self.hasCycle: return -1
        
        answer = [Counter() for _ in range(len(colors))]
        
        for node in topsort:
            
            for neighbor in graph[node]:
                for color in answer[neighbor]:
                    answer[node][color] = max(answer[node][color], answer[neighbor][color])  
                    
            answer[node][colors[node]] += 1 # add its own color
        
        return max(max(answer[i].values()) for i in range(len(answer)))