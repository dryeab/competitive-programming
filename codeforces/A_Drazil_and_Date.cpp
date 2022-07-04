/**
 * https://codeforces.com/problemset/problem/515/A
 * Time: O(1)
 * Space: O(1)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {
    int a, b, s;
    cin >> a >> b >> s;

    if (a < 0)
        a = -a;
    if (b < 0)
        b = -b;

    if (s < a + b)
        cout << "No";
    else if (s == a + b)
        cout << "Yes";
    else {
        if ((s - (a + b)) & 1)
            cout << "No";
        else
            cout << "Yes";
    }
}