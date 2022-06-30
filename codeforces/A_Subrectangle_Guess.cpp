#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n, m;
        cin >> n >> m;

        int mr = 0, mc = 0, M, x;
        for (int i = 1; i <= n; ++i)
        {
            for (int j = 1; j <= m; ++j)
            {
                cin >> x;
                if (!mr || M < x)
                {
                    mr = i;
                    mc = j;
                    M = x;
                }
            }
        }

        int h = max(mr, n - mr + 1);
        int w = max(mc, m - mc + 1);

        cout << h * w << endl;
    }
}