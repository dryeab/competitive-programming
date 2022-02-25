# Link - https://leetcode.com/problems/peak-index-in-a-mountain-array/

# Space: O(1)
# Time: O(log(n))

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        low, high = 1, len(arr) - 2
        
        while low < high:
            
            mid = (low + high) >> 1
            
            if arr[mid -1] < arr[mid] > arr[mid + 1]:
                return mid
            
            if arr[mid - 1] < arr[mid]:
                low = mid + 1
            else:
                high = mid
        
        return low
