
# link - https://leetcode.com/problems/contains-duplicate-ii/

# space: O(k)
# time: O(n)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        i = 0
        count = Counter(nums[:min(len(nums), k+1)])
        
        while (i < len(nums)):
            if count[nums[i]] > 1:
                return True
            
            count[nums[i]] -= 1
            if count[nums[i]] == 0:
                count.pop(nums[i])
            
            i += 1
            
            if i + k < len(nums):
                count[nums[i + k]] += 1
                
        return False
