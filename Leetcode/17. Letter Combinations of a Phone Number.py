
# Link - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Space: O(4^n)
# Time: O(4^n)

# Iterative
class Solution:

    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        mapping = ["", "", "abc", "def", "ghi",
                   "jkl", "mno", "pqrs", "tuv", "wxyz"]

        ans = [""]

        for digit in digits:
            new_ans = []
            for char in mapping[int(digit)]:
                for each in ans:
                    new_ans.append(each + char)
            ans = new_ans

        return ans


# Recursive
mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


class Solution:

    def letterCombinations(self, digits: str, i=0) -> List[str]:

        if i == len(digits):
            return []

        digit = int(digits[i])

        if i == len(digits) - 1:
            return list(mapping[digit])

        ans = []

        for val in self.letterCombinations(digits, i+1):
            for char in list(mapping[digit]):
                ans.append(char + val)

        return ans
