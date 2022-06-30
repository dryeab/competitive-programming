
from heapq import *

for _ in range(int(input())):
    n = int(input())

    heap, ans, i = [(-n, 1, n)], [0 for _ in range(n + 1)], 1

    while heap:

        _, l, r = heappop(heap)

        if (r - l + 1) % 2:
            mid = (l + r) // 2
        else:
            mid = (l + r - 1) // 2

        ans[mid] = i
        i += 1

        if l <= mid - 1:
            heappush(heap, (-(mid - 1 - l + 1), l, mid - 1))
        if mid + 1 <= r:
            heappush(heap, (-(r - (mid + 1) + 1), mid + 1, r))

    print(*(ans[1:]))
