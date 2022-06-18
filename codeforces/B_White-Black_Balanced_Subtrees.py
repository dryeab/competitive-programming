from collections import defaultdict
import sys, io, os
if 'PyPy' in sys.version:
    from _continuation import continulet
else:
    import threading

def solve():
    pass

def main():
    # write your code here
    count = 0
    def dfs(i, s):
        nonlocal count
    
        res = 1 if s[i - 1] == 'W' else -1
    
        for neighbor in graph[i]:
            res += dfs(neighbor, s)
    
        if res == 0:
            count += 1
    
        return res
 
 
    for _ in range(int(input())):
    
        count = 0
    
        n = int(input())
    
        a = [int(x) for x in input().split()]
        s = input()
    
        graph = defaultdict(list)
    
        for i in range(n-1):
            graph[a[i]].append(i + 2)
    
        dfs(1, s)
    
        print(count)

if __name__ == '__main__':
    if 'PyPy' in sys.version:

        def bootstrap(cont):
            call, arg = cont.switch()
            while True:
                call, arg = cont.switch(
                    to=continulet(lambda _, f, args: f(*args), call, arg))
        cont = continulet(bootstrap)
        cont.switch()
        main()
    else:
        sys.setrecursionlimit(1 << 30)
        threading.stack_size(1 << 27)

        main_thread = threading.Thread(target=main)
        main_thread.start()
        main_thread.join()