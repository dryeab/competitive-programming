#include <iostream>

using namespace std;

int data[100][2][4]{}; // col-spot-color

int main()
{
    int n, m;
    char gene;

    cin >> n >> m;

    for (int i = 0; i < 2 * n; ++i)
    {
        for (int j = 0; j < m; ++j)
        {
            cin >> gene;

            int index; // A- 0, C -1 , G - 2, T- 3

            if (gene == 'A')
                index = 0;
            if (gene == 'C')
                index = 1;
            if (gene == 'G')
                index = 2;
            if (gene == 'T')
                index = 3;

            data[j][i < n][index] = 1;
        }
    }

    int ans = 0;
    for (int col = 0; col < m; ++col)
    {
        int possible = 1;
        for (int color = 0; color < 4; ++color)
        {
            if (data[col][0][color] && data[col][1][color])
            {
                possible = 0;
                break;
            }
        }
        if (possible)
            ans++;
    }

    cout << ans;
}