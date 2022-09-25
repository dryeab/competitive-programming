#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("pails.in", "r", stdin);
    freopen("pails.out", "w", stdout);

    int x, y, m, res = 0;
    cin >> x >> y >> m;

    for (int i = 0; i <= m; ++i) {
        for (int j = 0; j <= m; ++j) {
            int pos = i * x + j * y;
            if (pos <= m)
                res = max(res, pos);
        }
    }

    // vector<bool> pos(m + 1);
    // pos[0] = true;

    // for (int i = x; i <= m; ++i) {
    //     pos[i] = pos[i - x];
    //     if (i - y >= 0 && pos[i - y])
    //         pos[i] = true;
    //     if (pos[i])
    //         res = i;
    // }

    cout << res;
}