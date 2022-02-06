# link - https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# space: O(1)
# time: O(n)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = j = k = 0
        while (k <= len(nums)):
            if k == len(nums) or nums[k] != nums[j]:
                rep = min(2, k-j)
                while rep:
                    nums[i] = nums[j]
                    i += 1
                    rep -= 1
                j = k
            k += 1
        return i
