
# Link - https://leetcode.com/problems/finding-the-users-active-minutes/

# Space: O(n)
# Time: O(n)

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        store = defaultdict(set)
        
        for id, time in logs:
            store[id].add(time)
        
        ans = [0]*k
        for id in store:
            ans[len(store[id]) - 1] += 1
        
        return ans