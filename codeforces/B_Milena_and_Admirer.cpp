#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

/*

*/

void solve() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int res = 0;
    for (int i = n - 2, x = a[n - 1]; i >= 0; --i) {
        res += (a[i] - 1) / x;
        if (a[i] % x)
            x = a[i] % x;
    }

    cout << res << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t = 1;
    cin >> t;

    while (t--) {
        solve();
    }
}