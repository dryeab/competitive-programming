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

    int mn = *min_element(a.begin(), a.end());

    for (int i = 0; i < n; ++i) {
        if (a[i] == mn) {
            for (int j = i + 1; j < n; ++j) {
                if (a[j] < a[j - 1]) {
                    cout << "-1\n";
                    return;
                }
            }
            cout << i << "\n";
            return;
        }
    }
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