from collections import defaultdict


def solve(i, count):
    ans = 0
    for x in count:
        if count[x] >= i:
            ans += i
    return ans


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count = defaultdict(int)

    for x in a:
        count[x] += 1

    freqs = set()
    for x in a:
        freqs.add(count[x])

    print(n - max(solve(i, count) for i in freqs))
