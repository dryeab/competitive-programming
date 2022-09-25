/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=1060
 * Time: O(N^2)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> p(n);
    for (int &x : p)
        cin >> x;

    int res = 0;
    for (int i = 0; i < n; ++i) {

        int sum = 0;
        set<double> found;

        for (int j = i; j < n; ++j) {
            found.insert(p[j]);
            sum += p[j];
            res += found.count((1.0 * sum) / (j - i + 1));
        }
    }

    cout << res;
}