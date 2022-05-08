
# link - https://leetcode.com/problems/remove-k-digits

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        store = {}
        mono_stack = []
            
        for i, val in enumerate(num):
            while (len(mono_stack) and num[mono_stack[-1]] > val):
                store[mono_stack.pop()] = i
            mono_stack.append(i)
            store[i] = -1

        start , ans = 0, ''
        v = len(num) - k
        
        while start < len(num) and len(ans) < v:
            while (store[start] != -1 and k > 0):
                temp = store[start]
                if (len(ans) + len(num) - temp) >= v:
                    k -= (temp - start)
                    start = temp
                else: break;
            
            ans += num[start]
            start += 1
            
        return str(int(ans)) if ans else "0"
