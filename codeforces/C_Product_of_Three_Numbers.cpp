/**
 * https://codeforces.com/problemset/problem/1294/C
 * Time: O(sqrt(n) * sqrt(sqrt(n)))
 * Space: O(1)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

void solve() {

    int n;
    cin >> n;

    for (int a = 2; a <= sqrt(n); ++a) {
        if (n % a)
            continue;
        int n2 = n / a;
        for (int b = 2; b <= sqrt(n2); ++b) {
            if (a == b || n2 % b)
                continue;
            if (a != n2 / b && b != n2 / b) {
                cout << "YES \n";
                cout << a << ' ' << b << ' ' << n2 / b << "\n";
                return;
            }
        }
    }

    cout << "NO \n";
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {
        solve();
    }
}
