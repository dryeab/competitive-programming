# link - https://leetcode.com/problems/super-pow/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        ans = 0
        for i in b:
            ans = ans*10 + i
        return pow(a, ans, 1337)
