for _ in range(int(input())):
    a, b , c, d = [int(x) for x in input().split()]

    count = 0

    if b > a:
        count += 1
    if c > a:
        count += 1
    if d > a:
        count += 1

    print(count)