for _ in range(int(input())):

    a, s = input().split()

    i, j = len(a) - 1, len(s) - 1

    possible = True

    b = ""

    while i >= 0 and j >= 0:

        if s[j] == a[i]:
            b = "0"+b
            j -= 1

        elif a[i] > s[j]:
            if j == 0 or s[j-1] != '1':
                possible = False
                break
            b = str(int(s[j-1:j+1]) - int(a[i])) + b
            j -= 2
        else:
            b = str(int(s[j]) - int(a[i])) + b
            j -= 1

        i -= 1

    if not possible or i >= 0:
        print(-1)
    else:
        if j >= 0:
            b = s[:j+1] + b
        print(int(b))
