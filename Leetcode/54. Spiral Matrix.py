
# link - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        i = j = 0

        row, col = len(matrix), len(matrix[0])
        is_row, dxn = True, 1

        ans = []

        while (row > 0 and col > 0):
            if is_row:
                temp = col
                while (temp > 0):
                    ans.append(matrix[i][j])
                    j += dxn
                    temp -= 1
                j -= dxn
                row -= 1

                i += dxn
            else:
                temp = row
                while (temp > 0):
                    ans.append(matrix[i][j])
                    i += dxn
                    temp -= 1
                i -= dxn
                col -= 1
                
                j += -dxn
                dxn = -dxn
                

            is_row = not is_row

        return ans
