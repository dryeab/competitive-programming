
# Link - https://leetcode.com/problems/can-place-flowers/

# Space: O(1)
# Time: O(n)

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        canPlant = lambda i: (i == 0 or flowerbed[i-1] == 0) and \
                                (i == len(flowerbed) - 1 or flowerbed[i+1] == 0)
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and canPlant(i):
                flowerbed[i], n = 1, n - 1
        
        return n <= 0