
# Link - https://leetcode.com/problems/vowels-of-all-substrings/

# Space: O(n)
# Time: O(n)

class Solution:
    def countVowels(self, word: str) -> int:
        
        dp = [0]
        for i, letter in enumerate(word):
            dp.append(dp[-1])
            if letter in {'a', 'e', 'i', 'o', 'u'}:
                dp[-1] += i + 1
        
        return sum(dp)