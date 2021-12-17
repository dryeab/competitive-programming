
# link - https://leetcode.com/problems/find-original-array-from-doubled-array

class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:

        from collections import Counter
        c = Counter(changed)
        
        if 0 in c:
            if c[0] % 2: return []
            c[0] /= 2

        keys = sorted(c.keys())
        for i in keys:
            if i == 0: continue;
            j = i * 2
            if c[i] > c[j]:
                return []
            c[j] -= c[i]
        
        ans = [None] * (len(changed)//2)
        k = 0
        for i, j in c.items():
            while j:
                ans[k] = i
                j -= 1
                k += 1
        
        return ans
