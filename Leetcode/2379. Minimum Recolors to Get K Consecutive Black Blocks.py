class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        res = float('inf')
        cnt = 0
        n = len(blocks)
        j = 0
        for i in range(n):
            while j < n and j - i < k:
                cnt += blocks[j] == 'W'
                j += 1
            if j - i >= k:
                res = min(res, cnt)
            
            cnt -= blocks[i] == 'W'
        
        return res