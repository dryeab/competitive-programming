# link - https://leetcode.com/problems/intersection-of-two-arrays/

# space: O(n)
# time: O(n)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))
        
