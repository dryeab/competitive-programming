# link - https://leetcode.com/problems/find-the-difference/

# space: O(len(s)+len(t))
# time: O(len(s)+len(t))

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = Counter(s+t)
        for i in c:
            if c[i] % 2:
                return i
            
