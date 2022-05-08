
# Link - https://leetcode.com/problems/top-k-frequent-elements/

# Space: O(n)
# Time: O(n*log(k))

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        heap, count = [], Counter(nums)
        
        for num in count:
            heapq.heappush(heap, (count[num], num))
            while len(heap) > k:
                heapq.heappop(heap)
        
        return map(lambda x: x[1], heap)