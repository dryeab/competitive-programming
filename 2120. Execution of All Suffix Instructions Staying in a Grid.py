
# Link - https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

# Space: O(n)
# Time: O(n)

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        
        answer = [-i for i in range(-len(s), 0)]
        
        ins = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1)
        }
        
        for start in range(len(s)):
            
            curX, curY = startPos
            
            for end in range(start, len(s)): # cur instruction
                
                dxn = ins[s[end]] # direction
                curX, curY = curX + dxn[0], curY + dxn[1]

                if not (0 <= curX < n and 0 <= curY < n):
                    answer[start] = end - start
                    break
                
        return answer