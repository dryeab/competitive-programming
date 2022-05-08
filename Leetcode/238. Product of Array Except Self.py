
# link - https://leetcode.com/problems/product-of-array-except-self/

# space: O(n)
# time: O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod, i, pp = 1, len(nums) - 1, [None] * len(nums)
        while (i >= 0):
            pp[i] = prod
            prod *= nums[i]
            i -= 1
        
        prod, answer = 1, [None] * len(nums)
        for i in range(len(nums)):
            answer[i] = prod * pp[i]
            prod *= nums[i]
        return answer     
