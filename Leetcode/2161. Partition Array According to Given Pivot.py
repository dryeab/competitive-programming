
# Link - https://leetcode.com/problems/partition-array-according-to-given-pivot/

# Space: O(n)
# Time: O(n)

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        cur, answer = 0, [0]*len(nums)
        
        for op in [pivot.__gt__, pivot.__eq__, pivot.__lt__]:
            for i in range(len(nums)):
                if op(nums[i]):
                    answer[cur] = nums[i]
                    cur += 1
                    
        return answer