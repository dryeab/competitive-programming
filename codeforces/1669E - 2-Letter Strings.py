for _ in range(int(input())):

    n = int(input())

    starts = [[0 for _ in range(11)] for _ in range(11)]
    ends = [[0 for _ in range(11)] for _ in range(11)]

    ans = 0

    for _ in range(n):

        s = input()

        f, l = ord(s[0]) - ord('a'), ord(s[1]) - ord('a')

        ans += sum(starts[f]) - starts[f][l]
        ans += sum(ends[l]) - ends[l][f]

        starts[f][l] += 1
        ends[l][f] += 1

    print(ans)
