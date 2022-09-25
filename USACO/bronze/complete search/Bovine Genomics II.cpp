/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=739
 * Time: O(NM^3)
 * Space: O(NM)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

const int MAX_N = 500, MAX_M = 50;
int spotty[MAX_N][MAX_M], plain[MAX_N][MAX_M];

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("cownomics.in", "r", stdin);
    freopen("cownomics.out", "w", stdout);

    int n, m;
    cin >> n >> m;

    char c;

    map<char, int> mp = {{'A', 0}, {'C', 1}, {'G', 2}, {'T', 3}};

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> c;
            spotty[i][j] = mp[c];
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> c;
            plain[i][j] = mp[c];
        }
    }

    int res = 0;
    for (int i = 0; i < m; ++i) {
        for (int j = i + 1; j < m; ++j) {
            for (int k = j + 1; k < m; ++k) {

                bool found[350] = {};
                for (int l = 0; l < n; ++l)
                    found[spotty[l][i] * 100 + spotty[l][j] * 10 + spotty[l][k]] = true;

                bool ok = true;
                for (int l = 0; l < n; ++l) {
                    if (found[plain[l][i] * 100 + plain[l][j] * 10 + plain[l][k]]) {
                        ok = false;
                        break;
                    }
                }

                res += ok;
            }
        }
    }

    cout << res;
}