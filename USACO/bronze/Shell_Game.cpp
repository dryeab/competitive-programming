#include <iostream>
#include <vector>

using namespace std;

int main()
{

    int N, x, p;
    cin >> N;

    vector<vector<int>> v(N, vector<int>(3));

    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < 3; ++j)
        {
            cin >> v[i][j];
        }
    }

    int count[3] = {};

    for (int i = 1; i < 4; ++i)
    {
        p = i;

        for (int j = 0; j < N; ++j)
        {
            cout << i << p << endl;

            if (v[j][0] == p)
            {
                p = v[j][1];
            }

            else
            {
                if (v[j][1] == p)
                {
                    p = v[j][0];
                }
            }
            count[i] += (p == v[j][2]);
        }
    }

    int ans = 0;
    for (auto x : count)
        ans = max(ans, x);

    cout << ans;

    return 0;
}