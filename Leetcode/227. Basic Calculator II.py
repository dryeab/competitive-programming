
# link - https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:

        ops = ['*', '/', '-', '+']
        store, i, j = [], 0, 0

        while (j < len(s)):

            if (j + 1 == len(s)) or (s[j] in ops):
                if j + 1 == len(s):
                    j += 1
                num = int(s[i:j].strip())

                if len(store) and store[-1] in ops[:2]:
                    op = store.pop()
                    if op == '*':
                        store[-1] *= num
                    elif op == '/':
                        store[-1] //= num
                else:
                    store.append(num)

                if j < len(s) and s[j] in ops:
                    store.append(s[j])
                i = j + 1

            j += 1

        ans, i = store[0], 1
        while (i < len(store)):
            if store[i] == '+':
                ans += store[i+1]
            elif store[i] == '-':
                ans -= store[i+1]
            i += 2
        return ans
