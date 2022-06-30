
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    for i in range(k):
        if a[i] <= b[-(i+1)]:
            a[i], b[-(i+1)] = b[-(i+1)], a[i]
        else:
            break

    print(sum(a))
