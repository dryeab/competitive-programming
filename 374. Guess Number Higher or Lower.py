
# lower - https://leetcode.com/problems/guess-number-higher-or-lower/

# space: O(1)
# time: O(log(n))

class Solution:
    def guessNumber(self, n: int) -> int:
        min, max = 1, n
        
        while min != max:
            mid = (min + max)//2
            g = guess(mid)
            if g == 0:
                return mid
            if g == 1:
                min = mid + 1
            else:
                max = mid - 1
                
        return (min + max)//2
        
