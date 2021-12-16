
# link - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for i in s:
            if i == ')':
                temp = ""
                while ((x:=stack.pop()) != '('):
                    temp += x
                for j in temp:
                    stack.append(j)
            else:
                stack.append(i)
        
        return "".join(stack)

                
