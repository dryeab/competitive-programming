import random

"""

a[i] -> a[j] : j > i

"""

for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))

    ans = [i + 1 for i in range(n)]

    ok = True
    for i in range(n):
        if (i - 1 >= 0 and s[i-1] == s[i]):
            ok = False
            break
        elif (i + 1 < n and s[i] == s[i+1]):
            pass
        else:
            