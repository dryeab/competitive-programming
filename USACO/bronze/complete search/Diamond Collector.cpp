/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=639
 * Time: O(N^2)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("diamond.in", "r", stdin);
    freopen("diamond.out", "w", stdout);

    int n, k;
    cin >> n >> k;

    vector<int> a(n);
    for (int &i : a)
        cin >> i;

    sort(a.begin(), a.end());

    int res = 0;
    for (int i = 0; i < n; ++i) {

        int j;
        for (j = i; j < n && a[j] - a[i] <= k; ++j)
            ;

        res = max(res, j - i);
    }

    cout << res;
}