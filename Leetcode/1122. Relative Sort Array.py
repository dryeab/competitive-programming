# link - https://leetcode.com/problems/relative-sort-array/

# space: O(n)
# time: O(n)

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        count = Counter(arr1)
        
        ans = []
        j = 0
        
        for _, val in enumerate(arr2):
            while (count[val] != 0):
                ans.append(val)
                count[val] -= 1
                j += 1
        
        temp = []
        for _, val in enumerate(arr1):
            if count[val] != 0:
                temp.append(val)
                count[val] -= 1
        
        return ans + sorted(temp)
        
            
