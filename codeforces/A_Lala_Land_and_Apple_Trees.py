# Link - https://codeforces.com/contest/558/problem/A
# Time: O(nlog(n))

n = int(input())

pos = []
neg = []

for _ in range(n):

    x, a = map(int, input().split())

    if x > 0:
        pos.append((x, a))
    else:
        neg.append((x, a))

pos.sort()
neg.sort(reverse=True)

pos = [x for _, x in pos]
neg = [x for _, x in neg]

if len(pos) == len(neg):
    print(sum(pos) + sum(neg))
else:

    ml = min(len(pos), len(neg))  # min length

    total = sum(pos[:ml]) + sum(neg[:ml])

    if len(pos) > ml:
        total += pos[ml]
    else:
        total += neg[ml]

    print(total)
