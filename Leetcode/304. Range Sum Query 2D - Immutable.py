# link - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        for row in matrix:
            sum = 0
            for i in range(len(row)):
                sum += row[i]
                row[i] = sum
                
        self.matrix = matrix 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        matrix = self.matrix
        
        sum = 0
        for i in range(row1, row2+1):
            rem = matrix[i][col1]
            if col1:
                rem -= matrix[i][col1-1]
            sum += (matrix[i][col2] - matrix[i][col1]) + rem
            
        return sum
