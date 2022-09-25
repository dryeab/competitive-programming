/**
 * http://usaco.org/index.php?page=viewproblem2&cpid=1203
 * Time: O(NM) -> M - number of divisors of sum(a)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

const int MAX_N = 1e5;
int a[MAX_N];

int solve() {

    int n, sum = 0;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        sum += a[i];
    }

    if (sum == 0)
        return 0;

    int res = n - 1;
    for (int i = 1; i <= sum; ++i) {

        if (sum % i)
            continue;

        int cur = 0, step = 0, cnt = 0;
        for (int j = 0; j < n; ++j) {

            if (cur == i) {
                step += cnt - 1;
                cur = 0, cnt = 0;
            }

            cur += a[j], cnt++;
        }

        if (cur == i)
            res = min(res, step + cnt - 1);
    }

    return res;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--)
        cout << solve() << "\n";
}