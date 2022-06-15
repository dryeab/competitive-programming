# Link - https://codeforces.com/contest/558/problem/B
# Time: O(n)

from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

M, counter = 0, defaultdict(int)
first, last = {}, {}

for i, x in enumerate(a):
    counter[x] += 1
    M = max(M, counter[x])
    if x not in first:
        first[x] = i
    last[x] = i

l, r = -1, -1
for x in a:
    if counter[x] == M:
        if l == -1 or last[x] - first[x] < r - l:
            l, r = first[x], last[x]

print(l + 1, r + 1)

"""

# find the max freq
m, counter = 0, defaultdict(int)
for x in a:
    counter[x] += 1
    m = max(m, counter[x])

counter.clear()

i, j = 0, 0
l, r = -1, -1

# sliding window
while j < n:
    counter[a[j]] += 1
    while counter[a[j]] >= m:
        if l == -1 or r - l > j - i:
            l, r = i, j
        counter[a[i]] -= 1
        i += 1
    j += 1

print(l + 1, r + 1)


"""
