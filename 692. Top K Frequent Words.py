# link - https://leetcode.com/problems/top-k-frequent-words/

# space: O(1)
# time: O(n + klog(n))

# solution 1

import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = list(map(lambda x: (-x[1], x[0]), Counter(words).items()))
        heapq.heapify(heap)
        return map(lambda x: x[1], [heapq.heappop(heap) for _ in range(k)])

# solution 2

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return map(lambda x: x[1], sorted(map(lambda x: (-x[1], x[0]), Counter(words).items()))[:k])
