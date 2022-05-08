
# link - https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

# space: O(1)
# time: O(n)

class Solution:
    def checkString(self, s: str) -> bool:
        b = False
        for i in range(len(s)):
            if s[i] == 'b':
                b = True
            else:
                if b:
                    return False
        return True
