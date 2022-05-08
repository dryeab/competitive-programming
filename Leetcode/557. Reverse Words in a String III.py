
# link - https://leetcode.com/problems/reverse-words-in-a-string-iii/

# space: O(n)
# time: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split()])
