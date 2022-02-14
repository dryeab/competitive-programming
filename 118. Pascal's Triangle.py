# link - https://leetcode.com/problems/pascals-triangle/

# space: -
# time: -

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]
        for i in range(numRows-1):
            last = answer[-1]
            next = [1] * (len(last)+1)
            for i in range(1, len(last)):
                next[i] = last[i] + last[i-1]
            answer.append(next)
        return answer
