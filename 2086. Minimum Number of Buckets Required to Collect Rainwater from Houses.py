
# Link - https://leetcode.com/problems/minimum-number-of-buckets-required-to-collect-rainwater-from-houses/

# Space: O(n)
# Time: O(n)

class Solution:
    def minimumBuckets(self, street: str) -> int:
        
        street = list(street)
        
        for i in range(len(street)):
            
            if street[i] == 'H':
                
                if i and street[i-1] == 'B': # already have bucket
                    continue
                    
                if i + 1 < len(street) and street[i+1] == '.':
                    street[i+1] = 'B'
                elif i and street[i-1] == '.':
                    street[i-1] = 'B'
                else: # impossible case
                    return -1
        
        return street.count('B')