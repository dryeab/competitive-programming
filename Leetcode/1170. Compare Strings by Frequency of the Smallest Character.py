
# Link - https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

# Solution 1
  # Space: O(1)
  # Time: ~

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def f(word):
            return word.count(min(word))
        
        for i, word in enumerate(words):
            words[i] = f(word)
        
        words.sort()
        
        ans = []
        for query in queries:
            
            q = f(query)
            
            left, right = 0, len(words) - 1
            while left < right:
                mid = (left + right)//2
                if words[mid] > q:
                    right = mid
                else:
                    left = mid + 1
                    
            if (left == len(words) - 1) and (q >= words[left]):
                left += 1
                
            ans.append(len(words) - left)
            
        return ans

# Solution 2
  # Space: O(1)
  # Time: O(n*m)

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def f(word): return word.count(min(word))
        
        for i, word in enumerate(words):
            words[i] = f(word)
        
        ans = []
        
        for query in queries:
            count, q = 0, f(query)
            for word in words:
                if q < word:
                    count += 1
            ans.append(count)
        return ans
