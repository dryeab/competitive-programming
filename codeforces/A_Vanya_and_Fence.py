n, h = map(int, input().split())
a = list(map(int, input().split()))

res = 0
for x in a:
    if x > h:
        res += 2
    else:
        res += 1

print(res)
