
# Link - https://leetcode.com/problems/jump-game-iii/

# Space: O(n)
# Time: ~

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        inBound = lambda i: 0 <= i < len(arr)
        visited = set()
        
        def dfs(i):
            
            if i in visited:
                return False
            
            if arr[i] == 0:
                return True
            
            visited.add(i)
            
            j, k = i + arr[i], i - arr[i]
            
            return (dfs(j) if inBound(j) else False) or (dfs(k) if inBound(k) else False)
        
        return dfs(start)