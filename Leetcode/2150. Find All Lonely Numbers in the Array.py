# link - https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

# space: O(n)
# time: O(n)

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        ans, count = [], Counter(nums)
        for i in count:
            if count[i] == 1 and not (count[i-1] or count[i+1]):
                ans.append(i)
        return ans
