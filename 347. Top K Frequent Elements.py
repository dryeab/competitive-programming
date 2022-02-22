# link - https://leetcode.com/problems/top-k-frequent-elements/

# space: O(n)
# time: O(nlog(n))

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return list(map(lambda x: x[0], Counter(nums).most_common()))[:k]

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap = list(map(lambda x: (-x[1], x[0]), Counter(nums).items()))
        heapq.heapify(heap)
        return list(map(lambda x: x[1], heapq.nsmallest(k, heap)))
