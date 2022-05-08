
# Link - https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

# Space: O(1)
# Time: O(n)

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        start = end = answer = 0
        
        while end < len(prices):
            if end and prices[end-1] != prices[end] + 1:
                start = end
            answer += end - start + 1
            end += 1
        
        return answer