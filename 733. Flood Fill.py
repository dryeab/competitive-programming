
# Link - https://leetcode.com/problems/flood-fill/

# Space: O(1)
# Time: O()

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        
        DIR = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        # (row, col) :-> left, right, top, bottom
            
        visited = set()
        color = image[sr][sc]
        
        # bounday check
        inBound = lambda y, x: (0 <= y < len(image)) and (0 <= x < len(image[0])) and ((y,x) not in visited)
        
        def dfs(r, c):
            
            visited.add((r,c))

            image[r][c] = newColor
            
            for d in DIR:
                nr, nc = r + d[0], c + d[1]
                if inBound(nr, nc) and image[nr][nc] == color:
                    dfs(nr, nc)
                    
        dfs(sr, sc)
        
        return image