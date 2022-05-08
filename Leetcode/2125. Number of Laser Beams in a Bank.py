
# List - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

# Space: O(1)
# Time: O(n)

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        ans = last = 0
        for i in range(len(bank)):
            count = bank[i].count('1')
            if count:
                ans += count * last
                last = count
        
        return ans