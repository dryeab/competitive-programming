
# link - https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        nums.sort()
        
        store = set()
        ans = 0
        var = -1 
        
        for i in nums:
            var = max(var, i)
            if i in store:
                while (var in store):
                    var += 1
                ans += (var - i)
            store.add(var)
        
        return ans
            
