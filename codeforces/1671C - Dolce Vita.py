for _ in range(int(input())):

    n, x = [int(x) for x in input().split()]

    a = [int(x) for x in input().split()]

    a.sort()

    sum = 0
    ans = 0

    for i in range(n):

        sum += a[i]

        if sum > x:
            break

        ans += (x - sum)//(i + 1) + 1

    print(ans)
