/**
 * https://codeforces.com/problemset/problem/451/B
 * Time: O(NlogN)
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

    vector<int> a(n), b(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        b[i] = a[i];
    }

    sort(b.begin(), b.end());

    int first = -1, last = -1;
    for (int i = 0; i < n; ++i) {
        if (a[i] != b[i]) {
            if (first == -1)
                first = i;
            last = i;
        }
    }

    bool ok = true;
    for (int i = first, j = last; i < n && i <= last && j >= first && j >= 0; --j, ++i) {
        if (a[i] != b[j]) {
            ok = false;
            break;
        }
    }

    if (ok) {
        if (first == -1)
            ++first, ++last;
        cout << "yes \n";
        cout << first + 1 << ' ' << last + 1;
    } else
        cout << "no";
}