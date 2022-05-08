
# link - https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i in "+*/-":
                x, y = stack.pop(), stack.pop()
                stack.append(int(eval(f"{y} {i} {x}")))
            else:
                stack.append(i)
                
        return stack.pop()
