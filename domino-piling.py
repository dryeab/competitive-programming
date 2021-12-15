# link - https://codeforces.com/problemset/problem/50/A

def solution(m, n):
    def wrapper(m,n):
        if not(m%2 or n%2):
            return (m*n)/2
        x = m-1
        return (x*n)/2 + n//2
    return int(wrapper(m,n))

print(solution(5,5))
    
