
# link - https://leetcode.com/problems/kth-largest-element-in-an-array/

# space: O(1)
# time: O(nlog(n))

# solution 1

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x: -x, nums))
        heapq.heapify(nums)
        for i in range(k):
            val = heapq.heappop(nums)
        return -val
      
# solution 2
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
