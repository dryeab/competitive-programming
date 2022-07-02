from collections import defaultdict
from heapq import *

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    if u != v:
        graph[u].append(v)
        graph[v].append(u)

visited = set()
heap = [1]
path = []

while heap and len(path) < n:

    cur = heappop(heap)
    if cur in visited:
        continue

    visited.add(cur)
    path.append(cur)

    for neighbor in graph[cur]:
        if neighbor not in visited:
            heappush(heap, neighbor)

print(*path)
