class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i = j = 0
        while i < len(nums1) or j < len(nums2):
            if i < len(nums1) and (j >= len(nums2) or (nums1[i] < nums2[j])):
                merged.append(nums1[i])
                i += 1
            elif j < len(nums2):
                    merged.append(nums2[j])
                    j += 1
                    
        if len(merged) % 2: return merged[len(merged)//2]
        return (merged[len(merged)//2] + merged[len(merged)//2-1])/2