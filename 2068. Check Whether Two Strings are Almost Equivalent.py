
# link - https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

# space: O(n + m)
# time: O(n + m)

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        count1, count2 = Counter(word1), Counter(word2)
        for i in range(ord('a'), ord('z')+1):
            char = chr(i)
            if abs(count1[char]-count2[char]) > 3:
                return False
        return True
