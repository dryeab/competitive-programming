
# Link - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

# Space: O(1)
# Time: O(log(n))

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        low, high = 0, len(letters) - 1
        while low < high:
            mid = low + ((high - low) >> 1)
            if letters[mid] > target:
                high = mid
            else:
                low = mid + 1
                
        return letters[high] if letters[-1] > target else letters[0]
