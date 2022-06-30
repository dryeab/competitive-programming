def solve(s):

    ans = 0
    for i in range(len(s)):
        if i == 0 or s[i] != s[i-1]:
            if ans >= 7:
                return "YES"
            ans = 0
        ans += 1

    return "YES" if ans >= 7 else "NO"


s = input()

print(solve(s))
