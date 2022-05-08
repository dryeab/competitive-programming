
# Link - https://codeforces.com/problemset/problem/1646/B

# Space: O(1)
# Time: O(nlog(n))

def solution(arr):

    arr.sort()

    left = right = 0 # Sum(blue), Sum(red)
    i, j = 0, len(arr) - 1 # Count(blue), Count(red)

    while i < j:
        
        # print('outside', i, j)
        right += arr[j]

        while i < j and left < right:
            # print('inside', i, j)

            if i > len(arr) - j and left < right:
                return "YES"

            left += arr[i]
            i += 1

        if i > len(arr) - j and left < right:
            return "YES"

        j -= 1
    
    return "NO"

for _ in range(int(input())):
    _, arr = input(), [int(x) for x in input().split()]
    print(solution(arr))