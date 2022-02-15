# link - https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

# space: O(1)
# time: O(nlog(n))

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        answer, i = 0, len(cost) - 1
        
        while i >= 0:
            answer += cost[i]
            i -= 1
            if i >= 0:
                answer += cost[i]
            i -= 2
        return answer
