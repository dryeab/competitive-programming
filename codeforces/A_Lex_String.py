for _ in range(int(input())):

    n, m, k = [int(x) for x in input().split()]
    a = sorted(list(input()))
    b = sorted(list(input()))

    c = []

    i = j = oa = ob = 0

    while (i < n and j < m):

        if oa < k and (ob >= k or a[i] < b[j]):
            c.append(a[i])
            oa += 1
            ob = 0
            i += 1

        elif ob < k and (oa >= k or b[j] < a[i]):
            c.append(b[j])
            ob += 1
            oa = 0
            j += 1

    print("".join(c))