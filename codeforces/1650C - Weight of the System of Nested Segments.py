from heapq import heappop, heappush

for _ in range(int(input())):

    input()

    n, m = [int(x) for x in input().split()]

    heap = []

    for i in range(m):

        x, w = [int(x) for x in input().split()]

        heappush(heap, (w, x, i+1))

    weight = 0
    segment = []

    for __ in range(2*n):
        w, x, i = heappop(heap)
        weight += w
        segment.append((x, i))

    segment.sort()

    print(weight)

    l, r = 0, len(segment) - 1
    while l <= r:
        print(segment[l][1], segment[r][1])
        l += 1
        r -= 1

    print()
