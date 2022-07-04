/**
 * https://codeforces.com/problemset/problem/1230/B
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, k;
    string s;

    cin >> n >> k;
    cin >> s;

    if (k == 0) {
        cout << s;
        return 0;
    }

    if (n == 1) {
        cout << "0";
        return 0;
    }

    if (s[0] != '1') {
        s[0] = '1';
        k--;
    }

    for (int i = 1; i < n; ++i) {
        if (k == 0)
            break;
        if (s[i] != '0') {
            s[i] = '0';
            k--;
        }
    }

    cout << s;
}