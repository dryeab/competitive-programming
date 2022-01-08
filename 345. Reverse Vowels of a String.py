# link - https://leetcode.com/problems/reverse-vowels-of-a-string/

# space: O(n)
# time: O(n)

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        s = list(s)
        
        vowels = 'aeiou'
        i, j = 0, len(s) - 1
        
        while (i < j):
            while i < j and s[i].lower() not in vowels:
                i += 1
            while i < j and s[j].lower() not in vowels:
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
            j -= 1
            i += 1
                
        return "".join(s)
        
