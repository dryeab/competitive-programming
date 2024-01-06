#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

/*

*/

void solve() {
    int n;
    cin >> n;

    vector<int> cnta(51);
    vector<vector<int>> cntb(n, vector<int>(51));

    for (int i = 0; i < n; ++i) {
        int k, x;
        cin >> k;
        while (k--) {
            cin >> x;
            cnta[x]++;
            cntb[i][x]++;
        }
    }

    int res = 0;
    for (int i = 0; i < 51; ++i) {
        if (!cnta[i])
            continue;
        vector<int> cntc(51);
        for (int j = 0; j < n; ++j) {
            if (cntb[j][i])
                continue;
            for (int k = 0; k < 51; ++k)
                if (cntb[j][k])
                    cntc[k] = 1;
        }
        res = max(res, (int)count(cntc.begin(), cntc.end(), 1));
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