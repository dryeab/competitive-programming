# link - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/submissions/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = sorted([int(x) for x in nums])
        return str(nums[-k])
        
