
# link - https://codeforces.com/problemset/problem/1/A

def solution(m, n, a):
    if n%a:
        n = a*(n//a) + a
    if m%a: 
        m = a*(m//a) + a
 
    return (m*n)//(a*a)
 
 
m, n, a = input().split()
m, n, a = (int(x) for x in (m, n, a))
 
print(solution(m, n, a))
