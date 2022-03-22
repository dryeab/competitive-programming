
# Link - https://leetcode.com/problems/partition-labels/

# Space: O(n)
# Time: O(n)

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        index = {char: [-1, -1] for char in s}
        
        for i in range(len(s)):
            if index[s[i]][0] == -1:
                index[s[i]] = [i, i]
            else:
                index[s[i]][1] = i
        
        
        answer = []
        j = length = 0
        
        for i in range(len(s)):
            
            length += 1
            
            j = max(index[s[i]][1], j)
            
            if i == j:
                answer.append(length)
                j = length = 0
        
        return answer