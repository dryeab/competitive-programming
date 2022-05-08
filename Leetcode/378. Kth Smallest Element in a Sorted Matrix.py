
# Link - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Solution 1 (heap)
    # Space: O(n)
    # Time: O(n + k*log(k))

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = [(list[0], i, 0) for i, list in enumerate(matrix)]
        
        for _ in range(k-1):
            
            val = heapq.heappop(heap)
            
            if val[2] < len(matrix) - 1:
                heapq.heappush(heap, (matrix[val[1]][val[2]+1], val[1], val[2]+1))
        
        return heapq.heappop(heap)[0]