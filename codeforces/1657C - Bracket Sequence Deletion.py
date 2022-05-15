for _ in range(int(input())):

    n = int(input())

    s = input()

    ops = removed = i = 0

    while i < (len(s) - 1):

        if s[i] == '(':
            removed += 2
            ops += 1
            i += 2
        else:
            l = i
            i += 1
            while i < n and s[i] == '(':
                i += 1

            if i < n:
                removed += i - l + 1
                ops += 1
            i += 1

    print(ops, n - removed)
