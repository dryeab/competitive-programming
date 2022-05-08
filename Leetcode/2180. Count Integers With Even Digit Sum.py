
# link - https://leetcode.com/problems/count-integers-with-even-digit-sum/

class Solution:
    def countEven(self, num: int) -> int:
        
        def digitSum(n):
            return sum([int(i) for i in str(n)])
        
        ans = 0
        for i in range(1, num+1):
            ans += [1,0][digitSum(i)%2]
        return ans
