/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=736
 * Time: O(NM)
 * Space: O(M)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("cownomics.in", "r", stdin);
    freopen("cownomics.out", "w", stdout);

    int n, m;
    cin >> n >> m;

    char c;

    map<char, int> mp = {{'A', 0}, {'C', 1}, {'G', 2}, {'T', 3}};

    vector<vector<bool>> found(m, vector<bool>(4));
    vector<bool> res(m, true);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> c;
            found[j][mp[c]] = true;
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> c;
            if (found[j][mp[c]])
                res[j] = false;
        }
    }

    cout << count(res.begin(), res.end(), true);
}