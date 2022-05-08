# link - https://leetcode.com/problems/merge-sorted-array/

# space: O(1)
# time: O(m+n)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        if not nums2: return 
        
        i = j = 0
        k = m
        
        while (i < m or j < n):
            if j == n:
                nums1[k] = nums1[i]
                i += 1
            elif i == m:
                nums1[k] = nums2[j]
                j += 1
            elif nums1[i] < nums2[j]:
                nums1[k] = nums1[i]
                i += 1
            elif nums1[i] >= nums2[j]:
                nums1[k] = nums2[j]
                j += 1
                
            k = (k+1) % (m+n)
        
        nums1[:n], nums1[n:] = nums1[m:], nums1[:m]
