
# link - https://leetcode.com/problems/zigzag-conversion/

# space: O(n)
# time: O(n)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1: return s
        
        ans = [[] for _ in range(numRows)]
        
        up, j = False, 0
        for char in s:

            ans[j].append(char)
            j += [1,-1][up]
            
            if j >= len(ans) - 1:
                up = True
            elif j == 0:
                up = False
                
        return "".join(["".join(row) for row in ans])
