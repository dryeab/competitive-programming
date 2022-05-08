# link - https://leetcode.com/problems/third-maximum-number/

# space: O(1)
# time: O(n)

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ans = [float('-inf')] * 3
        for num in nums:
            if num > ans[0] and num not in ans:
                j, ans[0] = 1, num
                while (j < 3 and ans[j] < ans[j-1]):
                    ans[j], ans[j-1] = ans[j-1], ans[j]
                    j += 1
        return ans[0] if ans[0] != float('-inf') else ans[-1]
        
        
