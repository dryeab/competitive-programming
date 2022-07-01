n, t = map(int, input().split())

ans = 10**(n-1)

if ans % t:
    ans += t - (ans % t)

print(ans if len(str(ans)) == n else -1)