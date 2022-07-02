#include <bits/stdc++.h>

using namespace std;

const int M = 1e5 + 5;

int t[M];
int gap[M];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, k;
    cin >> n >> k;

    for (int i = 0; i < n; ++i)
        cin >> t[i];

    int res = n;

    if (k >= n)
    {
        cout << res << endl;
        return 0;
    }

    sort(t, t + n);
    for (int i = 1; i < n; ++i)
        gap[i - 1] = -(t[i] - t[i - 1] - 1);

    sort(gap, gap + n - 1);

    k--;
    for (int i = k; i < n - 1; ++i)
        res += -gap[i];

    cout << res << endl;
}