/**
 * https://codeforces.com/contest/186/problem/B
 * Time: O(nlog(n))
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, t1, t2, k;
    cin >> n >> t1 >> t2 >> k;

    double a, b, mx;
    vector<pair<double, int>> score(n); // score, i

    for (int i = 1; i <= n; ++i) {
        cin >> a >> b;
        mx = max(a * t1 - (a * t1 * k / 100.0) + b * t2, b * t1 - (b * t1 * k / 100.0) + a * t2);
        score[i - 1] = {-mx, i};
    }

    sort(score.begin(), score.end());

    for (int i = 0; i < n; ++i)
        cout << score[i].second << " " << fixed << setprecision(2) << -score[i].first << "\n";
}