
# Link - https://leetcode.com/problems/jump-game-iv/

# Space: O(n)
# Time: 

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        index = defaultdict(list)
        
        for i, num in enumerate(arr):
            index[num].append(i)
        
        def bfs(i):
            
            q, visited, count = deque([i]), {i}, 0
            
            inBound = lambda i: 0 <= i < len(arr)
            
            while q:
                
                for _ in range(len(q)):
                    
                    j = q.popleft()
                    
                    if j == len(arr) - 1:
                        return count
                    
                    # the left neighbor
                    if inBound(j-1) and j-1 not in visited:
                        q.append(j-1)
                        visited.add(j-1)
                    
                    # the right neighbor
                    if inBound(j+1) and j+1 not in visited:
                        q.append(j+1)
                        visited.add(j+1)
                    
                    # indices with the same value
                    while index[arr[j]]:
                        k = index[arr[j]].pop()
                        if k not in visited:
                            q.append(k)
                            visited.add(k)
                        
                count += 1
        
        return bfs(0)