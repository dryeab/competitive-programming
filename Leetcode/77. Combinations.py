
# Link - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        self.combs = []
        self.n = n
        
        self.dfs(k, [])
        
        return self.combs
    
    def dfs(self, k, comb):
        
        if k == 0:
            self.combs.append(comb.copy())
            return 
        
        start = comb[-1] + 1 if comb else 1
        
        for i in range(start, self.n + 1):
            comb.append(i)
            self.dfs(k - 1, comb)
            comb.pop()
            