

from functools import reduce

for _ in range(int(input())):

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    b = 30
    while b >= 0 and k > 0:

        cnt = sum(((x >> b) & 1) == 0 for x in a)

        if cnt <= k:
            for i in range(n):
                a[i] = a[i] | (1 << b)
            k -= cnt

        b -= 1

    print(reduce(lambda a, b: a & b, a))
