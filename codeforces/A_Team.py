n = int(input())

count = 0
for _ in range(n):
    x = [int(x) for x in input().split()]
    if sum(x) > 1:
        count += 1

print(count)