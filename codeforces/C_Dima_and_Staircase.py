n = int(input())
a = list(map(int, input().split()))

ps = [a[0]]
for i in range(1, n):
    ps.append(max(ps[-1], a[i]))

m = int(input())

for _ in range(m):
    w, h = map(int, input().split())
    m = max(ps[w-1], ps[0])
    print(m)
    ps[0] = m + h
