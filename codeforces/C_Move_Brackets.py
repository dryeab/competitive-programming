
# https://codeforces.com/problemset/problem/1374/C
# Time: O(N)
# Space: O(N)

for _ in range(int(input())):

    n, s = int(input()), input()

    cnt = res = 0

    for x in s:
        cnt += 1 if x == '(' else -1
        if cnt < 0:
            res += 1
            cnt += 1

    print(res)
