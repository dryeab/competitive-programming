class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        original = nums.copy()
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
        
        result = []
        for i in original:
            result.append(nums.index(i))
        
        return result
        
