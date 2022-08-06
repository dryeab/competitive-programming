# https://codeforces.com/contest/20/problem/C
# Time:
# Space:

import sys
from heapq import *
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, w = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append((b, w))
    graph[b].append((a, w))

heap, parent = [(0, 0, n)], [-1] * n

while heap:

    dist, node, p = heappop(heap)

    if parent[node] == -1:

        parent[node] = p

        if node == n:
            break

        for neighbor, w in graph[node]:
            if parent[neighbor] == -1:
                heappush(heap, (dist + w, neighbor, node))

if parent[n - 1] == -1:
    print(-1)
else:
    res, p = [], n - 1
    while p != n:
        res.append(p + 1)
        p = parent[p]
    print(*res[::-1])
