# link - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while (i < len(s)):
            if s[i].isdigit():
                j = i + 1
                while s[j].isdigit():
                    j += 1
                stack.append(int(s[i:j]))
                i = j
            elif s[i] == ']':
                temp = ''
                while stack[-1] != '[':
                    temp += stack.pop()[::-1]
                stack.pop()  # remove the opening square bracket
                stack[-1] = (stack[-1] * temp[::-1])
                i += 1
            else:
                stack.append(s[i])
                i += 1

        return "".join(stack)
