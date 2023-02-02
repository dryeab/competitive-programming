class Solution:
    def numberOfWays(self, s: str) -> int:
        
        n = len(s)
        
        zel, zer = 0, s.count('0')
        onl, onr = 0, n - zer
        
        res = 0
        for i in range(n):
            if s[i] == '0':
                res += onl * onr
                zel += 1
                zer -= 1
            else:
                res += zel * zer
                onl += 1
                onr -= 1
                
        return res