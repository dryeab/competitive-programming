#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n, m, a;
    cin >> n >> m;

    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
        {
            cin >> a;
            if ((i + j) % 2 != a % 2)
                a++;
            printf("%d ", a);
        }
        printf("\n");
    }
}

int main()
{
    int t;
    cin >> t;

    while (t--)
        solve();
}