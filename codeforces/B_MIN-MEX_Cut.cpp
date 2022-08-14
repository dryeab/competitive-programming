/**
 * https://codeforces.com/contest/1566/problem/B
 * Time: O(N)
 * Space: O(1)
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

        string s;
        cin >> s;

        int res = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '0')
                res += (i == 0 || s[i - 1] == '1');
        }

        cout << min(2, res) << '\n';
    }
}