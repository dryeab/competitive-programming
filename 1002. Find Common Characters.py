# link - https://leetcode.com/problems/find-common-characters/

# : n - len(words) : m - average of len(word[i]) : 
# space: O(n*m)
# time: O(n*m)

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        ans = []
        count = [Counter(word) for word in words[1:]]

        for char in words[0]:
            all = True
            for c in count:
                if c[char] > 0:
                    c[char] -= 1
                else:
                    all = False
                    break;
            if all:
                ans.append(char)
        return ans
                
        
