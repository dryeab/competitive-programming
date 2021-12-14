# link -  https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        result = [""]*10
        splited = s.split()
        for i in splited:
            result[int(i[-1])] = i[:-1]            
        return " ".join(result).strip()
