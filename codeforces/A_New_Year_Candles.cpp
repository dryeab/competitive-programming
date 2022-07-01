/*
    https://codeforces.com/problemset/problem/379/A
    Time: O(1)
    Space: O(1)
*/

#include <iostream>
#include <algorithm>

using namespace std;

int solve1(int a, int b) // O(a)
{
    int ans = a;
    for (int i = b; i <= a; i += b - 1)
    {
        ans += 1;
    }

    return ans;
}

int solve2(int a, int b) // O(1)
{
    int ans = a;
    if (b <= a)
        ans += (a - b) / (b - 1) + 1;
    
    return ans;
}

int main()
{
    int a, b;
    cin >> a >> b;

    cout << solve2(a, b) << endl;
}