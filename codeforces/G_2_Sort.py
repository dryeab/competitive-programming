for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    i, j = 0, 0

    while j <= n:

        if j == n or (j and a[j-1] >= 2 * a[j]):
            # while j - i + 1 > k:
            #     ans += 1
            #     i += 1
            i = j
        else:
            if j - i + 1 > k:
                ans += 1

        j += 1

    print(ans)
