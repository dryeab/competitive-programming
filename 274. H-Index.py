
# link - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse=True)

        cur, i = citations[0], 0

        while (cur >= 0):
            if cur <= i + 1:
                return cur
            
            cur -= 1
            
            if i+1 < len(citations) and cur <= citations[i+1]:
                i += 1
                cur = citations[i]
