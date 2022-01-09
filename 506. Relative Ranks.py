# link - https://leetcode.com/problems/relative-ranks/

# space: O(n)
# time: O(n)

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        
        index = {}
        for i in range(len(score)):
            index[score[i]] = i
        
        answer = [None] * len(score)
        for i, val in enumerate(sorted_score):
            if i == 0:
                level = "Gold Medal"
            elif i == 1:
                level = "Silver Medal"
            elif i == 2:
                level = "Bronze Medal"
            else:
                level = f"{i+1}"
            answer[index[val]] = level
        
        return answer
            
        
