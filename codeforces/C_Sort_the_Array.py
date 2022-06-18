n = int(input())
a = [int(i) for i in input().split()]

i = 1
while i < n and a[i] >= a[i-1]:
    i += 1
j = i
while j < n and a[j] <= a[j-1]:
    j += 1

t = a[:i-1]+ a[i-1:j][::-1]+a[j:]

a.sort()

if t == a:
    print("yes")
    print(i, j)
else:
    print("no")
