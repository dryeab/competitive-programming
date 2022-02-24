
# Link - https://leetcode.com/problems/kth-largest-element-in-an-array/

# Solution 1
    # Space: O(k)
    # Time: O(n*log(k))

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if heap[0] < num:
                    heapq.heappushpop(heap, num)
        
        return heap[0]
      
# Solution 2
    # Space: O(1)
    # Time: O(n*log(n))
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
