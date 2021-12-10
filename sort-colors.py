class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def selection_sort(arr):
            for i in range(len(arr)):
                minimum = i
                j = i + 1
                while (j < len(arr)):
                    if arr[j] < arr[minimum]:
                        minimum = j
                    j += 1
                arr[minimum], arr[i] = arr[i], arr[minimum]
    
            return arr
        selection_sort(nums)
        return nums
