import sys, threading

# ------ Input Template --------

input = sys.stdin.readline

def iint():
    """ int """
    return int(input())

def ilint():
    """ List[int] """
    return list(map(int,input().split()))

def ilstr():
    """ List[str] """
    s = input()
    return list(s[:len(s)-1])

def imint():
    """ Map[int] """
    return map(int,input().split())

def main():
    pass

if __name__ == '__main__':
    # if recustion?
    # sys.setrecursionlimit(1 << 30)
    # threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

