n = int(input())
a = list(map(int, input().split()))

ans = cur = 1

for i in range(1, n):
    if a[i] <= a[i-1]:
        ans = max(ans, cur)
        cur = 0
    cur += 1

print(max(cur, ans))
