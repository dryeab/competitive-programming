/**
 * https://codeforces.com/problemset/problem/1490/C
 * Time: O(n)
 * Space: 
 */

#include <bits/stdc++.h>

using namespace std;

const int N = 1e5 + 5;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    set<long long> cubes;
    for (long long i = 1; i < N; ++i)
        cubes.insert(1ll * i * i * i);

    long long t, x;
    cin >> t;

    bool ok;
    while (t--) {

        ok = false;
        cin >> x;

        for (long long i : cubes) {
            if (i >= x)
                break;
            if (cubes.count(x - i)) {
                ok = true;
                break;
            }
        }
        cout << (ok ? "YES" : "NO") << endl;
    }
}