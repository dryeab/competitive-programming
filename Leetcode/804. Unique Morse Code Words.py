# https://leetcode.com/problems/unique-morse-code-words/
# Time: O(N)
# SoaceL O(N)

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        transformation = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                          "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        store = set()
        for word in words:
            tr = ""
            for char in word:
                tr += transformation[ord(char) - ord('a')]
            store.add(tr)

        return len(store)
