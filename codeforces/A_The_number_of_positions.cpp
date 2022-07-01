/*
    https://codeforces.com/problemset/problem/124/A
    Time: O(n)
    Space: O(1)
*/

#include <iostream>

using namespace std;

int main()
{
    int n, a, b;
    cin >> n >> a >> b;

    int cnt = 0;
    for (int i = a; i < n; ++i)
        if (n - i - 1 <= b)
            ++cnt;

    cout << cnt << endl;
}