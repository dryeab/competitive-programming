
# Link - https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        self.combs = []
        
        self.dfs(k, n, [])
        
        return self.combs
    
    def dfs(self, k, n, comb):

        if (k > n) or (n and not k): return

        if k == n == 0:
            self.combs.append(comb.copy())
            return;
        
        start = comb[-1] + 1 if comb else 1
        
        for i in range(start, 10):
            comb.append(i)
            self.dfs(k-1, n-i, comb)
            comb.pop() # backtrack