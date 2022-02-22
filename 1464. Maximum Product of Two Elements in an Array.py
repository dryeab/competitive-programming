# link - https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/


# solution 1

# space: O(1)
# time: O(n)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        x, y = float('-inf'), float('-inf')
        
        for num in nums:
            if num >= y:
                x, y = y, num
            elif num > x:
                x = num
                
        return (x-1)*(y-1)

    
# Solution 2

# space: O(n)
# time: O(n)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        return (-heapq.heappop(nums)- 1) * (-heapq.heappop(nums) - 1)
      
      
# solution 3

# space: O(1)
# time: O(nlog(n))

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)

      
