# link - https://leetcode.com/problems/maximize-distance-to-closest-person/

# space: O(1)
# time: O(n)

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        i, j, ans = 0, 0, float('-inf')
        while (j < len(seats)):
            if seats[j] == 1 or (j==len(seats)-1 and seats[j]==0):
                if seats[j] == 0 or seats[i] == 0:
                    ans = max(ans, j-i)
                else:
                    ans = max(ans, (j-i)//2)
                i = j
            j += 1
        return ans
