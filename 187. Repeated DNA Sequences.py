
# Link - https://leetcode.com/problems/repeated-dna-sequences/

# Space: O(n)
# Time: O(n)

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        answer = defaultdict(int)
        
        for i in range(len(s) - 9):
            answer[s[i:i+10]] += 1
        
        return [seq for seq in answer if answer[seq] > 1]