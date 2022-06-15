def add(s, x):

    h, m = int(s[:2]), int(s[-2:])

    m += x
    h += m // 60

    m %= 60
    h %= 24

    h = str(h)
    if len(h) == 1:
        h = '0' + h

    m = str(m)
    if len(m) == 1:
        m = '0' + m

    return h + ":" + m


for _ in range(int(input())):

    visited = set()

    s, x = input().split()
    x = int(x)

    ans = 0
    while s not in visited:

        if s == s[::-1]:
            ans += 1

        visited.add(s)
        s = add(s, x)

    print(ans)
