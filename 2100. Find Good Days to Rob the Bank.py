
# Link - https://leetcode.com/problems/find-good-days-to-rob-the-bank/

# Space: O(n)
# Time: O(n)

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
        if time >= (len(security) + 1)// 2:
            return []
        
        dp_left = [0]*len(security)
        for i in range(len(security)):
            if i and security[i-1] >= security[i]:
                dp_left[i] = dp_left[i-1] + 1
        
        dp_right = [0]*len(security)
        for j in range(len(security)-2, -1, -1):
            if security[j] <= security[j+1]:
                dp_right[j] = dp_right[j+1] + 1
        
        answer = []
        for i in range(time, len(security)-time):
            if dp_right[i] >= time and dp_left[i] >= time:
                answer.append(i)
        
        return answer
        