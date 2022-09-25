/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=668
 * Time: O(N^3)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

struct Cow {
    int x, y, p;
};

const int N = 205;
Cow cow[N];

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("moocast.in", "r", stdin);
    freopen("moocast.out", "w", stdout);

    int n;
    cin >> n;

    for (int i = 1; i <= n; ++i)
        cin >> cow[i].x >> cow[i].y >> cow[i].p;

    auto canReach = [&](int i, int j) {
        int x = cow[i].x - cow[j].x, y = cow[i].y - cow[j].y, p = cow[i].p;
        return ((x * x) + (y * y)) <= (p * p);
    };

    function<int(int, vector<bool> &)> dfs;
    dfs = [&](int i, vector<bool> &visited) {
        if (visited[i])
            return 0;

        visited[i] = true;

        int res = 1;
        for (int j = 1; j <= n; ++j)
            if (canReach(i, j))
                res += dfs(j, visited);

        return res;
    };

    int res = 0;
    for (int i = 1; i <= n; ++i) {
        vector<bool> visited(n + 1);
        res = max(res, dfs(i, visited));
    }

    cout << res;
}
