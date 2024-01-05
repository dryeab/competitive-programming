#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

/*

*/

void solve() {
    int m;
    cin >> m;

    vector<int> cnt(50);
    while (m--) {
        int t, v;
        cin >> t >> v;
        if (t == 1) {
            cnt[v]++;
        } else {
            int ok = 1;
            for (int i = 0, j = 0; i < 32; ++i, j /= 2) {
                if (((v >> i) & 1)) {
                    if (cnt[i] == 0 && j == 0) {
                        ok = 0;
                        break;
                    } else {
                        j--;
                    }
                }
                j += cnt[i];
            }
            cout << (ok ? "YES" : "NO") << "\n";
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t = 1;
    // cin >> t;

    while (t--) {
        solve();
    }
}