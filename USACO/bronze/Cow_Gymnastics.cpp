#include <iostream>

using namespace std;

int rnk[21][21]{};

int main()
{
    int k, n;
    cin >> k >> n;

    int r[20];

    for (int i = 0; i < k; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            cin >> r[j];
        }

        for (int c = 1; c <= n; ++c)
        {
            for (auto x : r)
            {
                if (x == c)
                    break;
                rnk[c][x] = 1;
            }
        }
    }

    int ans = 0;
    for (int i = 1; i <= n; ++i)
    {
        for (int j = 1; j <= n; ++j)
        {
            if (i != j && rnk[i][j] == 0)
                ans++;
        }
    }

    cout << ans;
}