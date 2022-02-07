# link - https://leetcode.com/problems/find-the-difference/

# space: O(1) ~ O(26)
# time: O(n)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = Counter(s+t)
        for i in c:
            if c[i] % 2:
                return i
            
