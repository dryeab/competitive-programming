def solve(s):

    one, two = 1, 1

    if s[0] in ['w', 'm']:
        return 0
        
    for i in range(1, len(s)):
        if s[i] == 'w' or s[i] == 'm':
            return 0
        three = two
        if s[i] in ['u', 'n'] and s[i-1] == s[i]:
            three += one
        one, two = two, three
        two %= 10**9 + 7

    return two


s = input()

print(solve(s))
