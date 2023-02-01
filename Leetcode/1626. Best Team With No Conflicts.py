class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        n = len(scores)
        
        player = sorted(list(zip(ages, scores)))
        
        @cache
        def dp(i, j):
            
            if i == n:
                return 0
            
            res = dp(i + 1, j) # don't choose
            if j == -1 or player[j][0] == player[i][0] or player[j][1] <= player[i][1]:
                res = max(res, dp(i + 1, i) + player[i][1]) # choose
            
            return res
        
        return dp(0, -1)
            
            
            
            
            