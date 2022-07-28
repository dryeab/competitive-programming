#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;

    cin >> n;

    int a[n];
    for (int i = 0; i < n; ++i)
        cin >> a[i];

    cin >> m;

    int b[m];
    for (int i = 0; i < m; ++i)
        cin >> b[i];

    sort(a, a + n);
    sort(b, b + m);

    int dp[n][m];
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            int dif = abs(a[i] - b[j]) < 2;
            if (i == 0 && j == 0)
                dp[i][j] = dif;
            else if (i == 0)
                dp[i][j] = max(dp[i][j - 1], dif);
            else if (j == 0)
                dp[i][j] = max(dp[i - 1][j], dif);
            else
                dp[i][j] = max({dp[i - 1][j - 1] + dif, dp[i - 1][j], dp[i][j - 1]});
        }
    }

    cout << dp[n - 1][m - 1];
}