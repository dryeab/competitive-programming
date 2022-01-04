# link - https://leetcode.com/problems/find-the-town-judge/

# space: O(n)
# time: O(n)

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if n == 1: return 1
        
        store = {}
        trusted = set()
        
        for i in trust:
            trust = i[1]
            trusted.add(i[0])
            
            store[trust] = 1 if trust not in store else store[trust] + 1
        
        for i in store:
            if store[i] == n - 1 and i not in trusted:
                return i
        return -1
            
