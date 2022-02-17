
# link - https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

# space: O(1)
# time: O(n**2)

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        
        ans = float('-inf')
        
        firstLen, secondLen = min(firstLen, secondLen), max(firstLen, secondLen)
        
        sum1 = sum(nums[:firstLen])
        for i in range(len(nums)-firstLen+1):
            
            # all possible scenarios for the subarray
            sum2 = sum(nums[:secondLen])
            for j in range(len(nums)-secondLen+1):
                
                # x1 <= y2 && y1 <= x2
                
                x1, x2 = i, i + firstLen - 1
                y1, y2 = j, j + secondLen - 1
                
                if not (x1 <= y2 and y1 <= x2):
             
                    ans = max(ans, sum1+sum2)

                if j + secondLen < len(nums):
                    sum2 += (nums[j+secondLen] - nums[j])
            
            if i + firstLen < len(nums):
                sum1 += (nums[i+firstLen] - nums[i])
        
        return ans
