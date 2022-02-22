# link - https://leetcode.com/problems/top-k-frequent-words/

# space: O(1)
# time: O(nlog(n))

import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return map(lambda x: x[1], sorted(map(lambda x: (-x[1], x[0]), Counter(words).items()))[:k])
