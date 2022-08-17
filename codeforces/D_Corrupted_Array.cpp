/**
 * https://codeforces.com/problemset/problem/1512/D
 * Time: O(NlogN)
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

        int n, ok = -1;
        cin >> n;

        vector<int> b(n + 2);
        for (int &x : b)
            cin >> x;

        sort(b.begin(), b.end());

        ll sum = accumulate(b.begin(), b.end(), 0LL) - b[n + 1];

        if (sum == 2 * b[n])
            ok = n;
        else {
            auto i = find(b.begin(), b.end() - 1, sum - b[n + 1]);
            if (i != b.end() - 1)
                *i = 0, ok = n + 1;
        }

        if (ok != -1) {
            for (int i = 0; i < ok; ++i)
                if (b[i])
                    cout << b[i] << ' ';
        } else
            cout << -1;

        cout << "\n";
    }
}