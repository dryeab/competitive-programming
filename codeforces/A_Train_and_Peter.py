atob = input()
first = input()
second = input()

ans = [0, 0]

one = atob.find(first)
if one != -1:
    two = atob[one+len(first):].find(second)
    if two != -1:
        ans[0] = 1

atob = atob[::-1]
one = atob.find(first)
if one != -1:
    two = atob[one+len(first):].find(second)
    if two != -1:
        ans[1] = 1

if sum(ans) == 2:
    print("both")
elif ans[0] == 1:
    print("forward")
elif ans[1] == 1:
    print('backward')
else:
    print('fantasy')
