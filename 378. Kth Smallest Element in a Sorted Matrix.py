

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = [(lst[0], i, 0) for i, lst in enumerate(matrix)]
        
        heapq.heapify(heap)
        
        for _ in range(k):
            
            val = heapq.heappop(heap)
            
            if val[2] < len(matrix[val[1]]) - 1:
                heapq.heappush(heap, (matrix[val[1]][val[2] + 1], val[1], val[2] + 1))
        
        return val[0]
