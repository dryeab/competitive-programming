/**
 * https://codeforces.com/contest/1352/problem/E
 * Time: O(n ^ 2)
 * Space: O(n)
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

        int n;
        cin >> n;

        int a[n + 1], cnt[n + 1]{};

        a[0] = 0;
        for (int i = 1; i <= n; ++i) {
            cin >> a[i];
            int s = a[i];
            for (int j = i - 2; j >= 0; --j) {
                s += a[j + 1];
                if (s <= n)
                    cnt[s]++;
            }
        }

        int res = 0;
        for (int i = 1; i <= n; ++i)
            if (cnt[a[i]])
                res++;

        cout << res << '\n';
    }
}