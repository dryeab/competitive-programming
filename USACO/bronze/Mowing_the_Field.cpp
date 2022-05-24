#include <iostream>

using namespace std;

int grid[2005][2005]{}; // last time visit
int r = 1000, c = 1000, t = 1, ans = -1;
int dxn[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int main()
{

    int n;
    cin >> n;

    char d;
    int s;

    while (n--)
    {
        cin >> d >> s;
        for (int i = 0; i < s; ++i)
        {
            int index, nr, nc;
            if (d == 'N')
                index = 0;
            if (d == 'E')
                index = 1;
            if (d == 'W')
                index = 2;
            if (d == 'S')
                index = 3;

            nr = r + dxn[index][0];
            nc = c + dxn[index][1];

            if (grid[nr][nc])
            {
                if (ans == -1)
                    ans = t - grid[nr][nc];
                else
                    ans = min(ans, t - grid[nr][nc]);
            }

            grid[nr][nc] = t;

            r = nr;
            c = nc;

            t++;
        }
    }

    cout << ans;
}