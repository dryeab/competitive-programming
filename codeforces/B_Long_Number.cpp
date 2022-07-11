/**
 * https://codeforces.com/contest/1157/problem/B
 * Time:
 * Space:
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    int mp[10];
    string s;

    cin >> s;

    for (int i = 1; i < 10; ++i)
        cin >> mp[i];

    bool ok = true;
    for (int i = 0; i < s.size();) {
        int x = s[i] - '0';
        if (ok && x < mp[x]) {
            while (x <= mp[x]) {
                cout << mp[x];
                x = s[++i] - '0';
            }
            ok = false;
        } else {
            cout << x;
            i++;
        }
    }
}