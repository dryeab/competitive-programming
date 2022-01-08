# link - https://leetcode.com/problems/add-binary/

# space: O(x) 
# time: O(x) 
# : x - length of the longest of the two

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        i, j = len(a)-1, len(b)-1
        
        ans = []
        
        while (i >= 0 and j >= 0):
            temp = int(a[i]) + int(b[j]) + carry
            sum = temp % 2
            carry = temp // 2
            ans.append(str(sum))
            i -= 1
            j -= 1
            
        while (j >= 0):
            temp = int(b[j]) + carry
            sum = temp % 2
            carry = 0 if temp < 2 else 1
            ans.append(str(sum))
            j -= 1
        
        while (i >= 0):
            temp = int(a[i]) + carry
            sum = temp % 2
            carry = 0 if temp < 2 else 1
            ans.append(str(sum))
            i -= 1
           
        if carry:
            ans.append(str(carry))
        
        
        return "".join(ans[::-1])

