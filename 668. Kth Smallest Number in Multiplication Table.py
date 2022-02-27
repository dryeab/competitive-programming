
# Link - https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

# Space: O(1)
# Time: O((m+n)*log(m*n))

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        def count(mid): # number of matrix elements with (element <= mid)
            ans, col = 0, n
            for row in range(1, m+1):
                while col and row*col > mid:
                    col -= 1
                ans += col
            return ans
        
        left, right = 1, m*n
        while left < right:
            mid = (left + right)//2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        
        return left