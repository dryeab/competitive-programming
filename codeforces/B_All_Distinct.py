from collections import Counter

for _ in range(int(input())):

    n = int(input())
    a = [int(x) for x in input().split()]

    count = Counter(a)

    ans = 0
    for x in count:
        ans += count[x] - 1

    if ans % 2:
        ans += 1

    print(n - ans)
