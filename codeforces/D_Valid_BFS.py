
# https://codeforces.com/problemset/problem/1037/D
# Time: O(V + E)
# Space: O(E)


from collections import deque


n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

a = list(map(int, input().split()))

if a[0] != 1:
    print("NO")
    exit()

q, visited = deque([1]), {1}

ok, i = True, 1

while i < n and q and ok:

    x = q.popleft()

    ys = set()

    for y in graph[x]:
        if y not in visited:
            ys.add(y)
            visited.add(y)

    while ys:
        if a[i] in ys:
            q.append(a[i])
            ys.discard(a[i])
            i += 1
        else:
            ok = False
            break

print("YES" if ok else "NO")
