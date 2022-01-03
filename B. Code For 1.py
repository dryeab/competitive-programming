# link - https://codeforces.com/problemset/problem/768/B
# space: O(log(n))
# time: O(log(n))

def findNums(n):
    ans = []
    while n != 1:
        ans.append(n)
        n //= 2
    return ans

def findAnswer(count, nums, i):

    mods = i // 4

    ans = (count[3]*((i-mods)//3)) + count[(i-mods) % 3]

    j, interval = 0, 4

    while (j < len(nums)):

        num = nums[j]

        if interval > i:
            break

        temp = 1 + (i-interval)//(interval*2)

        ans += temp*(num % 2)
        interval *= 2
        j += 1

    return ans

def solution(n, l, r):

    if n <= 1:
        print(n)
        return n

    nums = findNums(n)
    last = nums.pop()
    nums = nums[::-1]
    bottom = [last//2, last % 2, last//2]

    c, count = 0, {}
    count[0] = 0
    for i in range(len(bottom)):
        if bottom[i] == 1:
            c += 1
        count[i+1] = c

    ans = findAnswer(count, nums, r) - findAnswer(count, nums, l-1)

    print(ans)
    return ans


inp = input().split(" ")
n, l, r = (int(i) for i in inp)
solution(n, l, r)
