# https://codeforces.com/problemset/problem/1618/A
# Time: O(1)
# Space: O(1)

for _ in range(int(input())):
    b = list(map(int, input().split()))
    print(b[0], b[1], b[-1] - b[1] - b[0])
