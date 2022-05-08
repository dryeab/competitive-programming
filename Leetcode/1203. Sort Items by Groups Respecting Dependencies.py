
# Link - https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

# Space: -
# Time: O(n + E) :-> E = number of edges(sum(len(beforeItems[i])) for each i)

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        belongs_to, index = defaultdict(list), {}
        # belongs_to[i] = set of items that belong to group i
        for i in range(len(group)): # assign them group
            if group[i] == -1:
                group[i] = m
                m += 1
            index[i] = len(belongs_to[group[i]])
            belongs_to[group[i]].append(i)
        
        # O(n)
        
        ######### Check if there is a cycle #######
        
        memo = set()
        def dfs(i, path): # to detect cycle
            
            if i not in memo:
                
                for item in beforeItems[i]:

                    if item in path:
                        return False
                    
                    path.add(item)
                    if dfs(item, path) == False:
                        return False
                    path.remove(item)

                memo.add(i)
            
            return True
        
        for i in range(len(group)):
            if i not in memo and dfs(i, {i}) == False:
                return []
        
        # O(n + E) : E = number of edges(sum(len(beforeItems[i])) for each i)
        
        ######### no cycle ###########
        
        num_of_pres, dependents = defaultdict(int), defaultdict(set)
        for i, pres in enumerate(beforeItems):
            
            for pre in pres:
                
                if group[i] == group[pre]: # the two items belong to a same group
                    
                    before, after = min(index[i], index[pre]), max(index[i], index[pre])
                    
                    belongs_to[group[i]][before] = pre
                    belongs_to[group[i]][after] = i
                    
                    index[i], index[pre] = after, before
                    
                else:
                    if group[i] not in dependents[group[pre]]:
                        dependents[group[pre]].add(group[i])
                        num_of_pres[group[i]] += 1
        
        
        # O(n)
        
        answer, q, visited = [], deque(), set()
        # visited - set of visited groups
        
        for i in range(m):
            
            if i not in visited and num_of_pres[i] == 0:
                q.append(i)
                visited.add(i)
                
                while q:
                    g = q.popleft() # this group can, now, be added
                    answer.extend(belongs_to[g])
                    
                    for dependent in dependents[g]:
                        num_of_pres[dependent] -= 1
                        if num_of_pres[dependent] == 0:
                            q.append(dependent)
                            visited.add(dependent)

        # O(n + E) -> E: number of edges
        
        return answer if len(visited) == m else []