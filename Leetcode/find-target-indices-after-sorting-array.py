class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        result = []
        def selection_sort(arr):
            for i in range(len(arr)):
                print(arr)
                minimum = i
                j = i + 1
                while (j < len(arr)):
                    if arr[j] < arr[minimum]:
                        minimum = j
                    j += 1
                arr[minimum], arr[i] = arr[i], arr[minimum]

            return arr
        selection_sort(nums)
        for i in range(len(nums)):
            if nums[i]  == target:
                result.append(i)
                
        return result
