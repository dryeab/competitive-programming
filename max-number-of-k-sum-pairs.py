# link - https://leetcode.com/problems/max-number-of-k-sum-pairs


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        from collections import Counter
        counter = Counter(nums)

        ans = 0
        for i, j in counter.items():

            if i == k/2:
                ans += j//2
                continue;

            d = k - i
            f = counter.get(d) # frequency
            
            if not f or not j: continue;

            m = min(j, f)
            ans += m

            counter[i] -= m
            counter[d] -= m
        
        return ans
            
