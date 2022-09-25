/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=784
 * Time: O(NT)
 * Space: O(N + T)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("lifeguards.in", "r", stdin);
    freopen("lifeguards.out", "w", stdout);

    int n;
    cin >> n;

    int start[100], end[100], cnt[1001] = {};
    for (int i = 0; i < n; ++i) {
        cin >> start[i] >> end[i];
        for (int j = start[i]; j < end[i]; ++j)
            cnt[j]++;
    }

    int res = 0, covered = 1001 - count(cnt, cnt + 1001, 0);
    for (int i = 0; i < n; ++i) {
        int cur = covered;
        for (int j = start[i]; j < end[i]; ++j)
            if (cnt[j] == 1)
                cur--;
        res = max(res, cur);
    }

    cout << res;
}