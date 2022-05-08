
# link - https://leetcode.com/problems/reverse-words-in-a-string/

# space: O(n)
# time: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        
        s, answer = s.strip(), []
        i = j = len(s) - 1
                
        while (i >= -1):
            if i==-1 or s[i].isspace():
                answer.append(s[i+1:j+1])
                while i > 0 and s[i].isspace():
                    i -= 1
                j = i
            i -= 1

        return " ".join(answer)
