#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    int a[n], b[n];
    for (int i = 0; i < n; ++i) {
        cin >> a[i] >> b[i];
        b[i] = a[i] - b[i];
    }

    ll total = accumulate(a, a + n, 0ll);

    sort(b, b + n, greater<int>());

    int i = 0;
    for (; i < n && total > m; ++i)
        total -= b[i];

    cout << (total > m ? -1 : i);
}