/**
 * https://codeforces.com/contest/1675/problem/E
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

void solve() {
    
    int n, k;
    cin >> n >> k;

    string s;
    cin >> s;

    int change[26]{};
    for (int i = 0; i < s.size(); ++i) {
        while (s[i] != 'a' && (change[s[i] - 97] || k > 0)) {
            if (change[s[i] - 97])
                s[i] += change[s[i] - 97];
            else {
                change[s[i] - 97]--;
                s[i] -= 1;
                k--;
            }
        }
    }

    cout << s << '\n';
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--)
        solve();
}