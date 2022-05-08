# link - https://leetcode.com/problems/valid-anagram/

# space: O(n + m)
# time: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
