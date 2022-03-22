
# Link - https://leetcode.com/problems/partition-labels/

# Space: O(n)
# Time: O(n)

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        index = Counter()
        for i in range(len(s)):
            index[s[i]] = i
        
        M, length, answer = 0, 0, [] # max index, length so far, answer
        
        for i in range(len(s)):
            
            length += 1
            
            M = max(index[s[i]], M)
            
            if i == M:
                answer.append(length)
                M = length = 0
        
        return answer