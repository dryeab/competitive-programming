
# Link - https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

# Space: O(1)
# Time: O(n)

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        swap, count = [[0, 0] for _ in range(6)], Counter()
        
        for i in range(len(tops)):
            
            top, bottom = tops[i], bottoms[i]
            
            count[top] += 1
            
            if bottom != top:
                
                swap[bottom -1][0] += 1
                swap[top - 1][1] += 1
                
                count[bottom] += 1
            
        ans = float('inf')
        for i in range(1, 7):
            if count[i] == len(tops):
                ans = min(ans, *swap[i-1])
        
        return [ans, -1][ans == float('inf')]