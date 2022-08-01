
x = input()
res = 0

for i in x:
    i = int(i)
    res = res * 10 + (min(9 - i, i) if res or (i != 9) else 9)

print(res)
