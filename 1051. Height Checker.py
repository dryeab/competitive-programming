# link - https://leetcode.com/problems/height-checker/

# space: O(n)
# time: O(nlog(n))

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        expected = sorted(heights)
        ans = 0
        
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                ans += 1
        
        return ans
        
