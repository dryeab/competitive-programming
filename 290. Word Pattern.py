# link - https://leetcode.com/problems/word-pattern/

# space; O(n)
# time: O(n)

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        word_to_pattern = {}
        pattern_to_word = {}
        i = j = k = 0
        
        while (j <= len(s) and k < len(pattern)):
            if j == len(s) or s[j].isspace():
                word = s[i:j]
                if word in word_to_pattern or pattern[k] in pattern_to_word:
                    if pattern[k] in pattern_to_word and pattern_to_word[pattern[k]] != word:
                        return False
                    if word in word_to_pattern and word_to_pattern[word] != pattern[k]:
                        return False
                else:
                    pattern_to_word[pattern[k]] = word
                    word_to_pattern[word] = pattern[k]
                
                i = j+1
                k += 1
                
            j += 1
        
        return j == len(s) + 1 and k == len(pattern)
                
