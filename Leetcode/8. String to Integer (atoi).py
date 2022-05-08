
# link - https://leetcode.com/problems/string-to-integer-atoi/

# space: O(1)
# time: O(n)

class Solution:
    def myAtoi(self, s: str) -> int:

        start = end = -1
        firstChar = None
        
        for i in range(len(s)):
            if s[i].isdigit():
                if start == -1:
                    start = i
                end = i
            else:
                if start == - 1 and firstChar == None:
                     if not s[i].isspace():
                        firstChar = s[i]
                else:
                    break;
        
        if start == -1:
            return 0
        
        num = int(s[start:end+1])
        
        if firstChar == '+' or not firstChar:
            answer = num if num < 2**31 - 1 else 2**31 - 1
        elif firstChar == '-':
            answer = -(num if num < 2**31 else 2**31)
        else:
            return 0
        
        return answer
