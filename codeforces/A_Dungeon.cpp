/**
 * https://codeforces.com/contest/1463/problem/A
 * Time: O(1)
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

        int a, b, c;
        cin >> a >> b >> c;

        int tot = a + b + c;

        if (tot % 9 == 0 && tot / 9 <= min({a, b, c})) {
            cout << "YES";
        } else {
            cout << "NO";
        }

        cout << '\n';
    }
}