for _ in range(int(input())):

    n = int(input())
    p = list(map(int, input().split()))
    q = []

    if len(p) == 1:
        print(-1)
        continue

    store = set(p)
    mark = True

    for i in range(n):
        m = n+1
        for val in store:
            if val != p[i]:
                m = min(m, val)

        if m == n + 1:
            m = p[i]

        store.remove(m)
        q.append(str(m))

    if int(q[-1]) == p[-1]:
        q[-1], q[-2] = q[-2], q[-1]

    print(" ".join(q))
