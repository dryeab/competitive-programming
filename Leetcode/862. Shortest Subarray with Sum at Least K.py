# link - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:

        sum_so_far = start = 0
        store = deque()
        ans = float('inf')
        
        for end in range(len(nums)):
            sum_so_far += nums[end]

            if sum_so_far <= 0:
                start = end + 1
                sum_so_far = 0 
                store.clear()
                continue
            
            while (len(store) and store[-1][1] >= sum_so_far):
                store.pop()
            store.append((end, sum_so_far))
            
            if sum_so_far >= k:
                while len(store) and (sum_so_far - store[0][1]) >= k:
                    start = store.popleft()[0] + 1
                ans = min(ans, end - start + 1)
        
        return ans if ans != float('inf') else -1
