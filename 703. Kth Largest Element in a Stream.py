
# Link - https://leetcode.com/problems/kth-largest-element-in-a-stream/

# Space: O(k)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.heap = k, nums
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        for _ in range(len(self.heap)- self.k):
            heapq.heappop(self.heap)
        return self.heap[0]
