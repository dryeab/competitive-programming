
# Link - https://leetcode.com/problems/kth-largest-element-in-an-array/

# Solution 1
    # Space: O(k)
    # Time: O(n*log(k))

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        
        for num in nums:
            
            heapq.heappush(heap, num)
            
            while len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]
      
# Solution 2
    # Space: O(1)
    # Time: O(n*log(n))
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
