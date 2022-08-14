# https://codeforces.com/problemset/problem/365/A
# Time: O(N)
# Space: O(1)


n, k = map(int, input().split())

res = 0

for _ in range(n):
    a, digits = input(), set()
    for d in a:
        if 0 <= int(d) <= k:
            digits.add(d)
    res += len(digits) == k + 1

print(res)
