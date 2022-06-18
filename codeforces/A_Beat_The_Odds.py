for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    even = odd = 0

    for x in a:
        if x % 2:
            odd += 1
        else:
            even += 1

    print(min(even, odd))