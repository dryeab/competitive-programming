
# link - https://leetcode.com/problems/arithmetic-subarrays

class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: List[int]) -> List[bool]:
        
        def is_arithmetic(nums):
            d = nums[0] - nums[1]
            for i in range(1, len(nums)):
                if nums[i-1] - nums[i] != d:
                    return False
            return True
        
        ans = [False] * len(l)

        for i in range(len(l)):
            temp = nums[l[i]: r[i]+1]
            temp.sort()
            if is_arithmetic(temp):
                ans[i] = True
        
        return ans
