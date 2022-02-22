# link - https://leetcode.com/problems/top-k-frequent-elements/

# space: O(n)
# time: O(nlog(n))

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return list(map(lambda x: x[0], Counter(nums).most_common()))[:k]
