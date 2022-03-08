
# Link - https://codeforces.com/problemset/problem/1629/A

# Space: O(n)
# Time: O(n^2)

from collections import Counter

def solution(a, b, k):

    store = Counter()
    for i in range(len(b)):
        store[(b[i], a[i])] += 1

    while store:
        
        M = (0, 0)

        for piece in store:
            if piece[1] <= k:
                M = max(M, piece)
        
        if M == (0, 0):
            return k
        
        store[M] -= 1
        if store[M] == 0:
            store.pop(M)
        k += M[0]
    
    return k

for _ in range(int(input())):

    _, k = (int(x) for x in input().split())

    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    print(solution(a, b, k))