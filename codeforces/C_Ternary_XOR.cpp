/**
 * https://codeforces.com/problemset/problem/1328/C
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

        char x;
        cin >> x;

        string a = "1", b = "1";
        bool first = true;

        for (int i = 1; i < n; ++i) {
            cin >> x;
            if (x == '0')
                a.push_back('0'), b.push_back('0');
            else if (x == '1') {
                if (first) {
                    a.push_back('1');
                    b.push_back('0');
                    first = false;
                } else {
                    a.push_back('0');
                    b.push_back('1');
                }
            } else {
                if (!first) {
                    a.push_back('0');
                    b.push_back('2');
                } else {
                    a.push_back('1');
                    b.push_back('1');
                }
            }
        }

        cout << a << '\n'
             << b << '\n';
    }
}