/**
 * https://codeforces.com/problemset/problem/1369/B
 * Time: O(N)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {

        int n;
        cin >> n;

        string s;
        cin >> s;

        string res1, res2;
        for (int i = 0; i < n; ++i)
            if (s[i] == '0')
                res1.push_back('0');
            else
                break;

        for (int i = n - 1; i >= 0; --i)
            if (s[i] == '1')
                res2.push_back('1');
            else
                break;

        cout << (res1 + (res1.size() + res2.size() == n ? "" : "0") + res2) << '\n';
    }
}