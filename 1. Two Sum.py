
# link - https://leetcode.com/problems/two-sum/

# space: O(n)
# time: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            if target - nums[i] in store:
                return [store[target-nums[i]], i]
            store[nums[i]] = i
            

# space: O(1)
# time: O(n**2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    
