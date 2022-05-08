
# link - https://leetcode.com/problems/count-number-of-nice-subarrays/

# space: O(1)
# time: O(n)

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        ans = temp = n = i = j = 0
        
        while j <= len(nums):
            
            if j < len(nums):
                n += ([0,1][nums[j] % 2])
            
            if n > k or (j == len(nums) and n == k):
                
                old_i = i
                
                while (i <= j and n > k) or (j == len(nums) and n == k):
                    n -= [0, 1][nums[i]%2]
                    i += 1
                    
                ans += temp * (i-old_i)
                temp = 0
                
            if n == k:
                temp += 1
            
            j += 1
        
        return ans
