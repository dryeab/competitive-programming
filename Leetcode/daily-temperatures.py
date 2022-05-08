

# link - https://leetcode.com/problems/daily-temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = {}

        for i in range(len(temperatures)):
            if len(stack) and (temperatures[stack[-1]] < temperatures[i]):
                while (len(stack) and temperatures[stack[-1]] < temperatures[i]):
                    temp = stack.pop()
                    ans[temp] = i - temp
                stack.append(i)
            else:
                stack.append(i)
        
        while (len(stack)):
            ans[stack.pop()] = 0
        
        for i in ans:
            temperatures[i] = ans[i]

        return temperatures
