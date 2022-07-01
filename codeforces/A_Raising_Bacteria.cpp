/*
    https://codeforces.com/problemset/problem/579/A
    Time: O(log(x))
    Space: O(1)
*/

#include <iostream>

using namespace std;

int main()
{
    int x;
    cin >> x;

    int ans = 0;
    while (x)
    {
        if (x % 2)
            ans += 1;
        x /= 2;
    }

    cout << ans << endl;
}