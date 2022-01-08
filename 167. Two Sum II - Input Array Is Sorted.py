# link - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# space: O(1)
# time: O(n)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while (i <= j):
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            if numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
                
