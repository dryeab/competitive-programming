
# Link - https://leetcode.com/problems/flood-fill/

# Space: O(m * n)
# Time: O(m * n)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        if image[sr][sc] == newColor:
            return image
        
        m, n = len(image), len(image[0])
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        FOUR_DIR = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        def dfs(r, c, color):
            
            if inBound(r, c) and image[r][c] == color:
                image[r][c] = newColor

                for DIR in FOUR_DIR:
                    dfs(r + DIR[0], c + DIR[1], color)
        
        dfs(sr, sc, image[sr][sc])
        
        return image