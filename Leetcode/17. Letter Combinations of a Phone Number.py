
# Link - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Space: O(1)
# Time: O(n)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        lowercases, mapper = list(string.ascii_lowercase[::-1]), defaultdict(list)
        
        for i, num in enumerate([3, 3, 3, 3, 3, 4, 3, 4]):
            for _ in range(num):
                mapper[i+2].append(lowercases.pop())
        
        def helper(digits):
            
            if len(digits) == 0:
                return []
            if len(digits) == 1:
                return mapper[int(digits[0])]
            
            ans = []
            for letter in mapper[int(digits[0])]:
                for combination in helper(digits[1:]):
                    ans.append(letter + combination)
            
            return ans
            
        return helper(digits)
            