class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        n = len(words)
        
        i, res = 0, []
        
        while i < n:
            
            l, i, cur = len(words[i]), i + 1, [words[i]]
            while i < n and l + 1 + len(words[i]) <= maxWidth:
                cur.append(' ' + words[i])
                l += len(words[i]) + 1
                i += 1
            
            
            l = maxWidth - l
            
            if i == n or len(cur) == 1: # left-justified
                res.append(''.join(cur) + (' ' * l))
            else:
                each, rem = l // (len(cur) - 1), l % (len(cur) - 1)
                for j in range(len(cur) - 1):
                    cur[j] = cur[j] + (' ' * each) + (' ' * min(rem, 1))
                    if rem: rem -= 1
                res.append(''.join(cur))
        
        return res