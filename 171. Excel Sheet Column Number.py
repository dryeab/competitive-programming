
# link - https://leetcode.com/problems/excel-sheet-column-number/

# space: O(1)
# time: O(n)

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        i = answer = 0
        while i < len(columnTitle):
            answer += (1 + ord(columnTitle[-(i+1)]) - ord('A')) * (26**i)
            i += 1
        return answer
