# link - https://leetcode.com/problems/frequency-of-the-most-frequent-element/


class Solution:
    def maxFrequency(self, nums, k: int) -> int:
        
        nums = sorted(nums)


        def helper(nums):
            result = {}
            for i in range(len(nums)):
                result[nums[i]] = []
                for j in range(i-1, -1, -1):
                    result[nums[i]].append((nums[i]-nums[j]))
            return result


        diff = helper(nums)

        def counter(values, k=k):
            count = 0
            for i in values:
                if i <= k:
                    count += 1
                    k -= count
            return count
        m = 0
        n = float('inf')
        for i, j in diff.items():
            c = counter(j)
            if c > m:
                m = c
                n = i

            m = max(m, c)

        from collections import Counter

        freq = Counter(nums)
        
        return c + freq[n] if c != 0 else 1
