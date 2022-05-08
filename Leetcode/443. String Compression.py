
# link - https://leetcode.com/problems/string-compression/

# space: O(1)
# time: O(n)

class Solution:
    def compress(self, chars: List[str]) -> int:
        
        i = j = ans = 0
        
        while (j <= len(chars)):
            if j == len(chars) or chars[i] != chars[j]:
                
                chars[ans] = chars[i]
                ans += 1
                
                if j - i != 1:
                    rep = str(j-i)
                    for k in range(len(rep)):
                        chars[ans] = rep[k]
                        ans += 1
                i = j
            j += 1
        
        return ans
