
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())

    removed = [0 for _ in range(26)]

    for i in range(n):
        x = ord(s[i]) - 97

        while x and (removed[x] or k > 0):
            if removed[x] == 0:
                k -= 1
            removed[x] = 1
            x -= 1

        s[i] = chr(x + 97)

    print("".join(s))