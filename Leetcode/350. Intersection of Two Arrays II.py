# link - https://leetcode.com/problems/intersection-of-two-arrays-ii/

# space: O(m+n)
# time: O(m)
# : m = len(nums1), n = len(nums2)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        c1, c2 = Counter(nums1), Counter(nums2)
        
        ans = []
        for i in c1:
            ans += [i]*min(c1[i], c2[i])
        
        return ans
        
