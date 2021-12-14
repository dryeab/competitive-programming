# link -  https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        ans = sorted(s.split(), key=lambda x: x[-1])
        return " ".join([x[:-1] for x in ans])
        

