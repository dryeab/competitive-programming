from collections import defaultdict


def yes(a, b, c):
    sum = a + b + c
    return sum % 10 == 3


def solve(count):

    for i in range(10):
        if count[i] != 0:
            for j in range(10):
                if count[j] != 0:
                    for k in range(10):
                        if count[k] != 0:
                            if i == j == k and count[i] < 3:
                                continue
                            if i == j and count[i] < 2:
                                continue
                            if i == k and count[i] < 2:
                                continue
                            if j == k and count[j] < 2:
                                continue
                            if yes(i, j, k):
                                return "Yes"

    return "No"


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count = defaultdict(int)
    for x in a:
        count[x % 10] += 1

    print(solve(count))
