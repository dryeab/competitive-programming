/*
    https://codeforces.com/problemset/problem/479/A
    Time: O(1)
    Space: O(1)
*/

#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int a, b, c;
    cin >> a >> b >> c;

    cout << max({a + b + c, a * b * c, (a + b) * c, a * (b + c)}) << endl;
}