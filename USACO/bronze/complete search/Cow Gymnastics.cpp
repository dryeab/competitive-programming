/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=963
 * Time: O(KN^2)
 * Space: O(KN)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("gymnastics.in", "r", stdin);
    freopen("gymnastics.out", "w", stdout);

    int n, k;
    cin >> k >> n;

    vector<vector<int>> score(k, vector<int>(n));
    for (int i = 0; i < k; ++i) {
        for (int j = 0; j < n; ++j) {
            int cow;
            cin >> cow;
            score[i][cow - 1] = j;
        }
    }

    int res = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int t = 0; // number of times i exceeds j
            for (int l = 0; l < k; ++l) {
                t += score[l][i] > score[l][j];
            }
            res += (t == 0 || t == k);
        }
    }

    cout << res;
}