"""
 * https://codeforces.com/problemset/problem/115/A
 * Time: O(N)
 * Space: O(N)
"""


from functools import lru_cache
import sys
sys.setrecursionlimit(10**4)

n = int(input())

parent = [-1 for _ in range(n)]

for i in range(n):
    p = int(input())
    if p != -1:
        p -= 1
    parent[i] = p


@lru_cache(None)
def dp(i):
    if parent[i] == -1:
        return 1
    return 1 + dp(parent[i])


print(max(dp(i) for i in range(n)))
