
# Link - https://leetcode.com/problems/solving-questions-with-brainpower/

# Space: O(n)
# Time: O(n)

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        dp = [0]*len(questions)
        dp[-1] = questions[-1][0]
        
        for i in range(len(questions) - 2, -1, -1):
            
            max_point = dp[i+1]
            
            next = i + questions[i][1] + 1
            max_point = max(
                max_point, 
                (dp[next] if next < len(questions) else 0) + questions[i][0]
            )

            dp[i] = max_point
        
        return max(dp)