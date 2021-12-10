class Solution:
    def sortSentence(self, s: str) -> str:
        result = [""]*10
        i = 0
        j = 0
        while (j < len(s)):
            if s[j].isdigit():
                result[int(s[j])] = s[i:j]
                j += 2
                i = j
            else: j += 1
                
        return " ".join(result).strip()
