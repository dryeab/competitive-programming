# link - https://leetcode.com/problems/shortest-completing-word/

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        c = Counter(licensePlate.lower())
        ans = "                                          "
        for word in words:
            if len(ans) > len(word):
                cw = Counter(word.lower())
                
                state = True
                for i in c:
                    if i.isalpha() and cw[i] < c[i]:
                        state = False
                if state:
                    ans = word
        return ans
                    
        
