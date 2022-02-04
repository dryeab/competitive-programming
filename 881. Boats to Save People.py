
# link - https://leetcode.com/problems/boats-to-save-people/

# space: O(1)
# time: O(nlog(n))

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        
        i, j, ans = 0, len(people) - 1, 0
        while (i <= j):
            if i == j or people[i] + people[j] <= limit:
                i += 1
            j -= 1
            ans += 1
        
        return ans
