/*
    https://codeforces.com/problemset/problem/476/A
    Time: O(n)
    Space: O(1)
*/

#include <iostream>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;

    int ans = -1;
    for (int i = 0; i <= n / 2; ++i)
    {
        int j = (n - 2 * i);
        if ((i + j) % m == 0)
        {
            if (ans == -1 || ans > i + j)
                ans = i + j;
        }
    }

    cout << ans << endl;
}