
# link - https://leetcode.com/problems/reverse-string/

# space: O(1)
# time: O(n)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]