for _ in range(int(input())):

    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    i, j, total, ans = 0, 0, 0, -1
    # found = False

    while j < n:
        total += a[j]
        while total > s:
            total -= a[i]
            i += 1
        if total == s:
            ans = max(ans, j-i+1)

        j += 1

    if ans == -1:
        print(ans)
    else:
        print(n - ans)
