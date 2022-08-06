/**
 * https://codeforces.com/problemset/problem/1454/C
 * Time: O(N)
 * Space: O(N)
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

        int n, a;
        cin >> n;

        vector<int> last(n), res(n, 0);
        for (int i = 1; i <= n; ++i) {
            cin >> a;
            a--;
            res[a] += (last[a] + 1 != i);
            last[a] = i;
        }

        int ans = INT_MAX;
        for (int i = 0; i < n; ++i)
            if (last[i])
                ans = min(ans, res[i] + (last[i] != n));

        cout << ans << '\n';
    }
}