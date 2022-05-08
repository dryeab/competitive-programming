# link - https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mat = [(row.count(1), i, row) for i, row in enumerate(mat)]
        heapq.heapify(mat)
        return [heapq.heappop(mat)[1] for _ in range(k)]
