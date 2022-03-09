
# Link - https://leetcode.com/problems/reducing-dishes/

# Space: O(1)
# Time: O(nlog(n))

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort(reverse=True)
        
        sum = ans = 0
        for i in range(len(satisfaction)):
            if sum + satisfaction[i] < 0:
                return ans
            sum += satisfaction[i]
            ans += sum
                    
        return ans