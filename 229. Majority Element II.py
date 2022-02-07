
# link - https://leetcode.com/problems/majority-element-ii/

# space: O(n)
# time: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        c = Counter(nums)
        ans = set()
        
        for i in c:
            if c[i] > len(nums)//3:
                ans.add(i)
        
        return list(ans)
            
        
