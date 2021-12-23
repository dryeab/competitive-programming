
# link - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        start = end = ans = 0 
        imq = deque()
        dmq = deque()

        while (end < len(nums)):
            end_value = nums[end]

            while len(imq) and (nums[imq[-1]] >= end_value):
                imq.pop()
            imq.append(end)

            while len(dmq) and (nums[dmq[-1]] <= end_value):
                dmq.pop()
            dmq.append(end)

            while (nums[dmq[0]] - nums[imq[0]]) > limit:
                start += 1
                if start > imq[0]:
                    imq.popleft()
                if start > dmq[0]:
                    dmq.popleft()
            
            ans = max(ans, end - start + 1)
            end += 1
            
        return ans
