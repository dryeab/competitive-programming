
# Link - https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/


# Solution 1

# Space: O(n)
# Time: O(n*log(n))

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        nums = [(num, i) for i, num in enumerate(nums)]
        
        ans = sorted(sorted(nums)[-k:], key=lambda x: x[1])
        
        return map(lambda x: x[0], ans)

      
# Solution 2

# Space: O(n)
# Time: O(n + k*log(n))

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        nums = [(-num, i) for i, num in enumerate(nums)]
        heapq.heapify(nums)
        
        hp = []
        for _ in range(k):
            heapq.heappush(hp, heapq.heappop(nums)[::-1])
            
        return [-heapq.heappop(hp)[1] for _ in range(k)]
