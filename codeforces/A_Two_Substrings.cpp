/**
 * https://codeforces.com/problemset/problem/550/A
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

const int N = 1e5 + 1;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    string s;
    cin >> s;

    int ab = 1e6, ba = 1e6;

    for (int i = 1; i < (int)s.size(); ++i) {
        if (s[i] == 'A' && s[i - 1] == 'B') {
            if (ba < i - 1) {
                cout << "YES";
                return 0;
            }
            ab = min(ab, i);
        } else if (s[i] == 'B' && s[i - 1] == 'A') {
            if (ab < i - 1) {
                cout << "YES";
                return 0;
            }
            ba = min(ba, i);
        }
    }

    cout << "NO";
}
