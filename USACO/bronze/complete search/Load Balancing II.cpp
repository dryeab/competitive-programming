/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=619
 * Time: O(N^2)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("balancing.in", "r", stdin);
    freopen("balancing.out", "w", stdout);

    int n;
    cin >> n;

    vector<pair<int, int>> cow(n);
    for (int i = 0; i < n; ++i)
        cin >> cow[i].first >> cow[i].second;

    sort(cow.begin(), cow.end());

    int res = n;
    for (int i = 0; i < n; ++i) {

        vector<pair<int, int>> below, above;
        for (int j = 0; j < n; ++j) {
            if (cow[i].second >= cow[j].second)
                below.push_back(cow[j]);
            else
                above.push_back(cow[j]);
        }

        int belowIdx = 0, aboveIdx = 0;
        for (int k = 0; k < n; ++k) {

            while (belowIdx < (int)below.size() && below[belowIdx].first <= cow[k].first)
                belowIdx++;

            while (aboveIdx < (int)above.size() && above[aboveIdx].first <= cow[k].first)
                aboveIdx++;

            res = min(res, max({
                               belowIdx,
                               (int)below.size() - belowIdx,
                               aboveIdx,
                               (int)above.size() - aboveIdx,
                           }));
        }
    }

    cout << res;
}
