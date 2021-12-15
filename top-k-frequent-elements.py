
# link - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        counter = Counter(nums)
        s = sorted([(y, x) for x, y in counter.items()])

        return ([x for _, x in s[-k:]])
